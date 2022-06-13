from rest_framework import serializers
from .models import *


class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = '__all__'


class TapeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tape
        fields = '__all__'
