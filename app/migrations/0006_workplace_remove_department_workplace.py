# Generated by Django 4.1.3 on 2023-01-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_department_workplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='workplace',
        ),
    ]