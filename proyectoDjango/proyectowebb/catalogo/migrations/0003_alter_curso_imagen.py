# Generated by Django 4.2.5 on 2023-10-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_curso_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(upload_to='catalogo'),
        ),
    ]