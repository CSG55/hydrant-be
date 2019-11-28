# Generated by Django 2.2.7 on 2019-11-24 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hydrantAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=100)),
                ('review_text', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hydrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydrantAPI.Hydrant')),
            ],
        ),
    ]
