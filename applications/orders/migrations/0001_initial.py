# Generated by Django 4.0.5 on 2022-08-03 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('DELIVERED', 'Delivered')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('close', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
