from django.urls import path
from .views import *



urlpatterns = [
    path('home/',home, name='home'),
    path('about/',about, name='about'),
    path('blog-post/<int:id>/',blog_post, name='blog-post'),
    path('blog/',blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('contact/',contact, name='contact'),
    path('product/',product, name='product'),

    path('product-details/<int:id>/<slug:slug>',product_details, name='product-details'),
    
    path('product/<int:id>/<slug:slug>',products, name='product'),
    path('terms/',terms, name='terms'),
    path('testimonials/',testimonials, name='testimonials'),
    #path('check',check,name='check'),
    path('search/',search,name='search'),
    path('addtoshopcart/<int:id>/',addtoshopcart,name='addtoshopcart'),
    path('shopcart/',shopcart,name='shopcart'),
    path('deletefromcart/<int:id>/',deletefromcart,name="deletefromcart"),
    path('login/',login,name="login"),
    path('login_form/',login_form,name="login_form"),
    path('logout_form/',logout_form,name="logout_form"),
    path('signup_form/',signup_form,name="signup_form"),
    
    path('orderproduct/',orderproduct,name="orderproduct"),
    path('userprofile/',userprofile,name="userprofile"),
    path("update/",user_update,name="update"),
    path('password/',user_password,name="password"),
    path('orders/',user_orders,name="user_orders"),
    path('orders_product/',user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>',user_orderdetail,name="user_orderdetail"),
    path('order_product_detail/<int:id>/<int:oid>',user_order_product_detail, name='user_order_product_detail'),
    path('comments/', user_comments, name='user_comments'),
    path('deletecomment/<int:id>', user_deletecomment, name='user_deletecomment'),
    
]
