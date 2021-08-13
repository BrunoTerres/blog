# Generated by Django 3.2.6 on 2021-08-13 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=256)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='role.role')),
            ],
        ),
    ]
