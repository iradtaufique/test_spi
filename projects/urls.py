from django.urls import path

from projects.views import CreateActivityView

urlpatterns = [
    path('create_activity/', CreateActivityView.as_view(), name='create_activity')
]
