# Generated by Django 4.1.3 on 2023-02-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_tag_alter_category_slug_alter_post_category_post_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/", verbose_name="画像"
            ),
        ),
    ]