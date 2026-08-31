from django.db import models
from django.contrib.auth.models import User
class Job(models.Model):
    title=models.CharField(max_length=150); company=models.CharField(max_length=150)
    location=models.CharField(max_length=100); state=models.CharField(max_length=80,default="India")
    job_type=models.CharField(max_length=30,choices=[("Full Time","Full Time"),("Part Time","Part Time"),("Internship","Internship"),("Remote","Remote")])
    experience=models.CharField(max_length=80,default="Fresher"); salary=models.CharField(max_length=100,blank=True)
    skills=models.CharField(max_length=300); description=models.TextField(); category=models.CharField(max_length=80,default="Technology")
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-created_at"]
    def __str__(self): return f"{self.title} - {self.company}"
class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name="applications"); 
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    resume=models.CharField(max_length=255); message=models.TextField(blank=True)
    status=models.CharField(max_length=30,default="Applied",choices=[("Applied","Applied"),("Under Review","Under Review"),("Shortlisted","Shortlisted"),("Rejected","Rejected")])
    applied_at=models.DateTimeField(auto_now_add=True)
    class Meta: constraints=[models.UniqueConstraint(fields=["job","applicant"],name="unique_application")]
class SavedJob(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE); 
    user=models.ForeignKey(User,on_delete=models.CASCADE); saved_at=models.DateTimeField(auto_now_add=True)
    class Meta: constraints=[models.UniqueConstraint(fields=["job","user"],name="unique_saved_job")]
