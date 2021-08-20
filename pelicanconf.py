#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from collections import namedtuple

import os

AUTHORS = 'Pâmella Araújo Balcaçar'
SITENAME = 'Pâmella Araújo Balcaçar'
SITEURL = ''
TAGLINE = 'Bióloga & Tecnológa em Informática'
COPYRIGHT = u'Exceto onde indicado de outra forma, todos os conteúdos neste site estão licenciados sob licença Creative Commons Atribuição Compartilha Igual 4.0'

PATH = 'content'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'America/Campo_Grande'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme/pelican-chameleon'
DISPLAY_PAGES_ON_MENU = True

# Blogroll
MENUITEMS = [
        ('Início', '/'),
        ('Sobre', 'pages/sobre.html'),
        ('Projeto', 'pages/projeto.html'),
            ('Blog', [
            ('Tags', '/tags.html'),
            ('Categorias', '/categories.html'),
            ('Histórico', '/archives.html'),
            ]),
            ('Medias sociais', [
                ('CRBio Digital', 'http://www.crbiodigital.com.br/01/pamellabiotec'),
                ('Github', 'https://github.com/pamellabiotec'),
                ('Dev', 'https://dev.to/pamellabiotec'),
                ('Facebook', 'https://www.facebook.com/pamellabiotec'),
                ('Linkedin', 'https://www.linkedin.com/in/pamellabiotec/'),
                ('Twitter', 'https://twitter.com/pamellabiotec'),
                ('Telegram', 'https://t.me/pamellabiotec'), 
                ('Whatsapp', 'https://api.whatsapp.com/send?phone=5566996716343'),
            ]),
            ]


DEFAULT_PAGINATION = 15

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites"]

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}

STATIC_PATHS = ['images']