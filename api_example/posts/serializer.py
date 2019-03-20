from rest_framework import serializers
from .models import Posts

class PostListSerializer(serializers.ModelSerializer):
    """This is a model serializer for posts app """
    
    class Meta:
        """Class  Meta to map the serializer class with the model class"""
        model = Posts
        fields = (
            'id', 'title', 'body', 'user_id'
        )

#customise post detail view
class PostDetailSerializer(serializers.ModelSerializer):
    """This is a model serializer to customize get details of a specific post """

    class Meta:
        """Class Mets to map the serialize class with the model class"""
        model = Posts
        fields = (
            'title', 'body'
        )


class PostCreateSerializer(serializers.ModelSerializer):
    """This is a model serializer to create posts """


    class Meta:
        """Class Mets to map the serialize class with the model class"""
        model = Posts
        fields = (
            'id', 'title', 'body'
        )


