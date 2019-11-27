# Generated by Django 2.2.5 on 2019-09-04 05:58

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import main.users.manager.usermanager
import main.users.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True, verbose_name='Email address')),
                ('pin', models.PositiveIntegerField(default=main.users.models.user.get_random_pin, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='PIN')),
                ('first_name', models.CharField(blank=True, default='', max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, default='', max_length=30, verbose_name='Last name')),
                ('birthdate', models.DateField(null=True, verbose_name='Birth Date')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Is Verified')),
                ('is_email', models.BooleanField(default=False, verbose_name='Is Email Verified')),
                ('img', models.ImageField(blank=True, default='/static/assets/img/user.png', upload_to='users', verbose_name='Avatar')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('mob', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Your phone number should consist of 9-15 digits. Example: 1114442277', regex='(\\d{9,15})$')], verbose_name='Mobile')),
                ('tel', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Your phone number should consist of 9-15 digits. Example: 1114442277', regex='(\\d{9,15})$')], verbose_name='Telephone')),
                ('fax', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Your phone number should consist of 9-15 digits. Example: 1114442277', regex='(\\d{9,15})$')], verbose_name='Fax')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
            managers=[
                ('objects', main.users.manager.usermanager.UserManager()),
            ],
        ),
    ]
