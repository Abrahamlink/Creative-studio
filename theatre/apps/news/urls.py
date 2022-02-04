from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_news_data, name='all_news'),
    path('post_<int:post_id>/', views.post_data, name='one_post'),
    path('post_<int:post_id>$<int:comment_index>/', views.render_json_with_comments),
    path('images-gallery/', views.gallery_of_different_images, name='gallery'),
    path('images-gallery/<str:tag>/', views.render_json_with_images_paths, name='images_gallery'),
    path('actions/', views.actions, name='actions'),
    path('actions/N_<int:action_id>/', views.action_view, name='action_view'),
]
