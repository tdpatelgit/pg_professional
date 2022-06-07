# Generated by Django 4.0.4 on 2022-06-05 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0008_vehicle_alter_identity_identify_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pg.vehicle'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='identify_type',
            field=models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('Driving License', 'Driving License')], default='Aadhar Card', max_length=20),
        ),
    ]