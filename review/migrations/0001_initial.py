# Generated by Django 5.0 on 2023-12-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('hotel', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]
