# Generated by Django 4.1.2 on 2022-11-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_rename_answers_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
