from collections import deque
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from random import seed, randint, random
from rest_framework import status
from rest_framework.test import APITestCase

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


API_USER = 'user'
API_PASS = 'qweasdws'
N_CUSTOMER = 10
N_PRODUCT = 10

class LuizaLabsAPITestCase(APITestCase):
    def setUp(self) -> None:
        # cria usuario de api e faz login
        self.create_user_and_login()

    def create_user_and_login(self):
        """cria usuário para utilizar nas chamadas de APIs"""
        user = User.objects.create_user(API_USER,  'api.user@luizalabs.com', API_PASS)

        # checa que usuário consegue logar
        self.assertTrue(self.client.login(username=API_USER, password=API_PASS))


class CustomerAPITestCase(LuizaLabsAPITestCase):
    def setUp(self):
        super().setUp()

        # cria usuários para massa de teste
        self.create_n_customers(N_CUSTOMER)

    def create_customer(self, index):
        """Cria um usuário de API"""
        url = reverse('customer-list')
        data = {
            'name': 'API Customer {}'.format(index),
            'email': 'api{}.customer@luizalabs.com'.format(index)
        }
        response = self.client.post(url, data, format='json')
        return response.status_code

    def create_n_customers(self, n):
        """Cria n usuários de APIs"""
        customers_status = list(map(lambda x: self.create_customer(x), range(n)))

        # checa que foi criado atraves do status code
        deque(map(lambda x: self.assertEqual(x, status.HTTP_201_CREATED), customers_status))

    def test_create_customer(self):
        """Testa criação de cliente via API."""
        
        # Checa que foram criados N clientes
        self.assertEqual(Customer.objects.count(), N_CUSTOMER)

        # Checa cliente com id = 1
        self.assertEqual(Customer.objects.get(id=1).name, 'API Customer 0')
        self.assertEqual(Customer.objects.get(id=1).email, 'api0.customer@luizalabs.com')

    def get_all_customers(self):
        # Executa get
        url = reverse('customer-list')
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        return response

    def test_list_all_customer(self):
        """Testa a listagem de todos os clientes"""
        response = self.get_all_customers()

        # checa se há os n clientes
        self.assertEqual(len(response.data), N_CUSTOMER)

        # checa todos os valores
        [self.check_customer_att(customer) for customer in response.data]

    def check_customer_att(self, customer_api_obj):
        """checa todos os atributos do cliente com o que está na base de dados"""
        self.assertEqual(customer_api_obj.get('name'), Customer.objects.get(id=customer_api_obj.get('id')).name)
        self.assertEqual(customer_api_obj.get('email'), Customer.objects.get(id=customer_api_obj.get('id')).email)

    def test_get_one_customer(self):
        """Testa o retrieve de um único cliente"""
        # recupera um id para trazer os details
        response = self.get_all_customers()
        id = response.data[5].get('id')

        # Executa get
        url = reverse('customer-detail', kwargs={'pk': id})
        response = self.client.get(url, format='json')

        # Checa atributos
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.check_customer_att(response.data)
        
    def test_update_one_customer_put(self):
        """Testa a atualização de um cliente (put)"""
        # recupera um id para atualizar
        response = self.get_all_customers()
        id = response.data[5].get('id')

        # executa put   
        url = reverse('customer-detail', kwargs={'pk': id})
        response = self.client.put(url, data={'name': 'Nome alterado', 'email': 'email.alterado@luizalabs.com'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # checa atributos
        self.check_customer_att(response.data)

    def test_update_one_customer_patch(self):
        """Testa a atualização de um cliente (patch)"""
        # recupera um id para atualizar
        response = self.get_all_customers()
        id = response.data[5].get('id')

        # executa patch   
        url = reverse('customer-detail', kwargs={'pk': id})
        response = self.client.patch(url, data={'name': 'Apenas o nome será alterado'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # checa atributos
        self.check_customer_att(response.data)

    def remove_customer(self, id):
        """remove um cliente"""
        url = reverse('customer-detail', kwargs={'pk': id})
        response = self.client.delete(url)
        return response.status_code

    def test_delete_one_customer(self):
        """Testa a remoção de um cliente"""
        # recupera clientes para remover
        response = self.get_all_customers()

        # remove os clientes 1 por 1
        status_list = list(map(lambda customer: self.remove_customer(customer.get('id')), response.data))

        # checa que foi deletado atraves do status code
        deque(map(lambda x: self.assertEqual(x, status.HTTP_204_NO_CONTENT), status_list))

        # checa que há 0 clientes
        self.assertEqual(Customer.objects.count(), 0)


PRICE_MIN = 0
PRICE_MAX = 1000

class ProductAPITestCase(LuizaLabsAPITestCase):
    def setUp(self):
        super().setUp()

        # cria produtos para massa de teste
        self.create_n_products(N_PRODUCT)

    def create_product(self, index):
        """Cria um produto de API"""
        url = reverse('product-list')
        seed(index)
        data = {
            'title': 'API Product {}'.format(index), 
            'price': PRICE_MIN + (random() * (PRICE_MAX - PRICE_MIN)), 
            'image': 'http://blob.luizalabs.com/images/img_{}.png'.format(index),
            'brand': 'Marca {}'.format(index), 
            'review_score': randint(1, 5)
        }
        response = self.client.post(url, data, format='json')
        return response.status_code

    def create_n_products(self, n):
        """Cria n produtos de APIs"""
        products_status = list(map(lambda x: self.create_product(x), range(n)))

        # checa que foi criado atraves do status code
        deque(map(lambda x: self.assertEqual(x, status.HTTP_201_CREATED), products_status))

    def test_create_product(self):
        """Testa criação de produto via API."""
        
        # Checa que foram criados N produtos
        self.assertEqual(Product.objects.count(), N_PRODUCT)

        # Checa produto com id = 1
        self.assertEqual(Product.objects.get(id=1).title, 'API Product 0')
        self.assertEqual(Product.objects.get(id=1).brand, 'Marca 0')

    def get_all_products(self):
        # Executa get
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        return response

    def test_list_all_product(self):
        """Testa a listagem de todos os produtos"""
        response = self.get_all_products()

        # checa se há os n produtos
        self.assertEqual(response.data.get('count'), N_PRODUCT)

        # checa todos os valores
        [self.check_product_att(product) for product in response.data.get('results')]

    def check_product_att(self, product_api_obj):
        """checa todos os atributos do produto com o que está na base de dados"""
        self.assertEqual(product_api_obj.get('title'), Product.objects.get(id=product_api_obj.get('id')).title)
        self.assertEqual(product_api_obj.get('brand'), Product.objects.get(id=product_api_obj.get('id')).brand)
        self.assertEqual(product_api_obj.get('price'), Product.objects.get(id=product_api_obj.get('id')).price)
        self.assertEqual(product_api_obj.get('image'), Product.objects.get(id=product_api_obj.get('id')).image)
        self.assertEqual(product_api_obj.get('reviewScore'), Product.objects.get(id=product_api_obj.get('id')).review_score)

    def test_get_one_product(self):
        """Testa o retrieve de um único produto"""
        # recupera um id para trazer os details
        response = self.get_all_products()
        id = response.data.get('results')[5].get('id')

        # Executa get
        url = reverse('product-detail', kwargs={'pk': id})
        response = self.client.get(url, format='json')

        # Checa atributos
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.check_product_att(response.data)
        
    def test_update_one_product_put(self):
        """Testa a atualização de um produto (put)"""
        # recupera um id para atualizar
        response = self.get_all_products()
        id = response.data.get('results')[5].get('id')

        # executa put   
        url = reverse('product-detail', kwargs={'pk': id})
        response = self.client.put(url, data={'title': 'Titulo alterado', 'brand': 'Nova Marca', 'price': 123, 'image': 'http://imagem.com', 'reviewScore': 5}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # checa atributos
        self.check_product_att(response.data)

    def test_update_one_product_patch(self):
        """Testa a atualização de um produto (patch)"""
        # recupera um id para atualizar
        response = self.get_all_products()
        id = response.data.get('results')[5].get('id')

        # executa patch   
        url = reverse('product-detail', kwargs={'pk': id})
        response = self.client.patch(url, data={'title': 'Apenas o titulo será alterado'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # checa atributos
        self.check_product_att(response.data)

    def remove_product(self, id):
        """remove um produto"""
        url = reverse('product-detail', kwargs={'pk': id})
        response = self.client.delete(url)
        return response.status_code

    def test_delete_one_product(self):
        """Testa a remoção de um produto"""
        # recupera produtos para remover
        response = self.get_all_products()

        # remove os produtos 1 por 1
        status_list = list(map(lambda product: self.remove_product(product.get('id')), response.data.get('results')))

        # checa que foi deletado atraves do status code
        deque(map(lambda x: self.assertEqual(x, status.HTTP_204_NO_CONTENT), status_list))

        # checa que há 0 produtos
        self.assertEqual(Product.objects.count(), 0)
        