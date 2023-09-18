from rest_framework.response import Response
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


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer

from .forms import BookingForm

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view()
@renderer_classes([TemplateHTMLRenderer])
def homepage(request):
    # items = MenuItem.objects.select_related('category').all()
    # serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data': "empty"}, template_name='index.html')


# ?########################


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# @permissions
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        pass
    context = {'form': form}
    return render(request, 'book.html', context)

# Add your code here to create new views


def menu(request):
    menu_data = MenuTable.objects.all()
    # sorted_data = sorted(menu_data, key=lambda x: x.title.lower())
    # main_data = {
    #     'menu': sorted_data
    # }
    return render(request, 'menu.html', {'menu': menu_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = MenuTable.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})
