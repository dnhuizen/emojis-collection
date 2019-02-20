import re
import os
from collections import namedtuple

emoji_template = namedtuple('Emoji', 'code char qualification name')


class StateNames(object):
    GROUP = 'GROUP'
    SUBGROUP = 'SUBGROUP'
    EMOJI = 'EMOJI'
    STATE = 'GROUP'


class Mappings:
    EMOJI_NAME = {
        "#": 'hash',
        "*": 'start',
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen'
    }


class Patterns(object):
    GROUP = '# group:'
    SUBGROUP = '# subgroup:'
    CODES = re.compile(r'(.*)(?=;)')
    CHAR = re.compile(r'(?<=# )(.*?)(?= )')
    NAME = re.compile(r'(\b[a-zA-Z:,0-9_#*.“\- ]+)')
    QUALIFICATION = re.compile(r'(?<=; )(.*?)(?= )')


class DataPaths(object):
    JSON_PATH = os.path.join(os.path.dirname(__file__), 'resources/emoji-text.json')
    TEXT_PATH = os.path.join(os.path.dirname(__file__), 'resources/emoji-text.txt')

