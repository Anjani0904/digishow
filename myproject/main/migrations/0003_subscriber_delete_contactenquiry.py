# Generated by Django 4.0.1 on 2022-05-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contactenquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contactEnquiry',
        ),
    ]