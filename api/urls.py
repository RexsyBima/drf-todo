from django.urls import path
from . import views


urlpatterns = [
    path(
        "blogposts/",
        views.BlogPostListCreate.as_view(),
        name=views.BlogPostListCreate.__name__,
    ),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name=views.BlogPostRetrieveUpdateDestroy.__name__,
    ),
    path(
        "blogposts/get/",
        views.BlogPostGet.as_view(),
        name=views.BlogPostGet.__name__,
    ),
    path(
        "blogposts/authenticated-blog/",
        views.AuthenticatedBlogView.as_view(),
        name=views.AuthenticatedBlogView.__name__,
    ),
]
