from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    RegisterView,
    CategoryViewSet,
    ProfileViewSet
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]