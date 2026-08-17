from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class CustomPageNumberPagination(PageNumberPagination):
    """
    Requirement 4: PageNumberPagination with exactly 3 restaurants per page.
    """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    Requirement 5: LimitOffsetPagination supporting ?limit=2&offset=2
    """
    default_limit = 3
    max_limit = 100
