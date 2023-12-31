# Generated by Django 4.2.5 on 2023-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='servicios')),
                ('cantidad', models.IntegerField(default=0)),
                ('disponibilidad', models.BooleanField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'articulo',
            },
        ),
    ]
