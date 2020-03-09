from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Campus(models.Model):
    campus_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.campus_name


class College(models.Model):
    campus_name = models.ForeignKey(Campus, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"

    def __str__(self):
        return self.college_name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project_name


class ProjectInfo(models.Model):
    RF = 1
    USD = 2
    EUR = 3
    CURRENCY = ((RF, 'RF'), (USD, 'USD'), (EUR, 'EUR'))

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    donor = models.CharField(max_length=250)
    counter_part = models.BooleanField()
    country = CountryField(blank_label='(select country)')
    type_of_fund = models.CharField(max_length=250)
    domain_of_intervation = models.CharField(max_length=250)
    total_cost = models.PositiveIntegerField()
    cost_counter_part = models.PositiveIntegerField()
    currency = models.PositiveSmallIntegerField(choices=CURRENCY, default=1)
    start_date = models.DateField()
    initial_end_date = models.DateField()
    current_end_date = models.DateField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    project_coordinator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project info"
        verbose_name_plural = "Project info"

    def __str__(self):
        return self.project_name.project_name


class ProjectActivity(models.Model):

    PHASE = (('A', 'Phase A'), ('B', 'Phase B'), ('C', 'Phase C'), ('D', 'Phase D'), ('E', 'Phase E'))

    STATUS = (('PENDING', 'Pending'), ('ONGOING', 'Ongoing'), ('CLOSED', 'Closed'))

    activity_name = models.CharField(max_length=250)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    output = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    phase = models.CharField(max_length=30, choices=PHASE, default='Phase A')
    status = models.CharField(max_length=30, choices=STATUS, default='Pending')

    class Meta:
        verbose_name = 'Project Activity'
        verbose_name_plural = 'Project Activities'

    def __str__(self):
        return self.activity_name
