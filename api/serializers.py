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


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
