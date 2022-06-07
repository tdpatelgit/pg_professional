# Generated by Django 4.0.4 on 2022-06-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0004_identity_identity_proof_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='non_refundable_amount',
            field=models.DecimalField(decimal_places=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='purpose',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='refundable_amount',
            field=models.DecimalField(decimal_places=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='rental',
            field=models.DecimalField(decimal_places=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='work_place',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='identity',
            name='identify_type',
            field=models.CharField(choices=[('Driving License', 'Driving License'), ('Aadhar Card', 'Aadhar Card')], default='Aadhar Card', max_length=20),
        ),
    ]