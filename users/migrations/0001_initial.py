# Generated by Django 4.2.4 on 2023-08-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('profile', models.CharField(blank=True, choices=[("Directeur de l'informatique", "Directeur de l'informatique"), ('Chef de réseau', 'Chef de réseau'), ('Chef de service', 'Chef de service')], max_length=50, null=True)),
            ],
        ),
    ]
