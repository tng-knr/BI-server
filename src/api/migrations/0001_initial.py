# Generated by Django 2.2.4 on 2019-08-11 10:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(default='KSH', max_length=20)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('country', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsidiaries', to='api.Company')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ValueCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('subsidiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_centres', to='api.Subsidiary')),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ValueCentreTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_centres', to='api.Metric')),
                ('value_centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='api.ValueCentre')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Metric')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='api.Product')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='value_centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.ValueCentre'),
        ),
        migrations.CreateModel(
            name='IncomeStreamTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.BooleanField(default=False, help_text='This is to make sure deletes are not actual deletes')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('income_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='api.IncomeStream')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_streams', to='api.Metric')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='incomestream',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_streams', to='api.Product'),
        ),
    ]
