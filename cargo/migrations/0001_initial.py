# Generated by Django 4.2.7 on 2024-03-26 20:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='weight')),
                ('description', models.TextField(verbose_name='description')),
                ('end_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery', to='location.location')),
                ('start_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pick_up', to='location.location')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['weight'],
            },
        ),
    ]
