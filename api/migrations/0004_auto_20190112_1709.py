# Generated by Django 2.1.4 on 2019-01-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190111_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='swiped_taboo_cards',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='correctly_swiped_taboo_cards',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='translated_words',
            field=models.IntegerField(default=0),
        ),
    ]