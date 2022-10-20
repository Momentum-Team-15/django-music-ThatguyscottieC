# Generated by Django 4.1.2 on 2022-10-20 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_song_album_cover_remove_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_cover',
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album'),
        ),
    ]
