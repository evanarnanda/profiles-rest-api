from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')
"""base_name only if u don't have queryset or u want to overWrite it"""
router.register('profile', views.UserProfilesViewSet)
router.register('feed', views.UserProfilesFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
