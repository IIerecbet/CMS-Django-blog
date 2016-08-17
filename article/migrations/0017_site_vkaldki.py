# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:02
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20160717_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.TextField(verbose_name='Адрес сайта')),
                ('opisanie', models.TextField(verbose_name='Краткое описание сайта')),
                ('site_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('about_me', models.TextField(verbose_name='Обо мне')),
                ('about_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент обо мне')),
                ('about_opisanie', models.TextField(verbose_name='Описание Обо мне')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('contact_me', models.TextField(verbose_name='Cotact мне')),
                ('contact_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент контакты')),
                ('contact_opisanie', models.TextField(verbose_name='Описание контакты')),
                ('contact_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение контакты')),
            ],
            options={
                'db_table': 'site',
            },
        ),
        migrations.CreateModel(
            name='Vkaldki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='Вкладки сайта ссылка')),
                ('nazvanie', models.TextField(verbose_name='Название')),
            ],
            options={
                'db_table': 'vkladki',
            },
        ),
    ]
