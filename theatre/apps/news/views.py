from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NewsPost, ImagePost, Comment, Tag, ActionType
from .forms import CommentForm
from category.models import Studio


def all_news_data(request):
    '''
    Generate page with all news with links on specific posts
    :param request:
    :return:
    '''
    template = 'news/news.html'
    context = {'data': ''}
    try:
        all_news_posts = ActionType.objects.get(title='Новость').actions.order_by('-pubdate')
        for_post_page_data = [[post, len(Comment.objects.filter(post=post))] for post in all_news_posts]
        page = request.GET.get('page')
        if page is None:
            page = '1'
        paginator = Paginator(for_post_page_data, 5)
        try:
            posts_data = paginator.page(int(page))
        except PageNotAnInteger:
            posts_data = paginator.page(1)
        except EmptyPage:
            posts_data = paginator.page(paginator.num_pages)
        except Exception as _ex:
            context['data'] = []
            print(f'{_ex}')

        context['data'] = posts_data
        return render(request, template, context)

    except Exception as ex:
        context['data'] = []
        print(ex)
    return render(request, template, context)


def post_data(request, post_id):
    '''
    Generate page with specific news post
    :param request:
    :param post_id:
    :return response:
    '''
    template = 'news/post.html'
    studio = Studio.objects.get(pk=1)
    data_from_post = NewsPost.objects.get(id=post_id)
    for_twitter = data_from_post.title.replace(' ', '%20')
    links = {
        'vk': f'https://vk.com/share.php?url=$LINK$&title={data_from_post.title}&utm_source=share2',
        'twitter': f'https://twitter.com/intent/tweet?text={for_twitter}&url=$LINK$&utm_source=share2'
    }
    images = ImagePost.objects.filter(product=data_from_post)
    last_five_pubs = [(i.title, i.id) for i in ActionType.objects.get(title='Новость').actions.order_by('-pubdate')[:5]]
    # If user writes comment below the post
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            try:
                comment = _move_data_from_form_to_comment_model(form, comment, data_from_post)
                comment.save()
                return redirect('one_post', post_id)
            except ChildProcessError as ex:
                print('ERROR: incorrect data', ex, sep='\n')
    form = CommentForm()
    comments = Comment.objects.filter(post=data_from_post)
    for img in images:
        try:
            img.video = _set_youtube_link_normal(img.video, controls=False)
            img.save()
        except AttributeError:
            pass

    context = {
        'data': data_from_post,
        'images': images,
        'last_pubs': last_five_pubs,
        'comments': comments.order_by('-pubdate')[:5],
        'comments_count': len(comments),
        'form': form,
        'studio': studio,
        'links': links,
    }
    return render(request, template, context)


def gallery_of_different_images(request):
    """
    Function which renders all images of posts like gallery
    :param request:
    :return render: page with Images Gallery
    """
    template = 'news/gallery.html'
    all_images = [img.image.url for img in ImagePost.objects.filter(id=0) if img.image.name != '']
    all_tags = Tag.objects.all()
    context = {'images': all_images, 'tags': all_tags}
    return render(request, template, context)


def render_json_with_images_paths(request, tag):
    all_that_possible = ['all_images', 'all-images']
    if tag in all_that_possible:
        images = list(ImagePost.objects.all().values('image'))
        while {'image': ''} in images:
            images.remove({'image': ''})
        return JsonResponse(images, safe=False)
    try:
        tag_obj = Tag.objects.get(title=tag).images.all().values('image')
    except Exception as ex:
        print(f'ERROR == --{ex}--')
        tag_obj = []
    return JsonResponse(list(tag_obj), safe=False)


def render_json_with_comments(request, post_id, comment_index):
    cur_post = NewsPost.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=cur_post).order_by('-pubdate')
    if (len(comments) - comment_index) > 5:
        comments = comments[comment_index:comment_index + 5]
    else:
        comments = comments[comment_index:]
    comments_data = []
    for comment_object in comments:
        comment = dict()
        comment['author'] = comment_object.author
        comment['text'] = comment_object.text
        if comment_object.pubdate.month < 10:
            month = f'0{comment_object.pubdate.month}'
        else:
            month = f'{comment_object.pubdate.month}'
        comment['pubdate'] = f'{comment_object.pubdate.day}.{month}.{comment_object.pubdate.year}'
        comments_data.append(comment)
    return JsonResponse(comments_data, safe=False)


def actions(request):
    '''
    Generate page with all action's post
    :param request:
    :return:
    '''
    template = 'news/actions.html'
    context = {}
    try:
        all_actions = ActionType.objects.get(title="Мероприятие").actions.all()
        page = request.GET.get('page')
        if page is None:
            page = '1'
        paginator = Paginator(all_actions, 10)
        try:
            posts_data = paginator.page(int(page))
        except PageNotAnInteger:
            posts_data = paginator.page(1)
        except EmptyPage:
            posts_data = paginator.page(paginator.num_pages)
        except Exception as _ex:
            context = {}
            print(f'{_ex}')
        context['all_actions'] = posts_data
    except Exception as e:
        print(e)
    return render(request, template, context)


def action_view(request, action_id):
    '''
    Generate page with action post
    :param request:
    :param action_id:
    :return:
    '''
    template = 'news/action.html'
    action = NewsPost.objects.get(id=action_id)
    return render(request, template, {'action': action})


# Helpers
# move data from FORM to COMMENT MODEL
def _move_data_from_form_to_comment_model(form, comment, post):
    """Функция, которая переносит дфнные из заполненной на сайте формы в экземпляр класса Comment"""
    comment.post = post
    comment.author = form.data['author']
    comment.text = form.data['text']
    comment.author_email = form.data['author_email']
    comment.site = form.data['site']
    return comment


# normalize the link from Youtube Video
def _set_youtube_link_normal(image_link: str, controls=True):
    normal_prefix = 'https://www.youtube.com/embed/'
    link_separated = image_link.split('?')
    if image_link[0: len(normal_prefix)] == normal_prefix:
        if len(link_separated) == 1:
            if controls:
                if link_separated[0][-1] == '/':
                    return f'{link_separated[:-2]}?controls=1'
                else:
                    return f'{link_separated}?controls=1'
            else:
                return link_separated[0]
        return image_link
    video_id = link_separated[0].split('/')[-1]
    if link_separated[-1] == 'controls=1' or controls:
        return f'{normal_prefix}/{video_id}?controls=1'
    return f'{normal_prefix}/{video_id}'
