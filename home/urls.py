
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home,name='home'),
    path('hire', views.hire,name='hire'),
    path('update-res', views.update_resume,name='update-res'),
    path('update-employe', views.ProfileView.as_view(),name='profile'),
    path('details', views.details,name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    path('create-job/', views.create_job, name='create-job'),
    path('myjobs', views.myjobs, name='myjobs'),
    path('updateJobs/<int:pk>', views.updateJobs.as_view(), name='updateJobs'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='cat'),
    path('job-details/<int:pk>/', views.job_details, name='job-details'),
    path('manage-jobs', views.manage_jobs, name='manage-jobs'),
    path('apjobs/', views.show_apjobs, name='showapjobs'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
