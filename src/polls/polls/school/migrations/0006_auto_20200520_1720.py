# Generated by Django 3.0.5 on 2020-05-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200520_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'get_latest_by': ('modified_at',), 'ordering': ('an', '-title')},
        ),
        migrations.AlterUniqueTogether(
            name='courses',
            unique_together={('title', 'an')},
        ),
    ]