# Generated by Django 4.1.2 on 2022-11-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='post_categories',
            field=models.ManyToManyField(related_name='post_cat', to='news.post'),
        ),
    ]