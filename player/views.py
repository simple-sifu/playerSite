# from django.http import HttpResponse


# def list(request):

#      Player.objects.all()
#     return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, player_id):
#     return HttpResponse("You're looking at question %s." % player_id)

from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets

from .models import Player
from .serializers import PlayerSerializer

from .pagination import LimitOffsetPagination
from rest_framework import status


class PlayerViewSet(viewsets.ModelViewSet):

    serializer_class = PlayerSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        
        queryset = Player.objects.all()        
        return queryset


    # override function to determine if there are too many database hits.
    # Currently using prefetch_related method we are able to keep it under 3 or 4 query 
    # hits per method call. This is usually an issue with nested serializer
    # so need to confirm that it is working properly.
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        from django.db import connection
        print('*************** # of Queries: {}   *****************'.format(len(connection.queries)))

        return response

