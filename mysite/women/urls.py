from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', aboutSite, name='about'),
    path('addpage/', addPage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', showPost, name='post'),
    path('category/<int:cat_id>/', show_category, name = 'category'),
]
