# Generated by Django 3.0.5 on 2020-05-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_bani'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='an',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
