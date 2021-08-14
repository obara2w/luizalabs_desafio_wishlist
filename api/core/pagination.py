from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    Classe de paginação customizada, limitada por padrão com 10 items por página, pode ser alterada passando o parâmetro
    page_size
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
