# Generated by Django 2.2.9 on 2020-02-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('room_type', models.CharField(choices=[('office', 'Office'), ('faculty_cabin', 'Faculty Cabin'), ('classroom', 'Class Room'), ('workspace', 'Workspace'), ('other', 'Other')], max_length=100)),
                ('floor', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('description', models.TextField(blank=True, null=True)),
                ('occupants', models.ManyToManyField(blank=True, to='registrations.Person')),
            ],
        ),
    ]
