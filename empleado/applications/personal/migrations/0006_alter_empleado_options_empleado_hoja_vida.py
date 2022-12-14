# Generated by Django 4.0.5 on 2022-06-29 19:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Employee', 'verbose_name_plural': 'My Employees'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='Texto'),
            preserve_default=False,
        ),
    ]
