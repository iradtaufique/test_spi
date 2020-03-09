from django.urls import path
from .views import add_project, test
from .views import DashboardView, HomePage, activity_report, ProjectView, change_password, CreateProjectTeam, \
    update_profile

urlpatterns = [

    path('', HomePage.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('change_password/', change_password, name='change_password'),
    path('add-project/', add_project, name='add_project'),
    path('test/', test, name='test'),
    path('add-project/', ProjectView.as_view(), name='add_project'),
    path('activity-report/', activity_report, name='activity-report'),
    path('add_project_team/', CreateProjectTeam.as_view(), name='add_project_team'),
    path('update_profile/', update_profile, name='update_profile'),

]
