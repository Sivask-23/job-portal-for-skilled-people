from django import forms
from .models import Resume, Employe, Jobs




    



class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['first_name','last_name','location','job_title','aadhar']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'job_title':forms.TextInput(attrs={'class':'form-control'}),
            'aadhar':forms.TextInput(attrs={'class':'form-control'})
           
        }

class UpdateEmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['first_name','last_name','location','job_title','aadhar','mobile','district']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'job_title':forms.TextInput(attrs={'class':'form-control'}),
            'aadhar':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
        }







class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title','jobdesc','salary','location','experience','category','contact_details','cjob_img','is_available']
        widgets={

            'title':forms.TextInput(attrs={'class':'form-control'}),
            'jobdesc':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'experience':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'contact_details':forms.TextInput(attrs={'class':'form-control'}),
            'is_available':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }




