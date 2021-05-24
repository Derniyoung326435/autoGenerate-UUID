from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DetailSerializer
from .models import *

# Create your views here.


@api_view(['GET'])
def data_all(request):
    raw = []
    if request.method == 'GET':
        Detail.objects.create()

    user = Detail.objects.all().order_by('-time_stamp')

    userSerializer = DetailSerializer(user, many=True)
    users = userSerializer.data
    for i in users:
        data = {
            i['time_stamp']: i['user_id']
        }
        raw.append(data)

    print(raw)

    return Response(raw)
