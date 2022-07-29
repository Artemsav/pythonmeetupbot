# Generated by Django 4.0.5 on 2022-07-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_user_telegram_username_alter_donation_donated_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='status',
            field=models.CharField(choices=[('OP', 'Открыт'), ('FN', 'Закрыт')], default='OP', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название должности'),
        ),
    ]
