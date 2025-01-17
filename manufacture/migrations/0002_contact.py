# Generated by Django 3.0.7 on 2020-06-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('your_enquiry', models.TextField()),
                ('industry', models.CharField(max_length=30)),
                ('product_type', models.CharField(max_length=30)),
            ],
        ),
    ]
