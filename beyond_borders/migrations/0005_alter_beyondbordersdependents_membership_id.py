# Generated by Django 4.0.2 on 2024-03-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyond_borders', '0004_beyondbordersdependents_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beyondbordersdependents',
            name='membership_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
