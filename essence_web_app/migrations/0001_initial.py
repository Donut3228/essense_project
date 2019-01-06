# Generated by Django 2.1.4 on 2019-01-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Item.', max_length=100)),
                ('description', models.CharField(default='An item.', max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='essence_web_app.Brand')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='essence_web_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(max_length=150)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essence_web_app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='essence_web_app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='essence_web_app.SubCategory'),
        ),
    ]
