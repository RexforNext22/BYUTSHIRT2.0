# Generated by Django 3.2.8 on 2021-11-18 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleofClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_name', models.CharField(max_length=20)),
                ('rank', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='')),
                ('photo_main', models.ImageField(upload_to='photos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RanktShirts.category', to_field='category_name')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RanktShirts.material', to_field='material_name')),
                ('primarycolor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RanktShirts.primarycolor', to_field='color_name')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RanktShirts.size', to_field='size_name')),
            ],
        ),
    ]
