# Generated by Django 3.2.7 on 2021-11-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abr', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('descripción', models.TextField()),
                ('pista', models.BooleanField()),
                ('record', models.CharField(max_length=30)),
                ('frecord', models.CharField(max_length=30)),
                ('atleta', models.CharField(max_length=60)),
                ('atletaf', models.CharField(max_length=60)),
            ],
        ),
    ]
