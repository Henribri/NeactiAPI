# Generated by Django 2.2.12 on 2020-05-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sport', max_length=100)),
                ('iconId', models.IntegerField(default=57392)),
                ('fontFamily', models.CharField(default='MaterialIcons', max_length=100)),
                ('fontPackage', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
