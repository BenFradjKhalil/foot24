# Generated by Django 4.0.1 on 2022-01-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art24', '0008_delete_derniers_articles'),
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
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]