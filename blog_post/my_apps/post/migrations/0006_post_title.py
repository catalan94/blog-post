# Generated by Django 3.1 on 2020-09-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200906_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post Title', max_length=30),
            preserve_default=False,
        ),
    ]
