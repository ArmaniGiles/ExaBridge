from django.contrib.auth.models import Group
from .models  import DevUser, EmployerAccount

class ExaGroup:

    def checkGroup(self, request):
        # new_group, created = Group.objects.get_or_create(name='job_candidate')
        if 'company_name' in request.data:
            job_candidate = Group.objects.get_or_create(name='Developer User Group')
            dev_user = DevUser.objects.create(
                                    first_name=request.data['firstname'],
                                    last_name=request.data['lastname'],
                                    email=request.data['email'], 
                                    password=request.data['password'])
            job_candidate.user_set.add(dev_user)
        else :
            employer = Group.objects.get_or_create(name='Employer User Group')
            employer_user = EmployerAccount.objects.create(
                                                    first_name=request.data['firstname'],
                                                    last_name=request.data['lastname'],
                                                    company_name=request.data['company_name'],
                                                    email=request.data['email'], 
                                                    password=request.data['password'])
            employer.user_set.add(employer_user)        



