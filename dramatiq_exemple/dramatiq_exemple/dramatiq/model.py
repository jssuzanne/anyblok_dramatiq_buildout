from anyblok import Declarations
from anyblok.column import Integer


Model = Declarations.Model


@Declarations.register(Model)
class Task():
    id = Integer(primary_key=True, nullable=False)

    @classmethod
    def add(cls, *args, **kwargs):
        print("add Task", args, kwargs, cls.registry.session)
        return cls.insert().id
