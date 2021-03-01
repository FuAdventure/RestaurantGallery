# Generated by Django 3.1.7 on 2021-02-27 21:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='logo_image',
            field=models.ImageField(blank=True, upload_to='pizzariaImages'),
        ),
        migrations.AlterField(
            model_name='pizzeria',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d+$')]),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('image_title', models.CharField(blank=True, max_length=120)),
                ('uploded_at', models.DateTimeField(auto_now_add=True)),
                ('pizzeria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizzeria_images', to='stores.pizzeria')),
            ],
            options={
                'ordering': ['-uploded_at'],
            },
        ),
    ]