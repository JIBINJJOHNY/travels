# Generated by Django 4.2.5 on 2023-09-25 18:44

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='destination_image')),
                ('alt_text', models.CharField(blank=True, help_text='Optional. Max length: 300 characters', max_length=300, null=True, verbose_name='Alt text')),
                ('default_image', models.BooleanField(default=False, verbose_name='Default Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('destination', models.ForeignKey(help_text='Choose the destination for this image', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='destinations.destination', verbose_name='Destination')),
            ],
            options={
                'verbose_name': 'Destination image',
                'verbose_name_plural': 'Destination images',
                'ordering': ['destination'],
            },
        ),
    ]