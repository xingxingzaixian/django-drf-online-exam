# Generated by Django 3.2.9 on 2021-12-08 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='role',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='角色', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.tblrole'),
        ),
    ]
