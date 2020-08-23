# Generated by Django 2.2.15 on 2020-08-23 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('taxi_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehiclelocation_vehicle', to='vehicle.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profilelocation_user', to='taxi_profile.UserProfile')),
            ],
        ),
    ]
