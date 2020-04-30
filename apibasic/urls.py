
from django.urls import path


urlpatterns = [
    path('article/',views.article_list,name='article_list'),
]
