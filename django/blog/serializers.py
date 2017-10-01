from rest_framework import serializers
import markdown2

from . import models


class PostSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'title',
            'summary',
            'html_text',
            'published_at',
            'tags',
        )
        model = models.Post

    # return post's text as HTML!
    def get_html_text(self, post):
        return markdown2.markdown(post.text)