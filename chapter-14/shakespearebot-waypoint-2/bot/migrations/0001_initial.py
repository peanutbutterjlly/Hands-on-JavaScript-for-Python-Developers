# Generated by Django 3.0.7 on 2020-06-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayerLine', models.CharField(max_length=1000)),
            ],
        ),
    ]
