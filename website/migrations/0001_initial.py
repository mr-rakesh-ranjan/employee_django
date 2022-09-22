# Generated by Django 4.1.1 on 2022-09-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_college', models.CharField(max_length=200)),
                ('student_city', models.CharField(max_length=30)),
                ('student_age', models.IntegerField(max_length=13)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
