from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, CommentCreateView, RegisterView
from .auth_views import login  

router = DefaultRouter()
router.register('blogs', BlogViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login, name='login'),  
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
]
