from .main_page import MainPage
from .alfabank_page import AlfaBank
from .cloudpaymetns_page import CloudPayments
from .cart_page import CartPage

page_map = {
    "main": MainPage,
    "alfabank": AlfaBank,
    "cart": CartPage,
    "cloudpayments": CloudPayments
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
