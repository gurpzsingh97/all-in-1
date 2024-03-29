# Generated by Django 4.0.3 on 2023-04-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_groomside_song_request_alter_brideside_song_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brideside',
            name='attending',
            field=models.CharField(choices=[('yes', 'Yes, I will be attending'), ('no', 'No, I will not be attending')], max_length=10),
        ),
        migrations.AlterField(
            model_name='groomside',
            name='attending',
            field=models.CharField(choices=[('yes', 'Yes, I will be attending'), ('no', 'No, I will not be attending')], max_length=10),
        ),
    ]
