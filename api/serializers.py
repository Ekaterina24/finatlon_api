from rest_framework import serializers
from .models import *


class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = '__all__'
