from django.urls import path
from .import HODViews
from .import pharmacistViews,DoctorViews,views,patient_view,clerkViews
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',HODViews.adminDashboard,name='admin_dashboard'),
    path('admin_user/patient_form/',HODViews.createPatient,name='patient_form'),
    path('admin_user/all_patients/',HODViews.allPatients,name='all_patients'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'), 
    # path('get_user_details/', views.get_user_details, name="get_user_details"),

    path('admin_user/add_pharmacist/',HODViews.createPharmacist,name='add_pharmacist'),
    path('admin_user/manage_pharmacist/',HODViews.managePharmacist,name='manage_pharmacist'),
    path('admin_user/add_doctor/',HODViews.createDoctor,name='add_doctor'),
    path('admin_user/manage_doctor/',HODViews.manageDoctor,name='manage_doctor'),
    path('admin_user/add_pharmacyClerk/',HODViews.createPharmacyClerk,name='add_pharmacyClerk'),
    path('admin_user/admin_user/manage_pharmacyClerk/',HODViews.managePharmacyClerk,name='manage_pharmacyClerk'),
    path('admin_user/add_stock/',HODViews.addStock,name='add_stock'),
    path('admin_user/add_category/',HODViews.addCategory,name='add_category'),
    path('admin_user/manage_stock/',HODViews.manageStock,name='manage_stock'),    
    path('admin_user/prescribe_drug/',HODViews.addPrescription,name='prescribe'),
    path('admin_user/edit_patient/<patient_id>/',HODViews.editPatient,name='edit_patient'),
    # path('add_patient_save/',HODViews.editPatientSave,name='edit_patient_save'),

    path('admin_user/delete_patient/<str:pk>/',HODViews.confirmDelete,name='delete_patient'),
    path('admin_user/patient_personalRecords/<pk>/',HODViews.patient_personalRecords,name='patient_record'),
    path('admin_user/delete_prescription/<str:pk>/',HODViews.deletePrescription,name='delete_prescription'),
    path('admin_user/doctor_profile/',DoctorViews.doctorProfile,name='doctor_profile'),
    path('admin_user/hod_profile/',HODViews.hodProfile,name='hod_profile'),
    path('admin_user/delete_doctor/<str:pk>/',HODViews.deleteDoctor,name='delete_doctor'),
    path('admin_user/delete_pharmacist/<str:pk>/',HODViews.deletePharmacist,name='delete_pharmacist'),
    path('admin_user/delete_receptionist/<str:pk>/',HODViews.deletePharmacyClerk,name='delete_clerk'),
    path('admin_user/hod_profile/editAdmin_profile/',HODViews.editAdmin,name='edit-admin'),
    path('admin_user/delete_drug/<str:pk>/',HODViews.deleteDrug,name='delete_drug'),


    path('admin_user/edit_pharmacist/<staff_id>/', HODViews.editPharmacist, name="edit_pharmacist"),
    path('admin_user/edit_doctor/<doctor_id>/', HODViews.editDoctor, name="edit_doctor"),
    path('admin_user/edit_receptionist/<clerk_id>/', HODViews.editPharmacyClerk, name="edit_clerk"),
    path('admin_user/edit_drug/<pk>/', HODViews.editStock, name="edit_drug"),
    path('admin_user/receive_drug/<pk>/', HODViews.receiveDrug, name="receive_drug"),
    path('admin_user/reorder_level/<str:pk>/', HODViews.reorder_level, name="reorder_level"),
    path('admin_user/drug_details/<str:pk>/', HODViews.drugDetails, name="drug_detail"),
    path('patient_feedback_message/', pharmacistViews.patient_feedback_message, name="patient_feedback_message"),
    path('patient_feedback_message_reply/', pharmacistViews.patient_feedback_message_reply, name="patient_feedback_message_reply"),
    path('admin_user/delete_patient_feedback/<str:pk>/', pharmacistViews.deletefeedback, name="delete_fed"),

        path('delete_details/<str:pk>/', pharmacistViews.deleteDispense4, name="del_disp"),



    #Pharmacist
    path('pharmacist_home/',pharmacistViews.pharmacistHome,name='pharmacist_home'),
    path('pharmacist_manage_patients/',pharmacistViews.managePatientsPharmacist,name='manage_patient_pharmacist'),
    path('manage_disp/<pk>/',pharmacistViews.manageDispense,name='pharmacist_disp'),
#    path('manage_dispe/<str:pk>/',pharmacistViews.dispenseDrug,name='pharm_disp'),
    # path('manage_stock_form/<str:pk>/',pharmacistViews.dispense,name='pharm_disp2'),
    path('staff_profile/',pharmacistViews.userProfile,name='pharmacist_profile'),

    path('manage_stock2/',pharmacistViews.manageStock,name='manage_stock2'),    
    path('manage_prescrip/',pharmacistViews.managePrescription,name='pharmacist_prescription'),
    path('pharmacist_user/drug_details/<str:pk>/', pharmacistViews.drugDetails, name="drug_detail2"),



    #Doctor
    path('doctor_home/',DoctorViews.doctorHome,name='doctor_home'),
    path('manage_patients/',DoctorViews.managePatients,name='manage_patient_doctor'),
    path('doctor_prescribe_drug/<str:pk>/',DoctorViews.addPrescription,name='doctor_prescribe2'),
    path('patient_personalDetails/<str:pk>/',DoctorViews.patient_personalDetails,name='patient_record_doctor'),
    path('manage_prescription_doctor/',DoctorViews.managePrescription,name='manage_precrip_doctor'),
    path('doctor_prescribe_delete/<str:pk>/',DoctorViews.deletePrescription,name='doctor_prescrip_delete'),
    path('doctor_prescribe_edit/<str:pk>/',DoctorViews.editPrescription,name='doctor_prescrip_edit'),

    #Patients
    path('patient_profile/',patient_view.patientProfile,name='patient_profile'),
    path('patient_home/',patient_view.patientHome,name='patient_home'),
    path('patient_feedback/',patient_view.patient_feedback,name='patient_feedback'),
    path('staff_feedback_save/', patient_view.patient_feedback_save, name="patient_feedback_save"),
    path('taken_home/',patient_view.patient_dispense3,name='taken_home'),
    path('delete_patient_feedback2/<str:pk>/',patient_view.Patientdeletefeedback, name="delete_fed2"),
    path('delete_dispen/',patient_view.myPrescriptionDelete,name='taken_delete'),

    #Receptionist
    path('receptionist_profile/',clerkViews.receptionistProfile,name='clerk_profile'),
    path('receptionist_home/',clerkViews.clerkHome,name='clerk_home'),
    path('receptionist/patient_form/',clerkViews.createPatient,name='patient_form2'),
    path('receptionist/all_patients/',clerkViews.allPatients,name='all_patients2'),
    path('receptionist/edit_patient/<patient_id>/',clerkViews.editPatient,name='edit_patient_clerk'),
    path('receptionist/patient_personalRecords/<str:pk>/',clerkViews.patient_personalRecords,name='patient_record_clerk'),
    path('receptionist/delete_patient/<str:pk>/',clerkViews.confirmDelete,name='delete_patient_clerk'),
    # path('receptionist/dispense_drug/<str:pk>/',pharmacistViews.dispenseDrug,name='dispense_drug'),


  
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView
    .as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView
    .as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),



    

   path('reset_password_complete/',auth_views.PasswordResetCompleteView
    .as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
]
