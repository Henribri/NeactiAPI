# Generated by Django 2.2.12 on 2020-05-22 00:02

from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Jeux-video', max_length=100)),
                ('iconId', models.IntegerField(default=58168)),
                ('fontFamily', models.CharField(default='MaterialIcons', max_length=100)),
                ('fontPackage', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Event', max_length=30)),
                ('subtitle', models.CharField(default='No subtitle', max_length=50)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(default='No address', max_length=50)),
                ('act_people', djongo.models.fields.ListField()),
                ('all_people', models.IntegerField(default=0)),
                ('description', models.CharField(default='No description', max_length=100)),
                ('category', models.IntegerField(default=1)),
            ],
        ),
    ]
