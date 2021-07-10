from django.urls import path
from Products import views

urlpatterns = [
    path('',views.ProductsListView.as_view(),name='product_list'),
    path('products/new/',views.ProductsCreateView.as_view(),name='product_new'),
    path('products/<int:pk>/',views.ProductsDetailView.as_view(),name='product_detail'),
    path('products/<int:pk>/remove/',views.ProductsDeleteView.as_view(),name='product_delete'),
    path('products/profile/',views.ProductsListView.as_view(),name='product_list'),
    path('products/<int:pk>/edit/',views.ProductsUpdateView.as_view(),name='product_edit'),
]