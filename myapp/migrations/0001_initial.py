# Generated by Django 4.2.4 on 2023-08-31 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter Name', max_length=150, null=True, verbose_name='Name')),
                ('telegram_id', models.CharField(help_text='Enter Telegram ID', max_length=30, unique=True, verbose_name='Telegram ID')),
                ('language', models.CharField(default='uz', help_text='Enter Language', max_length=4, verbose_name='Language')),
                ('phone', models.CharField(blank=True, help_text='Enter phone number', max_length=20, null=True, verbose_name='Phone number')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'BotUSer',
                'verbose_name_plural': 'BotUSer',
                'db_table': 'BotUSer',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Category', max_length=150, verbose_name='Category')),
                ('name_uz', models.CharField(help_text='Enter Category', max_length=150, null=True, verbose_name='Category')),
                ('name_ru', models.CharField(help_text='Enter Category', max_length=150, null=True, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.botuser', to_field='telegram_id', verbose_name='Bot User')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter product name', max_length=150, null=True, verbose_name='Product')),
                ('name_uz', models.CharField(blank=True, help_text='Enter product name', max_length=150, null=True, verbose_name='Product')),
                ('name_ru', models.CharField(blank=True, help_text='Enter product name', max_length=150, null=True, verbose_name='Product')),
                ('image', models.ImageField(blank=True, help_text='Upload image', null=True, upload_to='product-images', verbose_name='Images')),
                ('about', models.TextField(verbose_name='About')),
                ('about_uz', models.TextField(null=True, verbose_name='About')),
                ('about_ru', models.TextField(null=True, verbose_name='About')),
                ('price', models.IntegerField(blank=True, help_text='Enter price', null=True, verbose_name='Price')),
                ('discount', models.IntegerField(blank=True, help_text='Enter discount', null=True, verbose_name='Discount')),
                ('category', models.ForeignKey(help_text='Choose category', on_delete=django.db.models.deletion.CASCADE, to='myapp.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myapp.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.botuser', to_field='telegram_id', verbose_name='Bot User')),
            ],
        ),
    ]