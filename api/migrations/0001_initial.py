# Generated by Django 3.2.3 on 2021-08-14 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(error_messages={'unique': 'Já existe um cliente cadastrado com o e-mail informado.'}, max_length=50, unique=True, verbose_name='E-Mail')),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(help_text='Preço do Produto', verbose_name='Preço')),
                ('image', models.URLField(help_text='URL da Imagem do Produto', verbose_name='Imagem')),
                ('brand', models.CharField(help_text='Marca do Produto', max_length=100, verbose_name='Marca')),
                ('title', models.CharField(help_text='Nome do Produto', max_length=100, verbose_name='Título')),
                ('review_score', models.FloatField(blank=True, help_text='Média dos reviews para este Produto', null=True, verbose_name='Média dos reviews')),
            ],
            options={
                'verbose_name': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.product')),
            ],
            options={
                'verbose_name': 'Lista de Produtos Favorito',
                'unique_together': {('customer', 'product')},
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='wish_list',
            field=models.ManyToManyField(through='api.Wishlist', to='api.Product'),
        ),
    ]
