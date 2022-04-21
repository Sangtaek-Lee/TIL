from rest_framework import serializers
from .models import Artist, Music


# class CommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('article',)

# class ArticleDetailSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comment_set = CommentListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Article
#         fields = '__all__'


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistSerializer(serializers.ModelSerializer):
    music_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    music_count = music_set.count()

    class Meta:
        model = Artist
        fields = '__all__'