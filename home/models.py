from django.db import models
from users.models import User

# Create your models here.


DISTRICT_CHOICES=(
    ('Trivandrum','Trivandrum'),
    ('Kollam','Kollam'),
    ('Pathanamthitta','Pathanamthitta'),
    ('Alappuzha','Alappuzha'),
    ('Kottayam','kottayam'),
    ('Idukki','Idukki'),
    ('Kochi','Kochi'),
    ('Thrissur','Thrissur'),
    ('Palakkadu','Palakkad'),
    ('Malappuram','Malappuram'),
    ('Wayanad','Wayanad'),
    ('Calicut','Calicut'),
    ('Kannur','Kannur'),
    ('Kasargod','Kasargod'),
    
)

CAT_CHOICES=(
    ('Plumber','Plumber'),
    ('Electrician','Electrician'),
    ('Mason','Mason'),
    ('Floor-worker','Floor-worker'),
    ('Helper','Helper'),
    ('Construction-worker','Construction-worker'),
    ('Carpenter','Carpenter'),
    ('Welder','Welder'),
)










class Resume(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    job_title = models.CharField(max_length=100,null=True, blank=True)
    aadhar = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    job_title = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=100,null=True, blank=True)
    aadhar = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(choices=DISTRICT_CHOICES, max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Jobs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.ForeignKey(Employe,on_delete=models.CASCADE)
    title = models.CharField(max_length=110)
    jobdesc = models.TextField()
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    category = models.CharField(choices=CAT_CHOICES,max_length=30)
    contact_details = models.CharField(max_length=50)
    cjob_img = models.ImageField(null=True, blank=True, upload_to='jobs')
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.user}'



class ApplyJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


