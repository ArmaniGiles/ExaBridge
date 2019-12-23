from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DevUser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect


class Main(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = DevUser.objects.all()
    template_name = 'main.html'

    def get(self, request):
        someDict = {'Fox':'One'}
        # DevUser.objects.get(headline__icontains='Lennon')

        return Response(someDict)

    # def create(self, request):
    #     DevUser.objects.create(
    #                             first_name=request.data['firstname'],
    #                             last_name=request.data['lastname'],
    #                             email=request.data['email'], 
    #                             password=request.data['password'])
    #     someDict = {'Fox':'One'}
    #     return Response(someDict)




class Register(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = DevUser.objects.all()
    template_name = 'register.html'

    def get(self, request):
        someDict = {'Fox':'One'}
        return Response(someDict)

    def create(self, request):
        DevUser.objects.create(
                                first_name=request.data['firstname'],
                                last_name=request.data['lastname'],
                                email=request.data['email'], 
                                password=request.data['password'])
        someDict = {'Fox':'One'}
        return HttpResponseRedirect('/')
    


