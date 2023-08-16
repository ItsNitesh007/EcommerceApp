# Generated by Django 4.2.3 on 2023-08-08 08:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_complaint_compid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(default=datetime.date.today)),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usermaster')),
            ],
        ),
    ]
