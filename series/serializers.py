from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Serie


class SerieSerializer(serializers.ModelSerializer):
    category_description = serializers.CharField(source='category.description', read_only=True)

    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category', 'category_description')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'description')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
