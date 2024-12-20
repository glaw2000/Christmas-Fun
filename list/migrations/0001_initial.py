# Generated by Django 4.2.17 on 2024-12-18 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_item', models.JSONField()),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wisher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaler', to=settings.AUTH_USER_MODEL)),
                ('fk_wish_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coals', to='list.wishlist')),
            ],
            options={
                'unique_together': {('fk_wish_list_id', 'fk_user_id')},
            },
        ),
    ]
