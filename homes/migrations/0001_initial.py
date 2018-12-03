# Generated by Django 2.1.2 on 2018-11-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('goods_id', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='商品ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('image', models.ImageField(upload_to='homes/banner/image', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('url', models.CharField(blank=True, max_length=512, null=True, verbose_name='url')),
                ('activity', models.CharField(blank=True, max_length=30, null=True, verbose_name='跳转控制器')),
            ],
            options={
                'verbose_name': '首页Banner',
                'verbose_name_plural': '首页Banner',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('category_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='类型ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('icon', models.ImageField(upload_to='homes/topic/icon', verbose_name='图标')),
                ('index', models.IntegerField(default=0, verbose_name='排列顺序')),
                ('url', models.CharField(blank=True, max_length=512, null=True, verbose_name='url')),
                ('activity', models.CharField(blank=True, max_length=30, null=True, verbose_name='跳转控制器')),
            ],
            options={
                'verbose_name': '首页Topic',
                'verbose_name_plural': '首页Topic',
            },
        ),
    ]