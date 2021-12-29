from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import NewsPost, ImagePost, Comment, Tag, ActionType
from .forms import CommentForm


def all_news_data(request):
    template = loader.get_template('news/news.html')
    all_news = NewsPost.objects.order_by('-pubdate')
    context = {'data': []}
    for post in all_news:
        context['data'].append([post, len(Comment.objects.filter(post=post))])
    return HttpResponse(template.render(context, request))


def post_data(request, post_id):
    print('hello')
    template = 'news/post.html'
    data_from_post = NewsPost.objects.get(id=post_id)
    images = ImagePost.objects.filter(product=data_from_post)
    last_five_pubs = [(i.title, i.id) for i in NewsPost.objects.all()[:5]]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            try:
                comment = _move_data_from_form_to_comment_model(form, comment, data_from_post)
                comment.save()
                return redirect('all_news')
            except ChildProcessError as ex:
                print('ERROR: incorrect data', ex, sep='\n')
    form = CommentForm()
    comments = Comment.objects.filter(post=data_from_post)[:5]
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
        'comments': comments,
        'form': form,
    }
    return render(request, template, context)


def gallery_of_different_images(request):
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


def actions(request):
    template = 'news/actions.html'
    all_actions = ActionType.objects.get(title="Мероприятие").actions.all()
    return render(request, template, {'all_actions': all_actions})


def action_view(request, action_id):
    template = 'news/action.html'
    action = NewsPost.objects.get(id=action_id)

    return render(request, template, {'action': action})


# Helpers
# move data from FORM to COMMENT MODEL
def _move_data_from_form_to_comment_model(form, comment, post):
    """Функция, которая переносит дфнные из щаполненной на сайте формы в экземпляр класса Comment()"""
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
