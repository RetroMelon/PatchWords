# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=200)),
                ('end', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(to='patchwords.Paragraph', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='patchwords.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'Not Specified', max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Not Specified', b'Not Specified')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='story',
            field=models.ForeignKey(to='patchwords.Story'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='paragraph',
            field=models.ForeignKey(to='patchwords.Paragraph'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favourite',
            name='story',
            field=models.ForeignKey(to='patchwords.Story'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
