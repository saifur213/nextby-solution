# Generated by Django 4.2.5 on 2023-10-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pck_id', models.CharField(max_length=20)),
                ('pck_title', models.CharField(max_length=100)),
                ('pck_img', models.ImageField(upload_to='img/')),
                ('pck_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pck_f1', models.CharField(max_length=100)),
                ('pck_f2', models.CharField(max_length=100)),
                ('pck_f3', models.CharField(max_length=100)),
                ('pck_f4', models.CharField(max_length=100)),
                ('pck_f5', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
