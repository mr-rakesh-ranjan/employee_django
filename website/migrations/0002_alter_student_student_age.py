# Generated by Django 4.1.1 on 2022-09-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_age',
            field=models.IntegerField(),
        ),
    ]
