NAME

::

    BOTL - bot library


SYNOPSIS

::

    botl  <cmd> [key=val] [key==val]
    botl  [-c] [-v]
    botld 

    options are:

    -c     start console
    -v     use verbose


INSTALL

::

    $ pipx install botl
    $ pipx ensurepath


DESCRIPTION

::

    BOTL contains all the python3 code to program objects in a functional
    way. It provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    BOTL  allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    BOTL has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    BOTL has a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    BOTL is Public Domain.


CONFIGURATION

::

    $ botl cfg 
    channel=#botl commands=True nick=botl port=6667 server=localhost

    irc

    $ botl cfg server=<server>
    $ botl cfg channel=<channel>
    $ botl cfg nick=<nick>

    sasl

    $ botl pwd <nsvnick> <nspass>
    $ botl cfg password=<frompwd>

    rss

    $ botl rss <url>
    $ botl dpl <url> <item1,item2>
    $ botl rem <url>
    $ botl nme <url> <name>


USAGE

::

    without any argument the program does nothing

    $ botl
    $

    see list of commands

    $ botl cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ botl mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ botl -c

    use mod=<name1,name2> to load additional modules

    $ botl -c mod=irc,rss
    >

    use -v for verbose

    $ botl -cv mod=irc
    BOTL started CV started Sat Dec 2 17:53:24 2023
    >


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    thr - show the running threads

SYSTEMD

::

    save the following it in /etc/systemd/system/botl.service and
    replace "<user>" with the user running pipx

    [Unit]
    Description=bot library
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.botl
    ExecStart=/home/<user>/.local/pipx/venvs/botl/bin/botld
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

    then run this

    $ mkdir ~/.botl
    $ sudo systemctl enable botl --now

    default channel/server is #botl on localhost

FILES

::

    ~/.botl
    ~/.local/bin/botl
    ~/.local/bin/botld
    ~/.local/pipx/venvs/botl/

AUTHOR

::

    Bart Thate <bthate@dds.nl>

COPYRIGHT

::

    BOTL is Public Domain.
