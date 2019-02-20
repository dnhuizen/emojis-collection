# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='emojis-collection',

    description='Collection of CLDR ordered Emojis-v12',
    author='Daniel Nieuwenhuizen',
    author_email='dnhuizen@gmail.com',
    url='https://github.com/s/emoji-collection',
    packages=find_packages(),
    keywords='emojis, unicode-v12, emojis-v12',
    include_package_data=True,
)