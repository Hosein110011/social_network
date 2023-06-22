from rest_framework import serializers

from .models import Post , Comment, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'caption', 'is_active', 'is_public')
        extra_kwargs = {
            'user':{'read_only':True}
            }
        
class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = ('post', 'user', 'text')
    extra_kwargs = {
        'post': {'read_only': True},
        'user': {'read_only': True}
    }

class LikeSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Like
        fields = ('post', 'user', 'is_liked')
        extra_kwargs = {
            # 'post':{'read_only': True},
            'user':{'read_only': True},
            'is_liked':{'required': False}
        }



