# Generated by Django 2.0.2 on 2018-04-27 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0021_memberfixture_quiniela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberfixture',
            name='quiniela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiniela.Quiniela'),
        ),
    ]
