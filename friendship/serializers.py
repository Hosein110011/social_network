from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

    # def to_representation(self, instance):
    #     return super().to_representation(instance)

    def get_avatar(self, instance):
        if hasattr(instance, 'profile') and instance.profile.avatar:
            return instance.profile.avatar.url
        return ''