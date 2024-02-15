from rest_framework import serializers
from.models import Author, Book


# HyperlinkSerializer:

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')
    class Meta:
        model=Author
        fields='__all__'
