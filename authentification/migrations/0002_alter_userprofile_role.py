# Generated by Django 4.2.4 on 2023-08-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('service', 'Chef de service'), ('informatique', "Directeur de l'informatique"), ('reseau', 'Chef réseau')], default='Server', max_length=50),
            preserve_default=False,
        ),
    ]
