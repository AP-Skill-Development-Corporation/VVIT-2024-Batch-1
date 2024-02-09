# Generated by Django 3.2 on 2024-02-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.CharField(max_length=10)),
                ('edesg', models.CharField(choices=[('0', '-- Select Designation --'), ('1', 'Intern'), ('2', 'Junior Trainee'), ('3', 'Junior Developer')], default='0', max_length=5)),
            ],
        ),
    ]
