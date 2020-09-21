from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Novel, Chapter


class ChapterSerializer(serializers.ModelSerializer):
    """ Chapter serializer for Chapter objects """
    class Meta:
        model = Chapter
        exclude = ('novel',)
        read_only_fields = ('id',)


class NovelSerializer(serializers.ModelSerializer):
    """ Novel serializer for Novel objects """
    author = UserSerializer(read_only=True)
    chapters = ChapterSerializer(read_only=True, many=True)

    class Meta:
        model = Novel
        fields = "__all__"
        read_only_fields = ('author', 'id', 'created', 'updated')
    
    def create(self, validated_data):
        request = self.context.get('request')
        novel = Novel.objects.create(**validated_data, author=request.user)
        return novel