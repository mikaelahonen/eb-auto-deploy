#Import django libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, F
from django.views import generic
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from gym.serializers import *

#Python libraries
import datetime as dt
import json

# Import models and forms
from .models import *

#Viewsets http://www.django-rest-framework.org/api-guide/viewsets/

class WorkoutViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Workout.objects.all().order_by('-id')
	serializer_class = WorkoutSerializer
	
	def list(self, request):
		#All objects
		queryset = Workout.objects.all()
		#Filter by current user
		queryset = queryset.filter(user=self.request.user)
		#Sort
		queryset = queryset.order_by('-id')
		
		#many=True: get or post multiple items at once
		serializer = WorkoutSerializer(queryset, many=True)		
		return Response(serializer.data)
	
	#def retrieve(self, request, pk=None):

	
class SetViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	
	serializer_class = SetSerializer
	queryset = Set.objects.all().order_by('workout_order')
	
	#Override the list method
	def list(self, request):
	
		#Get workout parameter from URL
		workout = self.request.query_params.get('workout', None)
		
		#All objects
		queryset = Set.objects.all()
		#Filter by workout parameter
		if(workout is not None):
			queryset = queryset.filter(workout__id=workout)
		#Filter by current user
		queryset = queryset.filter(user=self.request.user)
		#Sort
		queryset = queryset.order_by('-done', 'workout_order')
	
		#many=True: get or post multiple items at once
		serializer = SetSerializer(queryset, many=True)		
		return Response(serializer.data)
	
class ExcerciseViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Excercise.objects.all().order_by('-id')
	serializer_class = ExcerciseSerializer
	
class MuscleGroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = MuscleGroup.objects.all().order_by('-id')
	serializer_class = MuscleGroupSerializer