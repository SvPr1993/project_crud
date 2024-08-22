from django.shortcuts import render
from rest_framework.views import APIView
from app_crud.models import Person
from app_api.serializers import PersonSerializer
from rest_framework.response import Response


class NamelistApi(APIView):
    def get(self, request):
        name_list = Person.objects.all()
        serializer = PersonSerializer(name_list, many=True)
        return Response(serializer.data)
    def post(self):
        pass


