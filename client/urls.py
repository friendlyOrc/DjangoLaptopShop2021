
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>', views.prdDetail, name='prd-detail'),
    path('category/<int:pk>', views.prdList, name='prd-list'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('cart', views.cart, name='cart'),
    path('cart/add/<int:pk>', views.cart_add, name='cart_add'),
    path('cart/update/<int:pk>', views.cart_update, name='cart_update'),
    path('cart/remove/<int:pk>', views.cart_remove, name='cart_remove'),
    path('orders', views.orderList, name='order_list'),
    path('comment/<int:pk>', views.comment, name='comment'),
]
