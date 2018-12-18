# Generated by Django 2.0 on 2018-12-16 21:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0014_auto_20181216_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, verbose_name='标题')),
                ('release_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最新修改时间')),
                ('comment_no', models.IntegerField(blank=True, null=True, verbose_name='评论数')),
                ('like_no', models.IntegerField(blank=True, null=True, verbose_name='点赞数')),
                ('contribute_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contribute_person', to=settings.AUTH_USER_MODEL, verbose_name='帖子投稿者')),
                ('release_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='release_person', to=settings.AUTH_USER_MODEL, verbose_name='帖子发布者')),
            ],
        ),
        migrations.RemoveField(
            model_name='opensourcedetail',
            name='opensource',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Programming',
        ),
        migrations.RemoveField(
            model_name='post',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='post',
            name='opensource',
        ),
        migrations.RemoveField(
            model_name='post',
            name='software',
        ),
        migrations.RemoveField(
            model_name='programmingdetail',
            name='programming',
        ),
        migrations.RemoveField(
            model_name='softwaredetail',
            name='software',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='comment_no',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='contribute_person',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='id',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='like_no',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='modify_time',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='release_person',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='release_time',
        ),
        migrations.RemoveField(
            model_name='opensource',
            name='title',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='comment_no',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='contribute_person',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='id',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='like_no',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='modify_time',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='release_person',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='release_time',
        ),
        migrations.RemoveField(
            model_name='programming',
            name='title',
        ),
        migrations.RemoveField(
            model_name='software',
            name='comment_no',
        ),
        migrations.RemoveField(
            model_name='software',
            name='contribute_person',
        ),
        migrations.RemoveField(
            model_name='software',
            name='id',
        ),
        migrations.RemoveField(
            model_name='software',
            name='like_no',
        ),
        migrations.RemoveField(
            model_name='software',
            name='modify_time',
        ),
        migrations.RemoveField(
            model_name='software',
            name='release_person',
        ),
        migrations.RemoveField(
            model_name='software',
            name='release_time',
        ),
        migrations.RemoveField(
            model_name='software',
            name='title',
        ),
        migrations.AddField(
            model_name='opensource',
            name='description',
            field=mdeditor.fields.MDTextField(default='', verbose_name='软件描述'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programming',
            name='description',
            field=mdeditor.fields.MDTextField(default='', verbose_name='软件描述'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='software',
            name='description',
            field=mdeditor.fields.MDTextField(default='', verbose_name='软件描述'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='software',
            name='icon',
            field=models.ImageField(default='', upload_to='media/software/icon/%Y/%m', verbose_name='软件icon'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OpensourceDetail',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='ProgrammingDetail',
        ),
        migrations.DeleteModel(
            name='SoftwareDetail',
        ),
        migrations.AddField(
            model_name='opensource',
            name='commonfields_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.CommonFields'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programming',
            name='commonfields_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.CommonFields'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='software',
            name='commonfields_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.CommonFields'),
            preserve_default=False,
        ),
    ]
