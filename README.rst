NAME

::

    BOTL - cli library


DESCRIPTION

::

    BOTL has all the python3 code to program a unix cli program, such as
    disk perisistence for configuration files, event handler to
    handle the client/server connection, code to introspect modules
    for commands, deferred exception handling to not crash on an
    error, a parser to parse commandline options and values, etc.

    BOTL uses OBJX, an module that allows for easy json save//load
    to/from disk of objects. It provides an "clean namespace" Object class
    that only has dunder methods, so the namespace is not cluttered with
    method names. This makes storing and reading to/from json possible.


AUTHOR

::

    Bart Thate <objx@proton.me>


COPYRIGHT

::

    BOTL is Public Domain.
