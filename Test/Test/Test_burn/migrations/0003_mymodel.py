# Generated by Django 2.2.4 on 2019-11-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_burn', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
            ],
        ),
    ]
