import os
from django.shortcuts import get_object_or_404, redirect, render
from .models import Kegiatan
from .forms import FormKegiatan
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse


def check_template(request):
    template_path = os.path.join(settings.BASE_DIR, 'extracurricular', 'templates', 'extracurricular', 'registration', 'registration_form.html')
    if os.path.exists(template_path):
        return HttpResponse(f"Template exists at {template_path}")
    else:
        return HttpResponse(f"Template does not exist at {template_path}")

def home(request):
    return render(request, 'extracurricular/home.html')

@login_required
def halaman_utama(request):
    return render(request, 'extracurricular/dashboard/dashboard.html')
@login_required
def manage_activities(request):
    kegiatan = Kegiatan.objects.all()
    context = {'kegiatan': kegiatan}
    return render(request, 'extracurricular/dashboard/manage_activities.html', context)

@login_required
def registration_view(request):
    if request.method == 'POST':
        form = FormKegiatan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')   
    else:
        form = FormKegiatan()

    template_path = os.path.join(settings.BASE_DIR, 'extracurricular', 'templates', 'extracurricular', 'registration', 'registration_form.html')
    if os.path.exists(template_path):
        return render(request, template_path, {'form': form})
    else:
        return HttpResponse(f"Template does not exist at {template_path}")
@login_required
def registration_success(request):
    return render(request, 'extracurricular/registration_success.html')

@login_required
def delete_activity(request, activity_id):
    kegiatan = get_object_or_404(Kegiatan, pk=activity_id)
    
    if request.method == 'POST':
        kegiatan.delete()
        return redirect('extracurricular:manage_activities')
    
    return render(request, 'extracurricular/confirm_delete.html', {'kegiatan': kegiatan})

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Kegiatan, pk=activity_id)
    if request.method == 'POST':
        form = FormKegiatan(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('manage_activities')
    else:
        form = FormKegiatan(instance=activity)
    return render(request, 'extracurricular/edit_activity.html', {'form': form, 'activity': activity})