# Generated by Django 4.2.5 on 2023-10-04 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.menu')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ('-created',),
            },
        ),
    ]
