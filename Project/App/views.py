from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
from .models import Profile
from .models import Country
from .models import Field
from .models import Task
from .models import City
from django.views import View
from django.db.models import Q

# def device(requt):
#     if request.method == 'GET':
#         queryset = Contact.objects.all()
        # if queryset:
        #     data = {"queryset": queryset}
        #     return render(request, 'device/device.html', data)
        # else:
        #     return render(request, 'device/device.html')
# class homePage(View):
#     def get(self, request):
#         data = Contact.objects.all()
#         # print(id)
#         single= data.get(pk=id)
#         context = {'data': data, 'single': single}
#         return render(request, 'index.html', context)
class homePage(View):
    def get(self, request,id=None):

        data = Contact.objects.all()
        if id!=None:
            single= data.get(pk=id)
        else:
            single=None
        return render(request, 'index.html',{'data': data, 'single': single} )
    

class Aboutus(View):
    def get(self, request):
        profiles = Profile.objects.all()
        countries = Country.objects.all()
        fields = Field.objects.all()
        return render(request, 'aboutus.html',{'profiles':profiles,'countries': countries, 'fields':fields}) 
    
    def post(self, request,id=None):
        
        selected_field: str = request.POST.get('selected-field','')
        selected_country: str= request.POST.get('selected-country','')
        typed_field = request.POST.get('job-company-name','')

        
        profiles = Profile.objects.all()
  
        if selected_country and selected_country.isdigit():
                selected_country = int(selected_country)

        if selected_field and selected_field.isdigit():
                selected_field = int(selected_field)
                
       

        if typed_field!= None:
            
            profiles = profiles.filter(Q(name__icontains=typed_field) | Q(field__name__icontains=typed_field))
        
        
        if selected_field!=0:
            profiles = profiles.filter(field__id=selected_field)

        if selected_country!=0:
            profiles = profiles.filter(city__country__id=selected_country)

        countries= Country.objects.all()
        fields = Field.objects.all()
        
        
       
        
        return render(request, 'aboutus.html',{'profiles':profiles,'countries': countries, 
                                               
        'fields':fields, 'selected_field':selected_field, 'selected_country':selected_country , 'typed_field':typed_field}) 
    
class delt(View):
    # def get(self, request,pk):
    #     profile= Profile.objects.get(id=pk)
    #     return render(request, 'aboutus.html',{'profile':profile})

    def get(self, request,pk):
        profile= Profile.objects.get(id=pk)
        profile.delete()
        return redirect('aboutus')
    
class list(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('-updated')
        return render(request, 'newapp.html', {'tasks': tasks})

    def post(self, request):
        # task=Task.objects.all()
        task = Task.objects.create(
        body = request.POST.get('body','')
        )
        task.save()
        return redirect('tasks')
    
class detail(View):
    def get(self, request,pk):
        task= Task.objects.get(id=pk)
        return render(request, 'tasklist.html',{'task':task})

    def post(self, request,pk):
        task= Task.objects.get(id=pk)
        task.body = request.POST.get('body')
        task.save()
        return redirect('tasks')

class Delete(View):
    def get(self, request,pk):
        task= Profile.objects.get(id=pk)
        return render(request, 'delete.html',{'task':task})

    def post(self, request,pk):
        task= Task.objects.get(id=pk)
        
        task.delete()
        return redirect('tasks')
    
    
class profile(View):
    def get(self, request,id=None):
        profiles = Profile.objects.all()
        # countries = Country.objects.all()
        fields = Field.objects.all()
        cities = City.objects.all()
        if id!=None:
            single= profiles.get(pk=id)
        else:
            single=None   

        
        return render(request, 'profile.html',{'profiles':profiles, 'fields':fields,'cities':cities,'single':single}) 
    
    def post(self, request,id=None):
       
        
        
        
        if id!=None:
            profile = Profile.objects.get(pk=id)
            profile.name = request.POST.get('name')
            profile.rating = request.POST.get('rating')
            profile.tag =  request.POST.get('tag')
            profile.charges = request.POST.get('charges')
            profile.city_id = request.POST.get('city')
            profile.field_id = request.POST.get('field')
            # profile.save()
        else:
            profile = Profile.objects.create(
                name = request.POST.get('name',''),
                rating = request.POST.get('rating'),
                tag =  request.POST.get('tag'),
                charges = request.POST.get('charges'),
                city_id = request.POST.get('city'),
                field_id = request.POST.get('field'),
            )

        profile.save()
        
        
        return redirect('aboutus')
    

