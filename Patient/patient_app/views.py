from django.shortcuts import render,redirect

from . models import patient
from . forms import PatientForm

# Create your views here.
def home(request):
    patients = patient.objects.all()
    search = request.GET.get('search')
    patient_filter = request.GET.get('filter')
    if search:
        patients = patient.filter(title__icontains=search)
    if patient_filter:
        jobs = jobs.filter(patient__id=patient_filter)
    
    obj=patient.objects.all()
    return render(request,'home.html',{'obj':obj,'patients':patients})

# def home(request):
#     jobs = Job.objects.all()
#     search = request.GET.get('search')
#     company_filter = request.GET.get('filter')
#     if search:
#         jobs = jobs.filter(title__icontains=search)
#     if company_filter:
#         jobs = jobs.filter(company__id=company_filter)
#     company = Company.objects.all()
#     return render(request,'home.html',{'jobs':jobs,'company':company})

def add_patent(request):
    
    if request.method=='POST':
       frm=PatientForm(request.POST)
       if frm.is_valid():
           frm.save()
           return redirect('home')
    frm=PatientForm()      
    return render(request,'add_patient.html',{'frm':frm})

def edit(request,id):
    obj=patient.objects.get(id=id)
    frm=PatientForm(instance=obj)  
    if request.method=='POST':
       frm=PatientForm(request.POST,instance=obj)
       if frm.is_valid():
           frm.save()
           return redirect('home')   
    return render(request,'add_patient.html',{'frm':frm})

def delete(request,id):
    obj=patient.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':obj})


