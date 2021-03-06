# Generated by Django 2.1.2 on 2018-11-08 14:37

import django.db.models.deletion
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BidRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('is_out', models.BooleanField(default=True, verbose_name='是否出局')),
            ],
            options={
                'verbose_name': '出价记录',
                'verbose_name_plural': '出价记录',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='类型名称')),
                ('image', models.ImageField(upload_to='category/image/', verbose_name='类型的图片')),
                ('index', models.IntegerField(verbose_name='排序')),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('goods_id', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='商品id')),
                ('goods_sn', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='商品唯一货号')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('market_price', models.FloatField(default=0.0, verbose_name='市场价格')),
                ('now_price', models.FloatField(default=0.0, verbose_name='现在价格')),
                ('step_price', models.FloatField(default=0.1, verbose_name='每次出价价格')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='商品简短描述')),
                ('goods_desc', markdownx.models.MarkdownxField(verbose_name='商品描述')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('goods_front_image', models.ImageField(upload_to='goods/front/image', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热拍')),
                ('is_sell', models.BooleanField(default=False, verbose_name='是否拍出')),
                ('periods', models.IntegerField(verbose_name='期数')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Category',
                                               verbose_name='商品类目')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('index', models.IntegerField(verbose_name='图片顺序')),
                ('image', models.ImageField(upload_to='goods/detail/image', verbose_name='图片')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Goods',
                                            verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('name', models.CharField(max_length=100, verbose_name='房间名字')),
                ('onlookers', models.IntegerField(verbose_name='围观人数')),
                ('bidders', models.IntegerField(verbose_name='出价人数')),
                ('goods',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '房间详情',
                'verbose_name_plural': '房间详情',
            },
        ),
        migrations.AddField(
            model_name='bidrecord',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Goods',
                                    verbose_name='商品'),
        ),
    ]
