# Generated by Django 5.1.1 on 2024-09-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blog_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='genre',
            field=models.CharField(blank=True, choices=[('d', 'Diary'), ('s', 'Summary'), ('R', 'Review')], default='d', help_text='Blog genre', max_length=1),
        ),
    ]