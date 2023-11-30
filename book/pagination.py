from rest_framework.pagination import PageNumberPagination


class BookPagePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 1000
    page_query_param = 'page'
