# Generated by Django 4.1.2 on 2022-10-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_album_cover_alter_song_album_cover_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album_cover',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]
