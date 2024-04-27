from django.shortcuts import render , redirect
from. models import Resume, Employe, Jobs , ApplyJob
from django.views import View
from django.contrib import messages
from . forms import UpdateResumeForm , UpdateEmployeForm, CreateJobForm
from users.models import User
from django.db.models import Q



# Create your views here.



def home(request):
    dict_jobs=Jobs.objects.filter(is_available=True)
    return render(request, "index.html",locals())





def update_resume(request):
    resume = Resume.objects.filter(user=request.user)
    if request.method =='POST':
        form = UpdateResumeForm(request.POST, instance=resume)
        if form.is_valid():
            var = form.save(commit=False)
            user = User.objects.get(id=request.user)
            var.save()
            user.save()
            messages.info(request, 'Resume saved succesfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong')
    else:
        form = UpdateResumeForm(instance=resume)
        context = {'form':form}
        return render(request, 'dashboard.html',context)
    

    

def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context={'resume':resume}
    return render(request,'resume_details.html',context)



class ProfileView(View):
    def get(self,request):
        form = UpdateEmployeForm
        return render(request,'profile.html',locals())
    def post(self,request):
        form = UpdateEmployeForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            location = form.cleaned_data['location']
            job_title = form.cleaned_data['job_title']
            mobile = form.cleaned_data['mobile']
            aadhar = form.cleaned_data['aadhar']
            district = form.cleaned_data['district']

            reg = Employe(user=user,first_name=first_name,last_name=last_name,location=location,mobile=mobile,job_title=job_title,aadhar=aadhar,district=district)
            reg.save()
            messages.success(request, "Details saved Succesfully")
        else:
            messages.warning(request, "invalid data !!!")
        return render(request,'profile.html',locals())
    

def details(request):
    addr = Employe.objects.filter(user=request.user)
    return render(request, 'address.html',locals())




class updateAddress(View):
     def get(self, request,pk):
         add = Employe.objects.get(pk=pk)
         form = UpdateEmployeForm(instance=add)
         return render(request, 'updateAddress.html',locals())
     def post(self,request,pk):
         form = UpdateEmployeForm(request.POST)
         if form.is_valid():
             add = Employe.objects.get(pk=pk)
             add.first_name = form.cleaned_data['first_name']
             add.last_name = form.cleaned_data['last_name']
             add.location = form.cleaned_data['location']
             add.job_title = form.cleaned_data['job_title']
             add.mobile = form.cleaned_data['mobile']
             add.aadhar = form.cleaned_data['aadhar']
             add.district = form.cleaned_data['district']
             add.save()
             messages.success(request, "Details saved Succesfully")
         else:
             messages.warning(request, "invalid data !!!")

         return redirect('address')




def create_job(request):
    if request.method =='POST':
        form = CreateJobForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.author = request.user.employe
            var.save()
            messages.info(request, 'New job has been created')
            return redirect('profile')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('create-job')
    else:
        form = CreateJobForm()
        context = {'form':form}
        return render(request, 'create_job.html', context)




def myjobs(request):
    myjob = Jobs.objects.filter(user=request.user)
    return render(request, 'myjobs.html',locals())




class updateJobs(View):
     def get(self, request,pk):
         add = Jobs.objects.get(pk=pk)
         form = CreateJobForm(instance=add)
         return render(request, 'updatejob.html',locals())
     def post(self,request,pk):
         form = CreateJobForm(request.POST, request.FILES)
         if form.is_valid():
             add = Jobs.objects.get(pk=pk)
             add.title = form.cleaned_data['title']
             add.jobdesc = form.cleaned_data['jobdesc']
             add.salary = form.cleaned_data['salary']
             add.location = form.cleaned_data['location']
             add.experience = form.cleaned_data['experience']
             add.category = form.cleaned_data['category']
             add.contact_details = form.cleaned_data['contact_details']
             add.is_available = form.cleaned_data['is_available']
             add.cjob_img = form.cleaned_data['cjob_img']
             add.save()
             messages.success(request, "Details saved Succesfully")
         else:
             messages.warning(request, "invalid data !!!")

         return redirect('profile')

class CategoryView(View):
    def get(self,request,val):
        titl = Jobs.objects.filter(category=val)
        return render(request,'category.html',locals())



def job_details(request, pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied=True
    else:
        has_applied=False
    job = Jobs.objects.get(pk=pk)
    context = {'job':job,'has_applied':has_applied}
    return render(request, 'jobdetails.html', context)


def manage_jobs(request):
    cjob = Jobs.objects.filter(user=request.user)
    context ={'cjob':cjob}
    return render(request, 'manage_jobs.html', context)

def apply_to_job(request,pk):
    if request.user.is_authenticated:
        user = request.user
        job = Jobs.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission denied, You have already applied')
            return redirect('showapjobs')
        else:
            ApplyJob.objects.create(
            job=job,
            user = user
            )
        messages.success(request, 'You have succesfully applied !')
        return redirect('showapjobs')


def show_apjobs(request):
    user = request.user
    job = ApplyJob.objects.filter(user=user)
    return render(request,'addtoapjobs.html',locals())



def all_applicants(request, pk):
    job = Jobs.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job,'applicants':applicants}
    return render(request,'all_applicants.html', context)




def hire(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(location__icontains=q) | Q(location__icontains=q) | Q(job_title__icontains=q) | Q(district__icontains=q))
        data = Employe.objects.filter(multiple_q)
    else:
        data = Jobs.objects.all()
    context={
        'data':data,
    }
    return render(request, "hire.html",context)



