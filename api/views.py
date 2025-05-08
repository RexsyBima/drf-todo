from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView, Request


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        return Response("not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostGet(APIView):
    def get(self, request: Request, format=None):
        title = request.query_params.get("title", "")
        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthenticatedBlogView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        # Example logic: return the username of the logged-in user
        if request.user.is_superuser:
            return Response(
                {"message": f"Hello, {request.user.username}!"},
            )
