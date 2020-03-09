from django.shortcuts import render, redirect
from django.views.generic import CreateView

from projects.forms import CreateActivityForm
from projects.models import ProjectActivity


class CreateActivityView(CreateView):
    model = ProjectActivity
    form_class = CreateActivityForm
    template_name = 'project/project_activity.html'

    def form_valid(self, form):
        form.is_valid()
        form.save()
        return redirect('dashboard')
