# Generated by Django 4.2.7 on 2023-11-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='base_landing_page2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='b_test', to='dashboard.landingpage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='base_landing_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a_test', to='dashboard.landingpage'),
        ),
    ]
