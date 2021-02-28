from rest_framework import serializers
from comments.serializers import CommentSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    topic = serializers.ReadOnlyField(source='topic.url_name')
    comments = CommentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'created_at', 'updated_at', 'title',
                 'content', 'topic', 'author', 'comments']