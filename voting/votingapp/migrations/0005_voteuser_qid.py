# Generated by Django 4.2.3 on 2023-07-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0004_voteuser_ochosen'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteuser',
            name='qid',
            field=models.IntegerField(blank=True, max_length=40, null=True),
        ),
    ]
