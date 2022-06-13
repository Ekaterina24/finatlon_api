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

# @api_view(['GET'])
# def api(request):
#         api_urls = {
#             'users': '/auth/users/',
#             'login': '/token/login/',
#         }
#
#        return Response(api_urls)



