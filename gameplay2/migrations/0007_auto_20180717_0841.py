# Generated by Django 2.0.5 on 2018-07-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0006_auto_20180717_0831'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Move',
            new_name='Moves',
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('D', 'Draw'), ('F', 'First PLayer Move'), ('S', 'Second PLayer Move')], default='F', max_length=1),
        ),
    ]