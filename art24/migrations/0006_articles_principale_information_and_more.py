# Generated by Django 4.0.1 on 2022-01-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art24', '0005_derniers_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles_principale',
            name='information',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles_principale',
            name='titre',
            field=models.CharField(default=150, max_length=150),
            preserve_default=False,
        ),
    ]
