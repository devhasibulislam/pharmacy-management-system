from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .decorators import *
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required
def clerkHome(request):
    patients=Patients.objects.all().count()

    context={
       "patients_total":patients
    }
    return render(request,'clerk_templates/clerk_home.html',context)



@login_required
def receptionistProfile(request):
    customuser = CustomUser.objects.get(id=request.user.id)
    staff = PharmacyClerk.objects.get(admin=customuser.id)

    form=ClerkForm()
    if request.method == "POST":
       

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number=request.POST.get('phone_number')

      
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.save()

        staff = PharmacyClerk.objects.get(admin=customuser.id)
        form=ClerkForm(request.POST,request.FILES,instance=staff)

        staff.address = address
        staff.phone_number=phone_number
        staff.save()
        if form.is_valid():
            form.save()
        

    context={
        "form":form,
        "staff":staff,
        'user':customuser
    }
      

    return render(request,'clerk_templates/clerk_profile.html',context)


    
@login_required
def createPatient(request):
    form=PatientForm(request.POST, request.FILES)
    try:
        if request.method == "POST":
            if form.is_valid():
            
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                address = form.cleaned_data['address']
                phone_number = form.cleaned_data['phone_number']
                dob = form.cleaned_data['dob']
                gender = form.cleaned_data['gender']
            
        
            user = CustomUser.objects.create_user(username=username, email=email,password=password, first_name=first_name, last_name=last_name,user_type=5)
            user.patients.address = address
            user.patients.phone_number = phone_number
            user.patients.dob=dob
            user.patients.gender=gender
            user.save()

            messages.success(request, "Patient Added Successfully!")
            return redirect('patient_form2')
            
    except:
        
        messages.error(request,'Patient Not Saved')
        return redirect('patient_form2')
    context={
        "form":form
    }
       
    return render(request,'clerk_templates/add_patient.html',context)


@login_required
def allPatients(request):
    patients=Patients.objects.all()

    context={
        "patients":patients,

    }
    return render(request,'clerk_templates/manage_patient.html',context)



@login_required
def editPatient(request,patient_id):
    request.session['patient_id'] = patient_id

    patient = Patients.objects.get(admin=patient_id)

    form = EditPatientForm()
    

    form.fields['email'].initial = patient.admin.email
    form.fields['username'].initial = patient.admin.username
    form.fields['first_name'].initial = patient.admin.first_name
    form.fields['last_name'].initial = patient.admin.last_name
    form.fields['address'].initial = patient.address
    form.fields['gender'].initial = patient.gender
    form.fields['phone_number'].initial = patient.phone_number
    form.fields['dob'].initial = patient.dob
    try:
        if request.method == "POST":
            if patient_id == None:
                return redirect('all_patients')
            form = EditPatientForm( request.POST)

            if form.is_valid():
                
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                address = form.cleaned_data['address']
                gender = form.cleaned_data['gender']
                dob=form.cleaned_data['dob']
                phone_number = form.cleaned_data['phone_number']


                try:
                    user = CustomUser.objects.get(id=patient_id)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.username = username
                    user.save()

                    patients_edit = Patients.objects.get(admin=patient_id)
                    patients_edit.address = address
                    patients_edit.gender = gender
                    patients_edit.dob=dob
                    patients_edit.phone_number=phone_number
                    
                    patients_edit.save()
                    messages.success(request, "Patient Updated Successfully!")
                    return redirect('all_patients2')
                except:
                    messages.error(request, "Failed to Update Patient.")
                    return redirect('all_patients2')
    except:
         messages.error(request, "Invalid Error!")
         return redirect('all_patients')


    context = {
        "id": patient_id,
        "form": form
    }
    return render(request, "clerk_templates/edit_patient.html", context)


       

@login_required
def patient_personalRecords(request,pk):
    patient=Patients.objects.get(id=pk)
    prescrip=patient.prescription_set.all()

    context={
        "patient":patient,
        "prescription":prescrip

    }
    return render(request,'clerk_templates/patient_personalRecords.html',context)


@login_required
def confirmDelete(request,pk):
    try:
        patient=Patients.objects.get(id=pk)
        if request.method == 'POST':
            patient.delete()
            messages.success(request, "Staff  deleted")

            return redirect('all_patients2')
    except:
        messages.error(request, "Patient Cannot be deleted  deleted , Patient is still on medication or an error occured")
        return redirect('all_patients2')

    context={
        "patient":patient,

    }
    
    return render(request,'clerk_templates/delete_patient.html',context)