from django import forms

from projects.models import ProjectActivity


class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = ProjectActivity
        fields = '__all__'

