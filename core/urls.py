
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from api.views import *

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()

router.register(r'news', NewViewSet)
router.register(r'tapes', TapeViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('auth/', api, name='api_auth'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
