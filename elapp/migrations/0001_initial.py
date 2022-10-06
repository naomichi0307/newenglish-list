# Generated by Django 4.1.2 on 2022-10-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('priority', models.CharField(choices=[('danger', 'high'), ('info', 'middle'), ('success', 'low')], max_length=50)),
                ('duedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Newword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('mean', models.CharField(max_length=100, null=True)),
                ('useful', models.PositiveIntegerField(default='1', verbose_name='the number of access')),
                ('priority', models.CharField(choices=[('danger', 'high'), ('info', 'middle'), ('success', 'low')], max_length=50, null=True)),
            ],
        ),
    ]