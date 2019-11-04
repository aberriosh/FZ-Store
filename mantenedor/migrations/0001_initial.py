# Generated by Django 2.2.6 on 2019-10-22 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_nom', models.CharField(help_text='Ingrese Nombre del Desarrollador', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_desc', models.CharField(help_text='Ingrese Descripcion del genero', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IdiomaAu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_desc', models.CharField(help_text='Ingrese Descripcion del idioma', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IdiomaTx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_desc', models.CharField(help_text='Ingrese Descripcion del idioma', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_nom', models.CharField(help_text='Ingrese Nombre de la plataforma', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_nom', models.CharField(help_text='Ingrese Nombre del Distribuidor', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratng_desc', models.CharField(help_text='Ingrese Descripcion de la calificacion', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vg_nom', models.CharField(help_text='Ingrese Nombre del Juego', max_length=100)),
                ('vg_price', models.IntegerField(help_text='Ingrese el precio del juego (Ej: $ 999 999).')),
                ('vg_descr', models.TextField(help_text='Ingrese la descripcion del juego.', max_length=500)),
                ('vg_prev', models.BooleanField(null=True)),
                ('vg_online', models.BooleanField(null=True)),
                ('vg_online_plyr', models.IntegerField(help_text='Ingrese La cantidad de jugadores online.', max_length=2)),
                ('vg_local_plyr', models.IntegerField(help_text='Ingrese La cantidad de jugadores local (Ej: 1).', max_length=1)),
                ('vg_audio_lang', models.ManyToManyField(to='mantenedor.IdiomaAu')),
                ('vg_dev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Dev')),
                ('vg_gen', models.ManyToManyField(to='mantenedor.Genre')),
                ('vg_plat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Plat')),
                ('vg_pub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Pub')),
                ('vg_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Rating')),
                ('vg_tx_lang', models.ManyToManyField(to='mantenedor.IdiomaTx')),
            ],
        ),
    ]
