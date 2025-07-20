from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author']  # Include author here
        read_only_fields = ['author']  # 👈 This tells DRF not to expect it in input


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user