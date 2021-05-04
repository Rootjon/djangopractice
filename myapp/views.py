from django.shortcuts import render

from  .models import Profile

# Create your views here.
def homepage(request):
    profie = Profile.objects.all()


    context = {
        'profile': profie

    }
    return render (request,'index.html',context)
