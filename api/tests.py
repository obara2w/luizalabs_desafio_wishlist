from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase

from api.models import Customer, Product

def create_customers():
    Customer.objects.create(name='Cliente 1', email='cliente1@luizalabs.com')
    Customer.objects.create(name='Cliente 2', email='cliente2@luizalabs.com')
    Customer.objects.create(name='Cliente 3', email='cliente3@luizalabs.com')


def create_products():
    Product.objects.create(title='Produto 1', price=148.98, image='http://blob.luizalabs.com/images/img_1.png', brand='Marca 1', review_score=5)
    Product.objects.create(title='Produto 2', price=878, image='http://blob.luizalabs.com/images/img_2.png', brand='Marca 2', review_score=2.6)
    Product.objects.create(title='Produto 3', price=.98, image='http://blob.luizalabs.com/images/img_3.png', brand='Marca 3', review_score=.9)


class CustomerTestCase(TestCase):
    def setUp(self):
        create_customers()

    def test_customer_insert_count(self):
        """Testa se os clientes foram inseridos corretamente."""
        # Recupera todos os clientes
        all_customers = Customer.objects.all()

        # checa se há 3 clientes inseridos
        self.assertTrue(len(all_customers) == 3)

    def test_customer_insert(self):
        """Testa se os clientes foram inseridos corretamente."""
        customer_1 = Customer.objects.get(email='cliente1@luizalabs.com')
        customer_2 = Customer.objects.get(email='cliente2@luizalabs.com')
        customer_3 = Customer.objects.get(email='cliente3@luizalabs.com')

        # checa se clientes foram inseridos:
        self.assertEqual(customer_1.name, 'Cliente 1')
        self.assertEqual(customer_1.email, 'cliente1@luizalabs.com')
        self.assertEqual(customer_2.name, 'Cliente 2')
        self.assertEqual(customer_2.email, 'cliente2@luizalabs.com')
        self.assertEqual(customer_3.name, 'Cliente 3')
        self.assertEqual(customer_3.email, 'cliente3@luizalabs.com')

    def test_customer_insert_email_duplicated(self):
        """Testa se o cliente não pode ser inserido duas vezes com o mesmo endereço de e-mail. """
        with self.assertRaisesRegex(IntegrityError, 'duplicate key'):
            Customer.objects.create(name='Cliente email duplicado', email='cliente1@luizalabs.com')

    def test_customer_update(self):
        """Testa se um cliente pode ser atualizado"""
        # Recupera cliente para atualizar
        customer_1 = Customer.objects.get(email='cliente1@luizalabs.com')
        
        # atualiza nome
        customer_1.name = 'Cliente 1 Da silva'
        customer_1.email = 'cliente1.da.silva@luizalabs.com'
        customer_1.save()

        # Recupera novamente
        customer_1 = Customer.objects.get(email='cliente1.da.silva@luizalabs.com')

        # checa se clientes foi atualizado corretamente
        self.assertEqual(customer_1.name, 'Cliente 1 Da silva')
        self.assertEqual(customer_1.email, 'cliente1.da.silva@luizalabs.com')
    
    def test_customer_delete(self):
        """Testa se um cliente pode ser apagado"""
        # Recupera cliente para deletar
        customer_2 = Customer.objects.get(email='cliente2@luizalabs.com')

        # deleta
        customer_2.delete()

        # Checa que cliente não existe mais
        with self.assertRaises(ObjectDoesNotExist):
            customer_2 = Customer.objects.get(email='cliente2@luizalabs.com')


class ProductTestCase(TestCase):
    def setUp(self):
        create_products()

    def test_product_insert_count(self):
        """Testa se os produtos foram inseridos corretamente."""
        # Recupera todos os produtos
        all_products = Product.objects.all()
    
        # checa se há 3 produtos inseridos
        self.assertTrue(len(all_products) == 3)
    
    def test_product_insert(self):
        """Testa se os produtos foram inseridos corretamente."""
        product_1 = Product.objects.get(title='Produto 1')
        product_2 = Product.objects.get(title='Produto 2')
        product_3 = Product.objects.get(title='Produto 3')

        # checa se produtos foram inseridos:
        self.assertEqual(product_1.title, 'Produto 1')
        self.assertEqual(product_1.price, 148.98)
        self.assertEqual(product_1.image, 'http://blob.luizalabs.com/images/img_1.png')
        self.assertEqual(product_1.brand, 'Marca 1')
        self.assertEqual(product_1.review_score, 5)

        self.assertEqual(product_2.title, 'Produto 2')
        self.assertEqual(product_2.price, 878.0)
        self.assertEqual(product_2.image, 'http://blob.luizalabs.com/images/img_2.png')
        self.assertEqual(product_2.brand, 'Marca 2')
        self.assertEqual(product_2.review_score, 2.6)

        self.assertEqual(product_3.title, 'Produto 3')
        self.assertEqual(product_3.price, 0.98)
        self.assertEqual(product_3.image, 'http://blob.luizalabs.com/images/img_3.png')
        self.assertEqual(product_3.brand, 'Marca 3')
        self.assertEqual(product_3.review_score, 0.9)

    def test_product_update(self):
        """Testa se um produto pode ser atualizado"""
        # Recupera produto para atualizar
        product_2 = Product.objects.get(title='Produto 2')
        
        # atualiza
        product_2.title = 'Produto 2 foo'
        product_2.price = 1588.98
        product_2.image = 'http://blob.luizalabs.com/images/img_1_foo.png'
        product_2.brand = 'Marca 2 foo'
        product_2.review_score = 4.1
        product_2.save()

        # Recupera novamente
        product_2 = Product.objects.get(title='Produto 2 foo')

        # checa se produto foi atualizado corretamente
        self.assertEqual(product_2.title, 'Produto 2 foo')
        self.assertEqual(product_2.price, 1588.98)
        self.assertEqual(product_2.image, 'http://blob.luizalabs.com/images/img_1_foo.png')
        self.assertEqual(product_2.brand, 'Marca 2 foo')
        self.assertEqual(product_2.review_score, 4.1)

    def test_product_delete(self):
        """Testa se um produto pode ser apagado"""
        # Recupera produto para deletar
        product_3 = Product.objects.get(title='Produto 3')

        # deleta
        product_3.delete()

        # Checa que produto não existe mais
        with self.assertRaises(ObjectDoesNotExist):
            Product.objects.get(title='Produto 3')


class WhishlistTestCase(TestCase):
    def setUp(self):
        create_customers()
        create_products()
    
    def test_whishlist(self):
        """Testa se é possivel adicionar produtos na wishlist do cliente"""

        # Recupera cliente
        customer_3 = Customer.objects.get(email='cliente3@luizalabs.com')

        # Recupera 2 produtos para ser inserido na wishlist do cliente
        product_2 = Product.objects.get(title='Produto 2')
        product_3 = Product.objects.get(title='Produto 3')

        # adiciona produtos na wishlist
        customer_3.wish_list.add(product_2, product_3)
        
        # checa se há 2 produtos na wishlist do cliente
        self.assertTrue(Customer.objects.get(email='cliente3@luizalabs.com').wish_list.count() == 2)
