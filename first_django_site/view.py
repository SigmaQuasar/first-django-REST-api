from django.http import JsonResponse
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view()
def get_all_users(request):
    if request.method == 'GET':
        user = User.objects.all() #get all users
        serializer = UserSerializer(user, many=True) #serialize all the users
        return JsonResponse(serializer.data, safe= False) #return json
    else: 
        return Response({"message": "Something went wrong 🙁" })
  

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save() #saving data to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Something is wrong ☹️"})