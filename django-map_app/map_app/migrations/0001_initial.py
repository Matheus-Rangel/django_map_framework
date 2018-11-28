# Generated by Django 2.1.2 on 2018-11-27 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('comentario', models.TextField()),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('elemento', models.TextField(blank=True)),
                ('numero', models.CharField(max_length=16)),
                ('empenhado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('anulado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('liquidado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pago', models.DecimalField(decimal_places=2, max_digits=15)),
                ('data_inicio', models.DateField()),
                ('data_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('telefone', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('site', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
            },
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=256)),
                ('cep', models.CharField(blank=True, max_length=8)),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=12)),
            ],
            options={
                'verbose_name': 'localização',
                'verbose_name_plural': 'localizações',
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('telefone', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('site', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Orgão',
                'verbose_name_plural': 'Orgãos',
            },
        ),
        migrations.CreateModel(
            name='OrgaoInstituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map_app.Instituicao')),
                ('orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map_app.Orgao')),
            ],
            options={
                'verbose_name': 'Orgão e Instituicão',
                'verbose_name_plural': 'Orgãos e Instituições',
            },
        ),
        migrations.AddField(
            model_name='orgao',
            name='instituicoes',
            field=models.ManyToManyField(through='map_app.OrgaoInstituicao', to='map_app.Instituicao'),
        ),
        migrations.AddField(
            model_name='orgao',
            name='localizacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map_app.Localizacao'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='localizacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map_app.Localizacao'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='orgaos',
            field=models.ManyToManyField(through='map_app.OrgaoInstituicao', to='map_app.Orgao'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map_app.Localizacao'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='orgao_instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map_app.OrgaoInstituicao'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map_app.Despesa'),
        ),
    ]