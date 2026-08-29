from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from .models import Job,Application,SavedJob

def home(request):
    if request.GET and not request.user.is_authenticated: return redirect("login")
    return render(request,"home.html",{"jobs":Job.objects.all()[:6],"categories":Job.objects.values_list("category",flat=True).distinct().order_by("category"),"states":Job.objects.values_list("state",flat=True).distinct().order_by("state")})

@login_required
def jobs_page(request):
    jobs=Job.objects.all()
    q=request.GET.get("q","").strip(); 
    loc=request.GET.get("location","").strip(); 
    state=request.GET.get("state","")
    jt=request.GET.get("job_type",""); 
    cat=request.GET.get("category",""); 
    exp=request.GET.get("experience","")
    if q: jobs=jobs.filter(Q(title__icontains=q)|Q(company__icontains=q)|Q(skills__icontains=q))
    if loc: jobs=jobs.filter(location__icontains=loc)
    if state: jobs=jobs.filter(state=state)
    if jt: jobs=jobs.filter(job_type=jt)
    if cat: jobs=jobs.filter(category=cat)
    if exp: jobs=jobs.filter(experience__icontains=exp)
    return render(request,"jobs.html",{"jobs":jobs,"q":q,"location":loc,"state":state,"job_type":jt,"category":cat,"experience":exp,"states":Job.objects.values_list("state",flat=True).distinct().order_by("state"),"categories":Job.objects.values_list("category",flat=True).distinct().order_by("category")})

def register_view(request):
    if request.method=="POST":
        u=request.POST.get("username","").strip(); 
        e=request.POST.get("email","").strip(); 
        p=request.POST.get("password",""); 
        c=request.POST.get("confirm","")
        if not u or not e or not p: messages.error(request,"All fields are required.")
        elif p!=c: messages.error(request,"Passwords do not match.")
        elif User.objects.filter(username=u).exists(): 
            messages.error(request,"Username already exists.")
        else:
            user=User.objects.create_user(username=u,email=e,password=p); 
            login(request,user); 
            return redirect("home")
    return render(request,"register.html")

def login_view(request):
    if request.method=="POST":
        user=authenticate(request,username=request.POST.get("username",""),password=request.POST.get("password",""))
        if user: login(request,user); 
        return redirect("home")
        messages.error(request,"Invalid username or password.")
    return render(request,"login.html")

def logout_view(request): logout(request); return redirect("login")

def job_detail(request,job_id):
    job=get_object_or_404(Job,id=job_id)
    applied=request.user.is_authenticated and Application.objects.filter(job=job,applicant=request.user).exists()
    saved=request.user.is_authenticated and SavedJob.objects.filter(job=job,user=request.user).exists()
    return render(request,"job_detail.html",{"job":job,"applied":applied,"saved":saved})

@login_required
def apply_job(request,job_id):
    job=get_object_or_404(Job,id=job_id)
    if Application.objects.filter(job=job,applicant=request.user).exists(): 
        messages.info(request,"You already applied."); 
        return redirect("job_detail",job_id=job.id)
    if request.method=="POST":
        resume=request.POST.get("resume","").strip()
        if resume:
            Application.objects.create(job=job,applicant=request.user,resume=resume,message=request.POST.get("message","").strip())
            messages.success(request,"Application submitted successfully."); return redirect("my_applications")
        messages.error(request,"Resume is required.")
    return redirect("job_detail",job_id=job.id)

@login_required
def post_job(request):
    if request.method=="POST":
        keys=["title","company","location","state","experience","salary","skills","description","category"]
        d={k:request.POST.get(k,"").strip() for k in keys}; 
        d["job_type"]=request.POST.get("job_type","")
        if all(d.values()): 
            Job.objects.create(posted_by=request.user,**d); 
        messages.success(request,"Job published."); return redirect("jobs_page")
        messages.error(request,"Please complete all required fields.")
    return render(request,"post_job.html")

@login_required
def my_applications(request): 
    return render(request,"applications.html",{"applications":Application.objects.filter(applicant=request.user).select_related("job")})
@login_required
def save_job(request,job_id):
    job=get_object_or_404(Job,id=job_id); 
    x=SavedJob.objects.filter(job=job,user=request.user)
    if x.exists(): x.delete(); messages.info(request,"Removed from saved jobs.")
    else: SavedJob.objects.create(job=job,user=request.user); 
    messages.success(request,"Job saved.")
    return redirect("job_detail",job_id=job.id)
@login_required
def saved_jobs(request): 
    return render(request,"saved.html",{"saved":SavedJob.objects.filter(user=request.user).select_related("job")})
