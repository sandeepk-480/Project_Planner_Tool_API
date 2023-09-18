# Generated by Django 4.2.5 on 2023-09-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='team',
            new_name='team_id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='board',
            new_name='board_id',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETE', 'COMPLETE')], default='OPEN', max_length=50),
        ),
    ]