# Generated by Django 3.0.3 on 2020-02-22 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_name', models.CharField(max_length=100)),
                ('tv_cat', models.CharField(max_length=100)),
                ('tv_link', models.CharField(max_length=300)),
                ('tv_img', models.ImageField(default='logo.jpg', upload_to='tvlogo')),
            ],
            options={
                'ordering': ('-tv_name',),
            },
        ),
    ]