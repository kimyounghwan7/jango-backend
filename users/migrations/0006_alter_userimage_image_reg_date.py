# Generated by Django 4.0.3 on 2023-08-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userimage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image_reg_date',
            field=models.DateTimeField(null=True),
        ),
    ]
