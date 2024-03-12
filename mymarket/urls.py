from django.urls import path
from . import views
from .views import product_detail, BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, ContactView

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('posts/', BlogPostListView.as_view(), name='blogpost_list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('posts/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('posts/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('posts/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]
