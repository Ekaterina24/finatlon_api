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


class ArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Archive
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'
