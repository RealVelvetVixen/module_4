from django.urls import path
from .views import index, top_sellers, login, register, profile, advertisement, advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),

]