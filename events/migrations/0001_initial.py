# Generated by Django 2.2.12 on 2020-05-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Event', max_length=30)),
                ('subtitle', models.CharField(default='No subtitle', max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
