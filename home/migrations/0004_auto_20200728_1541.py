# Generated by Django 3.0.7 on 2020-07-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_subcatagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='catagory',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Show'), (2, 'Hide')], null=True),
        ),
    ]