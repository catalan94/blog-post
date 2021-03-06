from django.urls import path
from .views import(
    PostListView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    )

# pk=id 
urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
]
