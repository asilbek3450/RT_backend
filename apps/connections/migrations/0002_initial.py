# Generated by Django 4.1.2 on 2022-10-31 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '0001_initial'),
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertest',
            name='test_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
    ]
