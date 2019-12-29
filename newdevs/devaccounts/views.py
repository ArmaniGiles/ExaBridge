from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import DevUser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .groups import ExaGroup
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group



class Main(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = DevUser.objects.all()
    template_name = 'devaccounts/main.html'

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
    template_name = 'devaccounts/register.html'

    def get(self, request):
        someDict = {'Fox':'One'}
        return Response(someDict)

    def create(self, request):
        job_candidate = Group.objects.get_or_create(name='job_candidate')
        employer = Group.objects.get_or_create(name='employer')


        # employer = Group.objects.create(name='employer')

        # new_group, created = Group.objects.get_or_create(name='job_candidate')

        # if 'company_name' in request.data:
        #     Employee.objects.create(
        #                         first_name=request.data['firstname'],
        #                         last_name=request.data['lastname'],
        #                         company_name=request.data['company_name'],
        #                         email=request.data['email'], 
        #                         password=request.data['password'])
        #     # g1.user_set.add(user1, user2, user5, user7)
        #     ExaGroup.employerGroup.user_set.add(Employee)
        # else:
        #     DevUser.objects.create(
        #                             first_name=request.data['firstname'],
        #                             last_name=request.data['lastname'],
        #                             email=request.data['email'], 
        #                             password=request.data['password'])
        #     ExaGroup.jobCandidateGroup.user_set.add(DevUser)
        



        someDict = {'Fox':'One'}
        return HttpResponseRedirect('/')
