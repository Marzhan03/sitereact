from django.shortcuts import render
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers


@api_view(["GET",])
def main(request):
    book = Book.objects.all()
    serializer = serializers.BookSerializer(book, many=True)
    print(serializer.data)
    return Response(serializer.data)
