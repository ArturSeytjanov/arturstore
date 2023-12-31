# Generated by Django 4.2.5 on 2023-09-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_nike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('charactor', models.TextField()),
                ('price_type', models.CharField(choices=[("so'm", "so'm"), ('₽', '₽'), ('$', '$')], default="so'm", max_length=10)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_nike.category')),
            ],
        ),
    ]
