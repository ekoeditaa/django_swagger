# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, generics

from .models import Entity

# Create your views here.


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('model', 'text')


class Entity_list(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


@api_view(['POST'])
def hello_world(request):
    model = request.data.get('model', '')
    text = request.data.get('text', '')
    res = model + text
    return Response({"message": res})
