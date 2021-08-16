from django.db import models


class Product(models.Model):
    """
    Modelo Produto
    """
    price = models.FloatField(null=False, blank=False, verbose_name='Preço', help_text='Preço do Produto')
    image = models.URLField(max_length=200, blank=False, verbose_name='Imagem', help_text='URL da Imagem do Produto')
    brand = models.CharField(max_length=100, null=False, blank=False, verbose_name='Marca', 
                             help_text='Marca do Produto')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Título', 
                             help_text='Nome do Produto')
    review_score = models.FloatField(null=True, blank=True, verbose_name='Média dos reviews', 
                                     help_text='Média dos reviews para este Produto')

    class Meta:
        verbose_name = 'Produto',
        ordering = ['-id']

    def __str__(self):
        return 'Produto {} da Marca {} com preço de R$ {}'.format(self.title, self.brand, self.price)

    objects = models.Manager()


class Customer(models.Model):
    """
    Modelo Cliente
    """
    # O cadastro dos clientes deve conter apenas seu nome e endereço de e-mail.
    name = models.CharField(max_length=100, verbose_name='Nome')

    # Marcando o campo como unique garante que um cliente se registrará duas vezes com o mesmo endereço de e-mail.
    email = models.EmailField(max_length=50, verbose_name='E-Mail', unique=True, 
                              error_messages={'unique': "Já existe um cliente cadastrado com o e-mail informado."})
    
    # Usar ManyToMany com Products garante que cada cliente só terá uma única lista de produtos, 
    # e que a lista de produtos tenha uma quantidade ilimitada de produtos.
    wish_list = models.ManyToManyField(Product, through='Wishlist')

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.name

    objects = models.Manager()


class Wishlist(models.Model):
    """
    Modelo Lista produto favorito
    """
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    # Usar uma ForeignKey garante que apenas produtos existentes sejam adicionado na lista.
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Lista de Produtos Favorito'

        # Criar uma constraint de chave única para o cliente e produto, garante que um produto não esteja duplicado 
        # na lista de produtos favoritos de um cliente.
        unique_together = ['customer', 'product']

    def __str__(self):
        return 'Cliente {} possui em sua lista de favoritos o produto {}'.format(self.customer.name, self.product.title)

    objects = models.Manager()
