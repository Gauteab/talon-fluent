from talon import Context, Module, actions, settings, ctrl, app
from typing import Dict, List

module = Module()
context = Context()

module.list("fluent_variable_keywords", desc="keywords for declaring vaiables")
module.list("fluent_function_keywords", desc="keywords for declaring functions")
module.list("fluent_functions", desc="fluent functions")
module.list("fluent_types", desc="fluent types")
module.list("fluent_values", desc="fluent values")
module.list("fluent_modules", desc="fluent modules")
module.list("fluent_operators", desc="fluent opterators")

DEFAULT_OPERATORS = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "mod": "%",
    "is equal": "==",
    "not equal": "!=",
    "greater than": ">",
    "greater equals": ">=",
    "lesser equals": "<=",
    "less than": "<",
    "logical and": "&&",
    "logical or": "||",
}
context.lists["user.fluent_operators"] = DEFAULT_OPERATORS


def sep1(capture: str, sep: str = "and"):
    return f"{capture} ({sep} {capture})*"


@module.capture(rule="{user.fluent_functions}")
def fluent_function(m) -> str: return m


@module.capture(rule="{user.fluent_types}")
def fluent_type(m) -> str: return m


@module.capture(rule="{user.fluent_value}")
def fluent_value(m) -> str: return m


@module.capture(
    rule=f"[call] <user.fluent_function> [of] {sep1('<user.fluent_value>')}"
)
def fluent_invocation(m) -> str:
    return actions.user.fluent_invoke(m.fluent_function, m.fluent_value_list)


@module.capture(rule="(<user.fluent_opterator_expression>)")
def fluent_expression(m) -> str: return m


@module.capture(rule=sep1("<user.e1>", "{user.fluent_opterators}"))
def fluent_opterator_expression(m) -> str: return m


@module.capture(rule="(<user.fluent_invocation>|<user.fluent_expression_base>)")
def e1(m) -> str: return m


@module.capture(rule="(<user.fluent_var_name>|<user.letters>)")
def fluent_symbol(m) -> str: return m


@module.capture(rule="(<fluent_literal_expression>)")
def fluent_complex_literal_expression(m) -> str: return m


@module.capture(rule=f"list of {sep1('<user.fluent_expression_base>')}")
def fluent_list_literal(m) -> str:
    return "[" + ",".join(m.fluent_expression_base_list) + "]"


@module.capture(rule="string [of] <user.text>")
def fluent_string_literal(m) -> str: return f'"{m.text}"'


@module.capture(rule="(<number>|<user.fluent_value>)")
def fluent_expression_base(m) -> str: return m


@module.capture(rule="(<user.text>|<user.letters>)")
def fluent_var_name(m) -> str:
    formatter = settings.get("user.code_private_function_formatter")
    return actions.user.formatted_text(m[0], formatter)


@module.action_class
class language_actions:
    def fluent_invoke(function: str, args: List[str]) -> str:
        ""

    def insert_identifier(s: str):
        ""


@module.action_class
class Actions:
    def update_symbols(captures: Dict[str, List[str]]):
        "update captures"
        app.notify(str(captures["type"]))
    def fluent_update(captures: Dict[str, List[str]]):
        "update captures"
        app.notify(str(captures["type"]))
