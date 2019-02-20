
# Emojis-Collection
---

Emojis-Collection provides a set of Emojis ([Emoji 12.0](http://blog.unicode.org/2019/02/unicode-emoji-12-final-for-2019.html)) organised by [CLDR Emoji categories](https://www.unicode.org/Public/emoji/12.0/emoji-test.txt). The CLDR categorization provides logical groupings of Emojis which are recommended for keyboard layouts e.g., a subgroup of Face-smiling Emojis which belong to Smileys & Emotion group. Emojis-Collection allows for Emojis of CLDR subgroups or groups to be be easily accessed and navigated via a class attribute namespace structure. Emojis-Collection also allows for user-defined groups to be created, e.g., Emojis can be grouped by public sentiment categories.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
Minimum: Python 3.6

To render Emojis as a graphics in an Ipython console, insure the default encoding of your python environment set to UTF-8. Default encoding can be set using the terminal command:
    
    export PYTHONIOENCODING=UTF-8
WARNING: Failing to set the default encoding to UTF-8 may result in errors when using this package in an Ipython console.

### Installing

In the top level directory of this repository run the setup script:

    python setup.py install

### Tutorial
Import the full Emojis collection using:


```python
from emojis_collection import EMOJIS
```

Groups are defined as class attributes of `EMOJIS` and subgroups are defined as class attributes of groups. Groups and subgroup names are all notated using uppercase. For example, accessing all the Emojis in the  *Face Hand* subgroup of the *Smileys & Emotion* group is done as follow:


```python
EMOJIS.SMILEYS_AND_EMOTION.FACE_HAND
```




    EmojiGroup(FACE_WITH_HAND_OVER_MOUTH=Emoji(code='1F92D', char='\U0001f92d', qualification='fully-qualified', name='face with hand over mouth'), HUGGING_FACE=Emoji(code='1F917', char='🤗', qualification='fully-qualified', name='hugging face'), SHUSHING_FACE=Emoji(code='1F92B', char='\U0001f92b', qualification='fully-qualified', name='shushing face'), THINKING_FACE=Emoji(code='1F914', char='🤔', qualification='fully-qualified', name='thinking face'), _k={'HUGGING_FACE': Emoji(code='1F917', char='🤗', qualification='fully-qualified', name='hugging face'), 'FACE_WITH_HAND_OVER_MOUTH': Emoji(code='1F92D', char='\U0001f92d', qualification='fully-qualified', name='face with hand over mouth'), 'SHUSHING_FACE': Emoji(code='1F92B', char='\U0001f92b', qualification='fully-qualified', name='shushing face'), 'THINKING_FACE': Emoji(code='1F914', char='🤔', qualification='fully-qualified', name='thinking face')})



This returns an `EmojiGroup` of NamedTuples where each NamedTuple provides all relevant attributes to describe the Emojis. Emoji attributes include the unicode code point (*code*), UTF-8 encoded character (*char*), qualification status (*qualification*) and CLDR short name (*name*). Alternatively, Emojis can be returned as nested ordered dictionary by calling the `to_dict()` method of any `EmojiGroup` class instance:



```python
EMOJIS.SMILEYS_AND_EMOTION.FACE_HAND.to_dict()
```




    OrderedDict([('HUGGING_FACE',
                  OrderedDict([('code', '1F917'),
                               ('char', '🤗'),
                               ('qualification', 'fully-qualified'),
                               ('name', 'hugging face')])),
                 ('FACE_WITH_HAND_OVER_MOUTH',
                  OrderedDict([('code', '1F92D'),
                               ('char', '\U0001f92d'),
                               ('qualification', 'fully-qualified'),
                               ('name', 'face with hand over mouth')])),
                 ('SHUSHING_FACE',
                  OrderedDict([('code', '1F92B'),
                               ('char', '\U0001f92b'),
                               ('qualification', 'fully-qualified'),
                               ('name', 'shushing face')])),
                 ('THINKING_FACE',
                  OrderedDict([('code', '1F914'),
                               ('char', '🤔'),
                               ('qualification', 'fully-qualified'),
                               ('name', 'thinking face')]))])



This allows the Emojis to be hierarchically represented as groups/subgroups. Alternatively, a list containing the Emoji NamedTuples can be returned by calling the `to_list()` method of any `EmojiGroup` class instance:


```python
EMOJIS.SMILEYS_AND_EMOTION.FACE_HAND.to_list()
```




    [Emoji(code='1F917', char='🤗', qualification='fully-qualified', name='hugging face'),
     Emoji(code='1F92D', char='\U0001f92d', qualification='fully-qualified', name='face with hand over mouth'),
     Emoji(code='1F92B', char='\U0001f92b', qualification='fully-qualified', name='shushing face'),
     Emoji(code='1F914', char='🤔', qualification='fully-qualified', name='thinking face')]



A list of specific elements of the Namedtuple can be return directly by calling the `EmojiGroup` attribute properties `code`, `char`, `qualification` or `name`. For example, getting a list of Emoji characters for an `EmojiGroup` can be achieved using:


```python
EMOJIS.SMILEYS_AND_EMOTION.FACE_HAND.char
```




    ['🤗', '\U0001f92d', '\U0001f92b', '🤔']



Lastly, the `EmojiGroup` can be returned as an iterable by calling the `to.iter()` method:


```python
for e in EMOJIS.SMILEYS_AND_EMOTION.FACE_HAND.to_iter():
    print(e.name.ljust(30) + e.char)
```

    hugging face                  🤗
    face with hand over mouth     🤭
    shushing face                 🤫
    thinking face                 🤔


Note: All uppercase class instance attribute names of `EmojiGroup` are also of type `EmojiGroup` and thus allow for methods `to_dict()`, `to_list()` `to_iter()`, and properties `code`, `char`, `qualification` and `name`.

## Limitations
The Emojis are parsed by [data files](http://www.unicode.org/Public/emoji/12.0/) provided by The Unicode Consortium, meaning the accuracy of the Emojis and CLDR categorization are dependent on these files. Only a few Emojis have been hand validated.

## Authors

* **Daniel Nieuwenhuizen** - *Initial work* - [dnhuizen](https://github.com/dnhuizen/)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Acknowledgments

* The Unicode Consortium for providing the data files

