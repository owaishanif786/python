# Name Mangling

If you want to create some private variable in Parent class  in such a way that you dont want to accidently overrdie in child class you can use __variable notation so that it will end up like this
`_ParentClass__variable`

if you `dir(childClass)` then you will see both variables of parent and child class separately.
`_ParentClass__variable` and `_ChildClass__variable`

See thie Mapping and SubMapping class example

## Rules for identifire to be name manageled

- The name starts with at least two underscores (__).
- The name has at most one trailing underscore (_).
- The identifier must be defined in the definition of the class at the same level as methods.
