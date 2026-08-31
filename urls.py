from django.contrib import admin
from django.urls import path
from jobs import views
urlpatterns=[
path("admin/",admin.site.urls),
path("",views.home,name="home"),
path("register/",views.register_view,name="register"),
path("login/",views.login_view,name="login"),
path("logout/",views.logout_view,name="logout"),
path("jobs/",views.jobs_page,name="jobs_page"),
path("job/<int:job_id>/",views.job_detail,name="job_detail"),
path("job/<int:job_id>/apply/",views.apply_job,name="apply_job"),
path("job/<int:job_id>/save/",views.save_job,name="save_job"),
path("saved/",views.saved_jobs,name="saved_jobs"),
path("applications/",views.my_applications,name="my_applications"),
path("post-job/",views.post_job,name="post_job"),
]
