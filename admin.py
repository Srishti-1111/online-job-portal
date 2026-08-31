from django.contrib import admin
from .models import Job,Application,SavedJob
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=("title","company","location","state","job_type","category","created_at")
    search_fields=("title","company","location","state","skills","category")
    list_filter=("state","job_type","category")
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=("job","applicant","status","applied_at"); list_filter=("status",)
@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin): list_display=("job","user","saved_at")
