from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .permissions import IsAdminUserOrReadOnly
from rest_framework.response import Response

from rest_framework.decorators import api_view

class NewViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class TapeViewSet(ModelViewSet):
    queryset = Tape.objects.all()
    serializer_class = TapeSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ArchiveViewSet(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class OptionViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


@api_view(['GET'])
def api(request):
    api_urls = {
        'users_create': '/auth/users/'
    }
    return Response(api_urls)



