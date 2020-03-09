from django import forms
from dashboard.models import ProjectTeam, Profile
from projects.models import Project


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'projectname', 'class': 'form-control', 'name': 'projectname',
               'placeholder': 'Enter Project name'}))
    project_code = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'projectcode', 'class': 'form-control', 'name': 'projectcode',
               'placeholder': 'Enter Project code'}))

    class Meta:
        model = Project
        fields = ['project_name', 'project_code']


class CreateProjectTeamForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields = '__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        # def __init__(self, *args, **kwargs):
        #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        #     self.fields['Image'].label = False
        
 
            

       

