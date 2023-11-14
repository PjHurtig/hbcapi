from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import GearList
from .serializers import GearListSerializer


class GearListCreateView(generics.ListCreateAPIView):
    """
    Lists gearlists or create a gearlist if logged in
    The perform_create method associates the gearlist with the logged in user.
    Can be filtered by profile and searched
    """
    serializer_class = GearListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GearList.objects.all().order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'description',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GearListDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a gearlist and edit or delete it if you own it.
    """
    serializer_class = GearListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = GearList.objects.all().order_by('-created_at')
