# Generated by Django 3.0.4 on 2020-03-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectactivity',
            name='phase',
            field=models.CharField(choices=[('A', 'Phase A'), ('B', 'Phase B'), ('C', 'Phase C'), ('D', 'Phase D'), ('E', 'Phase E')], default='Phase A', max_length=30),
        ),
        migrations.AlterField(
            model_name='projectactivity',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ONGOING', 'Ongoing'), ('CLOSED', 'Closed')], default='Pending', max_length=30),
        ),
    ]
