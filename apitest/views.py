# coding=utf-8
from django.shortcuts import render
import json
from django.core  import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request,'machine/index.html')
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apitest.models import profit
from apitest.serializer import profitSerializer


@api_view(['GET', 'POST'])
def profit_list(request,code):
    """
    显示profit所有数据,后者创建一个新的snippet
    """
    # try:
    #     profits = profit.objects.filter(stk_code=request.data)
    # except profit.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        profits = profit.objects.filter(stk_code=request.data)
        serializer = profitSerializer(profits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = profitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
