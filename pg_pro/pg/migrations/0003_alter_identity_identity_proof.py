# Generated by Django 4.0.4 on 2022-06-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0002_alter_identity_identify_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='identity_proof',
            field=models.FileField(upload_to=''),
        ),
    ]