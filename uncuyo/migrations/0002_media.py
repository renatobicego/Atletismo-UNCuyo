# Generated by Django 3.2.7 on 2021-11-11 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uncuyo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
                ('prueba_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uncuyo.prueba')),
            ],
        ),
    ]