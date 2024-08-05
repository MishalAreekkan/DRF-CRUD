from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import PersonDetails,Team,Demo
from . serializers import PersonSerializer,TeamSerilalizer,DemoSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
    )
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication
    )
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
def show(request):
    data = {
        'name':'mishal',
        'place':'mlprm',
        'domain':'python'
    }
    return Response(data)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def detail(request):
    if request.method == 'GET':
        details = PersonDetails.objects.all()
        serializer  = PersonSerializer(details, many = True)
        print(serializer.data)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            print('sdfgsdgf')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = PersonDetails.objects.get(id=data['id'])
        serializer = PersonSerializer(obj,data = data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        obj = PersonDetails.objects.get(id = request.data['id'])
        serializer = PersonSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = PersonDetails.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'person deleted'})

class SuperPerson(APIView):
    def get(self,req):
        details = PersonDetails.objects.all()
        serializer  = PersonSerializer(details, many = True)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response('its a get method')
    
    def post(self,req):
        return Response('its a post method')
    
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = PersonDetails.objects.all()
    serializer_class  = PersonSerializer
    
    def list(self,request,*args, **kwargs):
        search = request.GET.get('search')
        queryset = self.queryset
        
        if search:
            queryset = queryset.filter(name__startswith = search)
        
        serializer = PersonSerializer(queryset,many = True)
        return Response({'data':serializer.data})
          
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerilalizer
    
class Teamsviewset(viewsets.ViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerilalizer
    def list(self,request,*args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset,many = True)
        return  Response(serializer.data)
# class team(viewsets.ModelViewSet):
#         queryset = Team.objects.all()
#         serializer_class  = TeamSerilalizer
    
    
# **********************generic n mixins********************** 

class DemoList(GenericAPIView,
            ListModelMixin,
            CreateModelMixin,
               ):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    print(queryset)
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,req,*args, **kwargs):
        return self.create(req,*args, **kwargs)
    
    
class DemolistRUD(GenericAPIView,
            UpdateModelMixin,
            DestroyModelMixin,
            RetrieveModelMixin
            ):
    
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer

    def delete(self,req,*args, **kwargs):
        return self.destroy(req,*args, **kwargs)
    
    def put(self,req,*args, **kwargs):
        return self.update(req,*args, **kwargs)
    
    def get(s,req,*args, **kwargs):
        return s.retrieve(req,*args, **kwargs)
    
        # *********************genericAPIView********************************
        
class DemoApi(CreateAPIView,ListAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    
class DemoAPIRUD(
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    ):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    
    
        # *******************Auth-BasicAuthentication*******************
        
class DemoAuthBasic(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]