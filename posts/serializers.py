from rest_framework import serializers

from .models import Post , Comment


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