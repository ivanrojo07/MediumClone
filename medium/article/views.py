# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Article, Author
from .serializers import ArticleSerializer
# Create your views here.

# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         # Parametro many implica que serializara mas de un articulo
#         serializer = ArticleSerializer(articles,many=True)
#         return Response({"articles":serializer.data})


#     def post(self,request):
#         article = request.data.get('article')

#         # Crear un articulo a partis de los datos anteriores
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success":"Article '{}' created successfully".format(article_saved.title)},status=status.HTTP_201_CREATED)
#         return Response({"error":"Failed"},status=status.HTTP_400_BAD_REQUEST)

#     def put (self,request,pk):
#         saved_article = get_object_or_404(Article.objects.all(),pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article,data=data,partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success":"Article '{}' updated successfully".format(article_saved.title)})
#         return Response({"error":"Failed"},status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         # Obtenemos el objeto con esa pk

#         article = get_object_or_404(Article.objects.all(),pk=pk)
#         article.delete()
#         return Response({"message":"Article with id '{}' has been deleted.".format(pk)},status=status.HTTP_204_NO_CONTENT)

# class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self,serializer):
        author = get_object_or_404(Author,id=self.request.data.get("author_id"))
        return serializer.save(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer