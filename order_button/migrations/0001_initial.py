# Generated by Django 2.2 on 2019-04-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_answer', models.TextField()),
                ('response_date', models.DateTimeField(verbose_name='response_date')),
            ],
        ),
    ]
