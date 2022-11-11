# Generated by Django 4.1.2 on 2022-11-04 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('usuario', '0008_usuario_fecnac_usuario_dir_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dir_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion.direccion'),
        ),
    ]