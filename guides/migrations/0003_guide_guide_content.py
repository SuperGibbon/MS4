# Generated by Django 3.2.5 on 2021-08-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='guide_content',
            field=models.TextField(null=True),
        ),
    ]
