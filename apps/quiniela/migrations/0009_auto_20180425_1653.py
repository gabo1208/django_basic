# Generated by Django 2.0.2 on 2018-04-25 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0008_remove_game_limit_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiniela.Group')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiniela.Team')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gamecontext',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='gamecontext',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gamecontext',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='game',
            name='context',
        ),
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiniela.Tournament'),
        ),
        migrations.DeleteModel(
            name='GameContext',
        ),
        migrations.AddField(
            model_name='group',
            name='teams',
            field=models.ManyToManyField(related_name='group_teams', through='quiniela.GroupTeam', to='quiniela.Team'),
        ),
        migrations.AddField(
            model_name='group',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiniela.Tournament'),
        ),
    ]
