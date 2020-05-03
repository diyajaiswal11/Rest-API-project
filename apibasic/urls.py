
from django.urls import path, include
from . import views
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    #path('article/',views.article_list,name='article_list'),
    path('article/',ArticleAPIView.as_view()),
    path('generic/article/<int:id>/',GenericAPIView.as_view()),
    #path('detail/<int:pk>/',views.article_detail,name='article_detail'),
    path('detail/<int:id>/',ArticleDetails.as_view()),
]
 