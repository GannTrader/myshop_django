# Generated by Django 3.0.7 on 2020-07-28 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200728_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='newCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Show'), (2, 'Hide')], null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.newCatagory')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcatagory',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_cat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.newCatagory'),
        ),
        migrations.DeleteModel(
            name='subCatagory',
        ),
    ]
