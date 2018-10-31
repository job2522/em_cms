# Generated by Django 2.1.1 on 2018-10-31 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_remove_shop_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='events.Category'),
        ),
    ]
