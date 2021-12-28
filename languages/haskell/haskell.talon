# title: /LinuxVDI/i
mode: user.haskell
mode: user.auto_lang
and code.language: haskell
-
settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_variable_formatter = "PRIVATE_CAMEL_CASE"
    
type <user.fluent_type>: "{fluent_type} "
to type <user.fluent_type>: " -> {fluent_type} "
par type <user.fluent_type>: "({fluent_type})"
of type : " : "
of type <user.fluent_type>: " : {fluent_type} "
[op] {user.fluent_operators}: " {fluent_operators} "

var <user.fluent_var_name>: "{fluent_var_name}"

comment: "-- "
add todo: "-- TODO: "

case of <user.fluent_var_name>: "case {fluent_var_name} of\n"
default branch: "_ -> "
lambda: 
    "(\\x -> )"
    key(left)
