# Generated by Django 5.1.2 on 2024-10-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('ex_data', models.ImageField(upload_to='')),
            ],
        ),
    ]
