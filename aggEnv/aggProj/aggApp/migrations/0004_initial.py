# Generated by Django 4.2.2 on 2023-06-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aggApp', '0003_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('document', models.CharField(max_length=20, verbose_name='Document')),
                ('phone', models.CharField(max_length=20)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
    ]
