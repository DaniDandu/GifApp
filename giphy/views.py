from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import Gif
from .search import search
from . import serializers

class GifViewset(viewsets.ModelViewSet):
    serializer_class = serializers.GifSerializer

    def get_queryset(self):
        gifs = Gif.objects.all()
        return gifs

    def get(self, request, format=None):
        gifs = self.get_queryset()
        serializer = serializers.GifSerializer(gifs, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.GifSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = '{name} {link}'.format(name=name, link=search(name))
            return Response({'Gif': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):
    #     gifs = self.get_queryset()
    #     gifs.delete()
    #     serializer = serializers.GifSerializer(gifs, many = True)
    #     return Response(serializer.data)