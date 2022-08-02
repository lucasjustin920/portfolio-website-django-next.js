# Generated by Django 4.0.6 on 2022-08-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.CharField(max_length=300)),
                ('author_name', models.CharField(max_length=100)),
                ('author_title', models.CharField(max_length=100)),
                ('author_photo', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
