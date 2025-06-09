from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return  render(request,'testapp/index.html')
from testapp.models import HydJobs
def hyd_jobs_view(request):
    job_list=HydJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/hydjobs.html',my_dict)


from testapp.models import BngJobs
def bng_jobs_view(request):
    job_list=BngJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/bngjobs.html',my_dict)

from testapp.models import PunneJobs
def punne_jobs_view(request):
    job_list=PunneJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/punne.html',my_dict)