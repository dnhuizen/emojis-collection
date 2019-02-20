import codecs
import json
import urllib.request
import re
from collections import OrderedDict
from itertools import chain
from types import SimpleNamespace

from .defines import Patterns, StateNames, emoji_template, Mappings


class ParseLine():
    @staticmethod
    def group_name(line):
        p_line = line.split(Patterns.GROUP)[1].strip()
        p_line = re.sub(' & ', '_AND_', p_line)
        p_line = re.sub('(\b-\b)|( )', '_', p_line)
        p_line = p_line.upper()
        return p_line

    @staticmethod
    def subgroup_name(line):
        p_line = line.split(Patterns.SUBGROUP)[1].strip()
        p_line = re.sub(' & ', '_AND_', p_line)
        p_line = re.sub('(-)|( )', '_', p_line)
        p_line = p_line.upper()
        return p_line

    @staticmethod
    def emoji_name(line):
        p_line = re.sub(' & ', '_AND_', line)
        p_line = re.sub('(-)|( )|(: )', '_', p_line)
        p_line = p_line.upper()
        return p_line

    @staticmethod
    def emoji(line):

        hash_split = line.split('# ')

        if len(hash_split) > 2:
            name = ' '.join(hash_split[1:])
        else:
            name = hash_split[1]
        name = ''.join(Mappings.EMOJI_NAME[n] if n in Mappings.EMOJI_NAME else n for n in name)

        try:
            data = dict(
                code=Patterns.CODES.search(line).group().strip(),
                char=Patterns.CHAR.search(line).group().strip(),
                qualification=Patterns.QUALIFICATION.search(line).group().strip(),
                name=Patterns.NAME.search(name).group())
        except :

            pass

        return data

class EmojiGroup(SimpleNamespace):
    def __init__(self, **kwargs):
        self._k = kwargs
        super(EmojiGroup, self).__init__(**kwargs)

    def __iter__(self):
        level_vals = (val for val in self._k.values() if isinstance(val, emoji_template))
        sublevels = (val for val in self._k.values() if isinstance(val, EmojiGroup))
        return chain(level_vals, *sublevels)

    def to_dict(self):

        result = OrderedDict()

        for key, value in self._k.items():
            if isinstance(value, EmojiGroup):
                result[key] = value.to_dict()
            else:
                result[key] = value._asdict()
        return result

    def to_iter(self):
        return iter(self)

    def to_list(self):
        return [x for x in iter(self)]

    @property
    def code(self):

        return [x.code for x in iter(self)]

    @property
    def char(self):
        try:
            return [x.char for x in iter(self)]
        except:
            print('Nope')

    @property
    def name(self):
        return [x.name for x in iter(self)]


class _ParserStateMachine:

    def __init__(self, initial_state):
        self.state = initial_state
        self.current_group = None
        self.current_subgroup = None

    def transition(self, state):
        self.state = state


class EmojiParser(object):

    def __init__(self):
        self.data = None

    @classmethod
    def from_txt(cls, path):
        ep = cls()
        with open(path, 'r', encoding='utf-8', errors='ignore') as file_in:
            ep._parse(file_in.readlines())
        return ep

    @classmethod
    def from_json(cls, path):
        ep = cls()
        with open(path, 'r', encoding='utf-8') as f:
            ep.data = json.load(f)

        return ep

    @classmethod
    def from_url(cls, path):
        ep = cls()
        uf = urllib.request.urlopen(path)
        data = uf.read().decode('utf-8').split('\n')
        ep._parse(data)
        return ep

    def to_dict(self):
        return self.data

    def to_json(self, path):
        with codecs.open(path, 'w', encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False)

    def _parse(self, raw_data):
        self.data = {}
        s = _ParserStateMachine(StateNames.GROUP)

        for line in raw_data:

            if s.state == StateNames.GROUP:
                if line.startswith(Patterns.GROUP):
                    s.current_group = ParseLine.group_name(line)
                    self.data[s.current_group] = {}
                    s.transition(StateNames.SUBGROUP)

            elif s.state == StateNames.SUBGROUP:
                if line.startswith(Patterns.SUBGROUP):
                    s.current_subgroup = ParseLine.subgroup_name(line)
                    self.data[s.current_group][s.current_subgroup] = {}
                    s.transition(StateNames.EMOJI)

                elif line.startswith('#'):
                    s.transition(StateNames.GROUP)

            elif s.state == StateNames.EMOJI:
                if not (line is '\n' or line is ''):
                    emoji = ParseLine.emoji(line)
                    emoji_name = self._format_name(emoji['name'], self.data[s.current_group][s.current_subgroup])
                    self.data[s.current_group][s.current_subgroup][emoji_name] = emoji
                else:
                    s.transition(StateNames.SUBGROUP)

        return self.data


    @staticmethod
    def _format_name(name, subgroup):
        name = ParseLine.emoji_name(name)
        cnt = 2
        tmp_name = name

        while True:
            if tmp_name in subgroup:
                try:
                    tmp_name = name + '_num_' + Mappings.EMOJI_NAME[str(cnt)]
                except KeyError:
                    break
                cnt += 1
            else:
                break

        return tmp_name.upper()


def _create_emojis_data_struct(data):
    l1_groups = {}
    for key_l1 in data:
        l2_groups = {}

        for key_l2 in data[key_l1]:
            l3_groups = {}

            for key_l3 in data[key_l1][key_l2]:
                emoji_dct = data[key_l1][key_l2][key_l3]
                l3_groups[key_l3] = emoji_template(
                    emoji_dct['code'],
                    emoji_dct['char'],
                    emoji_dct['qualification'],
                    emoji_dct['name'])

            l2_groups[key_l2] = EmojiGroup(**l3_groups)

        l1_groups[key_l1] = EmojiGroup(**l2_groups)

    return EmojiGroup(**l1_groups)


