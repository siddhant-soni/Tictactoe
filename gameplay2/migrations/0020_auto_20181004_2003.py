# Generated by Django 2.1.2 on 2018-10-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0019_auto_20180719_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('W', 'First Player Wins'), ('S', 'Second Player To Move'), ('L', 'Second Player Wins'), ('F', 'First PLayer Move'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]