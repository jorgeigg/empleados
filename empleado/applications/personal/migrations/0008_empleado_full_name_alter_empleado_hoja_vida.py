# Generated by Django 4.0.5 on 2022-07-04 19:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_alter_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='NombresCompleto'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
