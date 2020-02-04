from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

#region Version 1

# from django.contrib.auth import get_user_model
# from rest_framework import viewsets

# from .models import Post
# from .permissions import IsAuthorOrReadOnly
# from .serializers import PostSerializer, UserSerializer


# class PostList(viewsets.ModelViewSet):
#     """ Please, I have a family """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(viewsets.ModelViewSet):
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#endregion Version 1
