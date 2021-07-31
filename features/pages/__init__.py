from .emk24_page import Emk24Page
from .emkmet_ru_page import EmkMetRuPage
from .emksteel_ru import EmksteelRu
from .emkworld_com import EmkworldCom
from .forging_emk24_su import ForgingEmk24Su
from .railws_com import RailwsCom
from .a1_valves_com import A1ValvesCom

page_map = {
    "emk24.ru": Emk24Page,
    "emk24.by": Emk24Page,
    "emk24.kz": Emk24Page,
    "emk24.com.ua": Emk24Page,
    "emkmet.ru": EmkMetRuPage,
    "forging.emk24.su": ForgingEmk24Su,
    "railws.com": RailwsCom,
    "a1-valves.com": A1ValvesCom,
    "emksteel.ru": EmksteelRu,
    "emkworld.com": EmkworldCom,
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
