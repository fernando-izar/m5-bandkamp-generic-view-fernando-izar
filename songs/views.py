from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
import ipdb


class SongView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs[self.lookup_url_kwarg])
        serializer.save(album=album)
