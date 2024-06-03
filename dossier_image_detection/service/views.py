from django.shortcuts import render

# Create your views here.
# def services(request):
#     context = {
#     }

#     return render (request, "services.html", context = context)


# myapp/views.py


from django.shortcuts import render
# from .models import LogEntry
from .models import LoginActivity
# def log_list(request):
#     logs = LogEntry.objects.all()
#     return render(request, 'log_list.html', {'logs': logs})


from django.contrib.auth.signals import user_logged_in ,user_login_failed ,user_logged_out

def user_is_admin(user):
    return user.is_authenticated and user.is_staff


# @user_passes_test(user_is_admin)
def login_activity(request):
    login_entries = LoginActivity.objects.all().order_by('-timestamp')
    return render(request, 'log_list.html', {'login_entries': login_entries})