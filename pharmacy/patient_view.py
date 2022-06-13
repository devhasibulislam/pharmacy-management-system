from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .decorators import *
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required
def patientHome(request):
    patient_obj = Patients.objects.get(admin=request.user.id)

    patient_dispen=patient_obj.dispense_set.all().count()
    context={
          "total_disp":patient_dispen
    }
    return render(request,'patient_templates/patient_home.html',context)

@login_required
def patientProfile(request):
    customuser = CustomUser.objects.get(id=request.user.id)
    patien = Patients.objects.get(admin=customuser.id)
   
    form=PatientPicForm1()
    if request.method == "POST":
       

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

      
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.email=email
        
        customuser.save()
        patien = Patients.objects.get(admin=customuser.id)
        form=PatientPicForm1(request.POST,request.FILES,instance=patien)

        patien.address = address
        if form.is_valid():
            form.save()
        patien.save()
       
        messages.success(request, "Profile Updated Successfully")
        return redirect('patient_profile')

    context={
        "patien":patien,
        "form":form
    }
      

    return render(request,'patient_templates/patient_profile.html',context)


def myPrescription(request):
    precrip=Prescription.objects.all()

    patient = Patients.objects.all()


    context={
        "prescrips":precrip,
        "patient":patient
    }
    return render(request,'doctor_templates/myprescription.html' ,context)

def myPrescriptionDelete(request):
    patient_obj = Patients.objects.get(admin=request.user.id)
    precrip=patient_obj.prescription_set.all()
    if request.method == "POST":
        precrip.delete()




    context={
        "prescrips":precrip,
    }
    return render(request,'patient_templates/sure_delete.html',context)

def patient_feedback(request):
    patient_fed = Patients.objects.get(admin=request.user.id)
    feedback = PatientFeedback.objects.filter(patient_id=patient_fed)
    context = {
        "feedback":feedback
    }
    return render(request, "patient_templates/patient_feedback.html", context)


def patient_feedback_save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback_message')
        staff_obj = Patients.objects.get(admin=request.user.id)

     
        add_feedback =PatientFeedback(patient_id=staff_obj, feedback=feedback, feedback_reply="")
        add_feedback.save()
        messages.success(request, "Feedback Sent.")
        return redirect('patient_feedback')

def Patientdeletefeedback(request,pk):
    try:
        fed=PatientFeedback.objects.get(id=pk)
        if request.method == 'POST':
            fed.delete()
            messages.success(request, "Feedback  deleted successfully")
            return redirect('patient_feedback')

    except:
        messages.error(request, "Feedback Error, Please Check again")
        return redirect('patient_feedback')


   
    return render(request,'patient_templates/sure_delete.html')


def patient_dispense3(request):
    patient_obj = Patients.objects.get(admin=request.user.id)

    patient_dispen=patient_obj.dispense_set.all()

    context={
        "dispense":patient_dispen
    }
    return render(request, "patient_templates/patient_dispense.html", context)


