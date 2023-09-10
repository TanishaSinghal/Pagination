# Generated by Django 4.2.2 on 2023-06-27 18:33

from django.db import migrations

def create_data(apps, schema_editor):
        Student = apps.get_model('aggApp', 'Student')
        Student(name="Joe Silver", email="joe@email.com", document="22342342", phone="00000000").save()


class Migration(migrations.Migration):   
    
    dependencies = [
        ('aggApp', '0005_students'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]