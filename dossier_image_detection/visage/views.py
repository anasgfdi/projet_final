from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def homepage(request):
    context = {
    }

    return render (request, "home_page.html", context = context)
