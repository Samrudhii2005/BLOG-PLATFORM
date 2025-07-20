from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Blog API</h1>")

# Create your views here.
from rest_framework import viewsets
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  # Require login
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # ✅ Automatically set author

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add this if not already

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny] 
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
 