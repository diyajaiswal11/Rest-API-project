from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def article_list(request):

    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True) 
        return Response(serializer.data)
        #return JsonResponse(serializer.data,  safe=False)   


    elif request.method=='POST':
        #data=JSONParser().parse(request)
        #serializer=ArticleSerializer(data=data)
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            #return JsonResponse(serializer.data,status=201) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        #return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk) 

    except Article.DoesNotExist:
        return HttpResponse(status=404) 

    if request.method=='GET':
        serializer=ArticleSerializer(article) 
        return JsonResponse(serializer.data)  

    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors,status=400)  


    elif request.method=='DELETE':
        article.delete()
        return HttpResponse(status=204)


    


    