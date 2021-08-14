from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase

from api.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name='Cliente 1', email='cliente1@luizalabs.com')
        Customer.objects.create(name='Cliente 2', email='cliente2@luizalabs.com')
        Customer.objects.create(name='Cliente 3', email='cliente3@luizalabs.com')

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
