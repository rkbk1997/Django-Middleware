# Generated by Django 3.0.3 on 2020-02-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findusapp', '0004_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=300, null=True)),
                ('lname', models.CharField(blank=True, max_length=300, null=True)),
                ('username', models.CharField(blank=True, max_length=300, null=True)),
                ('password1', models.CharField(blank=True, max_length=300, null=True)),
                ('password2', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
    ]
