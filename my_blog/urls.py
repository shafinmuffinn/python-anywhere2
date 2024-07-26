from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("posts", views.AllPostsView.as_view(), name='post-page'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name='post-detail-page'),              #posts/my-first-post   (slug format -  no special characters)
    path("read-later", views.ReadLaterView.as_view(), name='read-later')
]


