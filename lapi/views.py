from django.shortcuts import render
from rest_framework import viewsets
from .models import movie
from .serializers import movieSerializer
from rest_framework import  permissions
from rest_framework import generics
#from rest_framework.generics import ListAPIView
from rest_framework.response import Response 

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters  import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class movieAPIViewPagination(LimitOffsetPagination):    #to add pagination creating the pagination class
	default_limit = 10
	max_limit = 100



class movieView(viewsets.ModelViewSet):
	queryset = movie.objects.all()
	serializer_class = movieSerializer
	pagination_class 		= movieAPIViewPagination
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends 		= [SearchFilter , OrderingFilter,DjangoFilterBackend]
	search_fields			= ['title']