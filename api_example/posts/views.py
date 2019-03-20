from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    CreateAPIView
    )
from .models import Posts
from .serializer import (
    PostListSerializer, PostDetailSerializer, PostCreateSerializer
)

# Create your views here.
class PostCreateAPIView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

class PostListAPIView(ListAPIView):
    """This is  view to get all posts from the database model"""
    queryset = Posts.objects.all()
    serializer_class = PostListSerializer


class PostUpdateAPIView(UpdateAPIView):
    """This is  view to update a post"""
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

class PostDeleteAPIView(DestroyAPIView):
    """This is  view to delete a post from the database"""
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'







