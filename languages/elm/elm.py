
from talon import Context, Module, actions, settings, ctrl
from ...fluent import DEFAULT_OPERATORS, sep1

module = Module()
context = Context()
context.matches = r"""
mode: user.elm
mode: user.auto_lang
and code.language: elm
"""

context.lists["user.fluent_types"] = {
    # Basic
    "car": "Char",
    "character": "Char",
    "boolean": "Bool",
    "string": "String",
    "float": "Float",
    "integer": "Int",
    "hint": "Int",
    # Special
    "number": "number",
    "comparable": "comparable",
    "appendable": "appendable",
    "unit": "()",
    # Complex
    "list": "List",
    "array": "Array",
    "maybe": "Maybe",
    "CMD": "Cmd",
    "sub": "Sub",
    "task": "Task",
    "dictionary": "Dict",
    "set": "Set",
    "result": "Result",
    # Common
    "model": "Model",
    "message": "Msg",
}

context.lists["user.fluent_functions"] = {
    "print": 'Debug.log "" ',
    "filter": "filter",
    "map": "map",
    "and then": "andThen",
    "with default": "Maybe.withDefault",
}

context.lists["user.fluent_operators"] = DEFAULT_OPERATORS | {
    "piper": "|>",
    "compr": ">>",
    "apply": "<|",
    "compose": "<<",
    "p skip": "|.",
    "p keep": "|=",
    "route join": "</>",
}

# type captures


@context.capture(rule="<user.elm_function_type>")
def fluent_type(m) -> str: return m


@module.capture(rule=sep1('<user.elm_complex_type>', 'to'))
def elm_function_type(m) -> str:
    return " -> ".join(m.elm_complex_type_list)


@module.capture(rule="({user.fluent_types}|<user.letter>)+")
def elm_complex_type(m) -> str: return " ".join(list(m))


@module.capture(rule=sep1('<user.record_type_entry>'))
def record_type(m) -> str:
    return "{ " + ', '.join(m.record_type_entry_list) + " }"


@module.capture(rule="<user.text> [and <user.text>]* [of [{user.fluent_types}]]")
def record_type_entry(m) -> str:
    return ", ".join(f"{t} : {getattr(m, 'fluent_types', 'undefined')}" for t in m.text_list)


