from .emk24_page import Emk24Page
from .emkmet_ru_page import EmkMetRuPage

page_map = {
    "emk24.ru": Emk24Page,
    "emk24.by": Emk24Page,
    "emk24.kz": Emk24Page,
    "emk24.com.ua": Emk24Page,
    "emkmet.ru": EmkMetRuPage,
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
