from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import VersionDetailView
from .views import product_create, product_update

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('list/', views.product_list, name='product_list'),
    path('product/version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/update/', product_update, name='product_update'),
]
