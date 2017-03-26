from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
import datetime

# Create your views here.
def profile_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    current_user = request.user
    context = {"user":current_user,}
    return render(request,'profile_page/profile_page.html',context)