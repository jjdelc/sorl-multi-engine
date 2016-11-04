# coding: utf-8

from django.conf import settings
from sorl.thumbnail.helpers import get_module_class

engines = [get_module_class(engine_path)
    for engine_path in settings.SORL_ENGINES]

EngineMixin = type('EngineMixin', tuple(engines), {})
