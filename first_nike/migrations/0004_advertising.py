# Generated by Django 4.2.5 on 2023-09-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_nike', '0003_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
