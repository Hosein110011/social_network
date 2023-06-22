# from django.shortcuts import render
# from rest_framework.viewsets import mixins



# class PostView(viewsets.GenericViewSet,
#                mixins.CreateModelMixin,
#                mixins.ListModelMixin,
#                mixins.RetrieveModelMixin):
#     pass
from rest_framework.decorators import APIView, api_view
from .models import Post
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PostView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def post(self, request):
        print(request.auth)
        print(request.user)
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    
class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False
        
    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status = status.HTTP_404_NOT_FOUND)
        # comments = Comment.objects.filter(post post , is_approved = True)
        comments = post.comments.filter(is_approved = True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk = post_pk)
        except Post.DoesNotExist:
            return False
    
    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        likes = post.likes.filter(is_liked = True).count()
        return Response({'like': likes})
        
    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = LikeSerializer(post = post, user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)





