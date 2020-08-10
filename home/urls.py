from django.urls import path, include
from .import views
app_name = 'home'
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name = 'contact'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('cart/', views.cart, name = 'cart'),
    path('products/<int:id>', views.products, name = 'products'),
    path('probyCat/<int:id>/', views.probyCat, name = 'probyCat'),
    path('catagory/', views.catagory, name = 'catagory'),
    path('insertCart/<int:id>', views.insertCart, name = 'insertCart'),
    path('deleteCart/<int:id>', views.deleteCart, name = 'deleteCart'),
    path('updateCart/', views.updateCart, name = 'updateCart'),
]