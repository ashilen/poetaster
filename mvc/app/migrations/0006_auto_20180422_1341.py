# Generated by Django 2.0.3 on 2018-04-22 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0005_auto_20180421_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='previous_week',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_week', to='chart.Week'),
        ),
    ]
