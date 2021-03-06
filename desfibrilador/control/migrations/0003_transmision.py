# Generated by Django 3.0.6 on 2020-05-06 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20200506_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transmision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateTimeField(verbose_name='date transmitted')),
                ('trans_text', models.CharField(max_length=100)),
                ('desfibrilador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Desfibrilador')),
            ],
        ),
    ]
