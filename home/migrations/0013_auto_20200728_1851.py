# Generated by Django 3.0.7 on 2020-07-28 11:51

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200728_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newcatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Show'), (2, 'Hide')], null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Newcatagory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Newcatagory'),
        ),
        migrations.DeleteModel(
            name='catagory',
        ),
    ]
