# Generated by Django 4.2.7 on 2023-11-03 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('conversion_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('html', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('user_ideas', models.TextField()),
                ('traffic_description', models.TextField()),
                ('base_landing_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.landingpage')),
            ],
        ),
    ]
