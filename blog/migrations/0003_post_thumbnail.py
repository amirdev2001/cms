# Generated by Django 4.2 on 2023-12-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='thumb'),
        ),
    ]
