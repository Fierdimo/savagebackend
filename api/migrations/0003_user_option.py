# Generated by Django 4.0.4 on 2022-06-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='option',
            field=models.CharField(default='', help_text='Ultima accion', max_length=10),
        ),
    ]
