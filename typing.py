class _GenericType:
    def __getitem__(self, key):
        return key


Iterable = _GenericType()
Union = _GenericType()
Optional = _GenericType()

Type = object()
Callable = object()
Any = object()
List = object()
Dict = object()
Tuple = object()
Set = object()


def NewType(name, tp):
    return tp


def TypeVar(name, *constraints, bound=None):
    return object()


def Generic(*args, **kwargs):
    pass


def cast(typ, val):
    return val


def get_type_hints(obj, globals=None, locals=None):
    return {}


class GenericMeta(type):
    pass


TYPE_CHECKING = False
