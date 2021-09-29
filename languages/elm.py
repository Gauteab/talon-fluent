
from talon import Context, Module, actions, settings, ctrl
from ..fluent import DEFAULT_OPERATORS

module = Module()
context = Context()
context.matches = r"""
mode: user.elm
mode: command
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
}


context.lists["user.fluent_opterators"] = DEFAULT_OPERATORS | {
    "pipe right": "|>",
    "pipe left": "<|"
}


@context.capture(rule="(<user.function_type>|rec <user.record_type>|<user.elm_complex_type>)")
def fluent_type(m) -> str: return m


@module.capture(rule="{user.fluent_types}+")
def elm_complex_type(m) -> str: return " ".join(m.fluent_type_list)


@module.capture(rule="{user.fluent_types} [to {user.fluent_types}]*")
def function_type(m) -> str:
    return " -> ".join(m.fluent_types)


@module.capture(rule="<user.record_type_entry> [and <user.record_type_entry>]*")
def record_type(m) -> str:
    return "{ " + ', '.join(m.record_type_entry_list) + " }"


@module.capture(rule="<user.text> [and <user.text>]* [of [{user.fluent_types}]]")
def record_type_entry(m) -> str:
    return ", ".join(f"{t} :: {getattr(m, 'type', ' ')}" for t in m.text_list)


