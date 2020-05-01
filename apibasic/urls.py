
from django.urls import path
from . import views
from .views import ArticleAPIView, ArticleDetails
urlpatterns = [
    #path('article/',views.article_list,name='article_list'),
    path('article/',ArticleAPIView.as_view()),
    #path('detail/<int:pk>/',views.article_detail,name='article_detail')
    path('detail/<int:id>/',ArticleDetails.as_view()),
]
 