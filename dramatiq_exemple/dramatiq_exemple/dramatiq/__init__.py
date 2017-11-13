"""Blok declaration example
"""
from anyblok.blok import Blok
from anyblok_dramatiq.actor import declare_actor_for


class DramatiqExemple(Blok):
    """Dramatiq's Blok class definition
    """
    version = "0.1.0"
    author = "jssuzanne"
    required = ['anyblok-core', 'dramatiq']

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import model  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import model  # noqa
        reload(model)

    @classmethod
    def define_actor(cls, registry):
        declare_actor_for(registry.Task, 'add')
