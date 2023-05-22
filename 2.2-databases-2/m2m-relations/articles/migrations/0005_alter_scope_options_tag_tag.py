# Generated by Django 4.2.1 on 2023-05-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_tag_articles_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.ManyToManyField(related_name='tag', to='articles.article'),
        ),
    ]