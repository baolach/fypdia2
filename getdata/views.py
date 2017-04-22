from rest_framework.views import APIView  # returns data
from rest_framework.response import Response
from .serializers import ClientSerializer
from .serializers import LessonSerializer
from .serializers import LocationSerializer
from .serializers import ExpenseSerializer
from .serializers import UserSerializer


from django.shortcuts import render
from .models import GetClient
from .models import GetLesson
from .models import GetLocation
from .models import GetExpense
from .models import GetUser

from django.http import HttpResponse
import django.contrib.auth.models

from rest_framework import status




from django.shortcuts import render
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        User.objects.create_user('jon', 'lennon@thebeatles.com', 'johnpassword')
        return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')


# Create your views here.
def index(request):
    all_entries = GetClient.objects.all()
    return HttpResponse(all_entries.values())

def home(request):
    clientdata = GetClient.objects.order_by('client_name')
    #clientdata = GetLesson.objects.order_by('lesson_name')  # clientdata will be a list of all the clients


    return render(request, 'getdata/home.html', {'getclients': clientdata})


# this either lists all clients or creates a new one
class ClientList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        #clients = GetClient.objects.all().filter().order_by('-client_name') #.extra(order_by=['char_length(name)'])  # gets the clients to pass through the serializer
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        #Species.objects.all().extra(order_by=['char_length(name)'])  # PostgreSQl
        clients = GetClient.objects.all().extra(order_by=['client_name'])  # PostgreSQl


        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)  # the json data

    def post(self):
        return

# this either lists all clients or creates a new one
class LessonList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        # lessons = GetLesson.objects.all()  # gets the clients to pass through the serializer
        lessons = GetLesson.objects.all().extra(order_by=['lesson_date'])  # PostgreSQl

        serializer = LessonSerializer(lessons, many=True)  # how many objects to be serialized
        return Response(serializer.data)  # the json data
        # return HttpResponse(clients.values())

    def post(self):
        return

class LocationList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        locations = GetLocation.objects.all()  # gets the clients to pass through the serializer
        serializer = LocationSerializer(locations, many=True)  # how many objects to be serialized
        return Response(serializer.data)  # the json data
        # return HttpResponse(clients.values())

    def post(self):
        return

class UserList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        users = GetUser.objects.all()  # gets the clients to pass through the serializer
        serializer = UserSerializer(users, many=True)  # how many objects to be serialized
        return Response(serializer.data)  # the json data
        # return HttpResponse(clients.values())

    def post(self):
        return



class ExpenseList(APIView):
    # returns these as a view when called in urls.py
    def get(self, request):
        expenses = GetExpense.objects.all()  # gets the clients to pass through the serializer
        serializer = ExpenseSerializer(expenses, many=True)  # how many objects to be serialized
        return Response(serializer.data)  # the json data
        # return HttpResponse(clients.values())

    def post(self):
        return