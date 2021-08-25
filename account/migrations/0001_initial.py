# Generated by Django 3.2.5 on 2021-08-21 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='technical_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(blank=True, max_length=20, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('services_description', models.TextField(blank=True, null=True)),
                ('services_icon', models.TextField(blank=True, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profilee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='pic')),
                ('profesion', models.CharField(blank=True, max_length=30, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('Dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('university', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('connection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='professional_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(blank=True, max_length=20, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='portfollio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallary', models.ImageField(blank=True, null=True, upload_to='gallary')),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
