from rest_framework import serializers
# from posts.serializer import PostSerializer
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    # posts = PostSerializer(read_only=True, many=True)
    
    class Meta:
        model = Topic
        fields = ['created_at', 'updated_at', 'title',
                  'name', 'description', 'url_name', 'author']
        # fields = ['created_at', 'updated_at', 'title',
        #           'name', 'description', 'url_name', 'author', 'posts']
