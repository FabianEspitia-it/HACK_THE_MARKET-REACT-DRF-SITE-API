from django.urls import path
from products.api.views import ProductsAPiView, ProductsCategoryApiView, OneProductCategoryApiView

urlpatterns = [
    path('all_products/', ProductsAPiView.as_view(), name= 'products' ),
    path('products/<str:category>', ProductsCategoryApiView.as_view(), name='products_category'),
    path('product/<int:pk>', OneProductCategoryApiView.as_view(), name= 'one_product' )
 
]
