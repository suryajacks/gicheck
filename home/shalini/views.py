from django.shortcuts import render , HttpResponse
from .models import Articles
from .serializers import ArticlesSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView

class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        articles = Articles.objects.all()
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])
# def articles_list(request):
#  if request.method == 'GET':
#        articles = Articles.objects.all()
#        serializer =ArticlesSerializers(articles, many=True)
#        return Response(serializer.data)


#  elif request.method == 'POST':
      
#        serializer = ArticlesSerializers(data=request)
#        if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticlesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articles = self.get_object(pk)
        serializer = ArticlesSerializers(articles)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        articles = self.get_object(pk)
        serializer = ArticlesSerializers(articles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
















# @api_view(['GET', 'PUT', 'DELETE'])
# def articles_details(request,pk):
   
#     try:
#         articles = Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticlesSerializers(articles)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
        
#         serializer = ArticlesSerializers(articles, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         articles.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
 
 

     
    


