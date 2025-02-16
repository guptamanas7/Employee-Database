# Generated by Django 4.1.2 on 2022-10-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail_id', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('passwd', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
