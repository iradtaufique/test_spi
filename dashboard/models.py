from django.db import models
from phone_field import PhoneField
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from projects.models import Project, Campus, College
from django.contrib.auth.models import User, AbstractUser


class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete = models.CASCADE)
    image   = models.ImageField(default='default.jpg', upload_to='profile_pictures')


    def __str__(self):
        return f'{self.user.username} Profile'


class UserProfile(models.Model):
    PROJECT_MANAGER = 1
    EVALUATOR = 2
    PROJECT_ACCOUNTANT = 3
    UR_SPIU = 4
    ROLE = (
        (PROJECT_MANAGER, 'Project manager'),
        (EVALUATOR, 'Evaluator'),
        (PROJECT_ACCOUNTANT, 'Project Accountant'),
        (UR_SPIU, 'UR SPIU'),
    )

    user_name = models.OneToOneField(User, default=1, on_delete=models.CASCADE, related_name='user_profile')
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE, default=2)

    class Meta:
        verbose_name = "Project User"
        verbose_name_plural = "Project Users"

    def __str__(self):
        return self.user_name.get_username()


class ProjectTeam(models.Model):
    MALE = 1
    FEMALE = 2
    SEX = ((MALE, 'Male'), (FEMALE, 'Female'))

    BACHELOR = 1
    MASTERS = 2
    PHD = 3
    PROFESSOR = 4
    DEGREES = ((BACHELOR, 'Bachelor'), (MASTERS, 'Masters'), (PHD, 'Phd'), (PROFESSOR, 'Professor'))

    RF = 1
    USD = 2
    EUR = 3
    CURRENCY = ((RF, 'RF'), (USD, 'USD'), (EUR, 'EUR'))

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    donor = models.CharField(max_length=250)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    sex = models.PositiveSmallIntegerField(choices=SEX, default=1)
    nationality = national_id = CountryField(blank_label='(Select Country)')
    national_id = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField(help_text='Enter Phone Phone')
    position = models.CharField(max_length=250)
    degree = models.PositiveSmallIntegerField(choices=DEGREES, default=1)
    domain = models.CharField(max_length=250)
    status_in_ur = models.CharField(max_length=250)
    recruitment_date = models.DateField()
    contract_expiration = models.DateField()
    gross_salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    # currency = models.PositiveSmallIntegerField(choices=CURRENCY, default=1)
    rssb_number = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Project Team"
        verbose_name_plural = "Project Team"

    def __str__(self):
        return self.first_name

#############################################################################


