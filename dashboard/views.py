from django.db.models import Count,Sum

from dashboard.forms import ProjectForm
from dashboard.models import ProjectTeam
from dashboard.models import UserProfile
from django.shortcuts import render, redirect
from projects.models import ProjectInfo, Project
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import ListView, TemplateView, CreateView
from dashboard.forms import ProjectForm, CreateProjectTeamForm, ProfileUpdateForm

from dashboard.models import ProjectTeam
from projects.models import ProjectInfo, Project, ProjectActivity

from dashboard.forms import ProjectForm, CreateProjectTeamForm

from dashboard.forms import ProjectForm
from dashboard.models import UserProfile


class HomePage(TemplateView):
    template_name = 'home.html'


class DashboardView(ListView):
    model = ProjectInfo
    template_name = 'dashboard/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["userprofile"] = UserProfile.objects.all()
        # context['projectinfo'] = Project.objects.values('projectactivity__status')\
        #                                          .annotate(activity_nam=Count('projectactivity__status'))

        context['projectinfo'] = Project.objects.annotate(num_activity=Count('projectactivity'))\
                                                # .annotate(sta=Count(projectactivity__status='PENDING'))
                                                # .annotate(sta=Count(projectactivity__status='PENDING'))




        context['project_activity'] = ProjectActivity.objects.filter(project_name=self.request.user.user_profile.project_name)
        return context


##############view for changing password##################################
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('login')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/change_password.html', {'form': form})


def add_project(request):
    return render(request, 'dashboard/add_project.html')


def test(request):
    return render(request, 'dashboard/test.html')


def activity_report(request):
    return render(request, 'dashboard/activity_report.html')


class ProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard/add_project.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        return redirect('add_project_leader')


class CreateProjectTeam(CreateView):
    model = ProjectTeam
    form_class = CreateProjectTeamForm
    template_name = 'dashboard/add_project_team.html'

    def form_valid(self, form):
        form.is_valid()
        form.save()
        return redirect('dashboard')



def update_profile(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
      
            return redirect('update_profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'dashboard/update_profile.html',{'p_form':p_form})

