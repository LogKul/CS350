# Generated by Django 4.1 on 2022-09-18 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.author')),
            ],
        ),
    ]