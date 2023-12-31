# Generated by Django 4.2.4 on 2023-08-31 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter subcategory', max_length=150, verbose_name='SubCategory')),
                ('name_uz', models.CharField(help_text='Enter subcategory', max_length=150, null=True, verbose_name='SubCategory')),
                ('name_ru', models.CharField(help_text='Enter subcategory', max_length=150, null=True, verbose_name='SubCategory')),
                ('category', models.ForeignKey(help_text='Choose category', on_delete=django.db.models.deletion.CASCADE, to='myapp.category', verbose_name='Category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, help_text='Choose category', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subcategory', verbose_name='Category'),
        ),
    ]
