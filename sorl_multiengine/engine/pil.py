# coding: utf-8

from sorl.thumbnail.engines.pil_engine import Engine as PILEngine

from sorl_multiengine.engine import EngineMixin

class Engine(EngineMixin, PILEngine):
    pass
