from django.shortcuts import render
from rest_framework import (
    generics,
    viewsets,
    permissions
)
from .models import MenuTable, BookingTable
from restaurant.serializers import (
    MenuSerializer,
    BookingSerializer,
    UserSerializer
)

from django.contrib.auth.models import User

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
