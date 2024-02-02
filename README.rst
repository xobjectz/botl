python3 irc bot

BOTL is a python3 irc bot, it can connect to IRC, fetch and display RSS
feeds, take todo notes, keep a shopping list and log text. You can also
copy/paste the service file and run it under systemd for 24/7 presence
in a IRC channel.

BOTL has all the python3 code to program a unix cli program, such as
disk perisistence for configuration files, event handler to
handle the client/server connection, code to introspect modules
for commands, deferred exception handling to not crash on an
error, a parser to parse commandline options and values, etc.

BOTL provides an botl.objects module that allows for easy json save//load
to/from disk of objects. It provides an "clean namespace" Object class
that only has dunder methods, so the namespace is not cluttered with
method names. This makes storing and reading to/from json possible.

BOTL is Public Domain.

SYNOPSIS

    botl <cmd> [key=val] [key==val]
    botl [-a] [-c] [-d] [-h] [-v] 

USAGE

without any argument the program does nothing

    $ botl
    $


see list of commands

    $ botl cmd
    cmd,err,mod,req,thr,ver


list of modules

    $ botl mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr


use mod=<name1,name2> to load additional modules

    $ botl cfg mod=irc


start a console

    $ botl -c mod=irc,rss
    >


use -v for verbose

    $ botl -cv mod=irc
    BOTL started CV started Sat Dec 2 17:53:24 2023
    >


start daemon

    $ botl -d
    $ 

CONFIGURATION

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

COMMANDS

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
    req - reconsider
    rss - add a feed
    thr - show the running threads

SYSTEMD

save the following it in /etc/systems/system/botl.service and
replace "<user>" with the user running pipx

    [Unit]
    Description=python3 irc bot
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.botl
    ExecStart=/home/<user>/.local/pipx/venvs/botl/bin/botl -d
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

then run this

    $ mkdir ~/.botl
    $ sudo systemctl enable botl --now

default channel/server is #botl on localhost

FILES

    ~/.botl
    ~/.local/bin/botl
    ~/.local/pipx/venvs/botl/

AUTHOR

    Bart Thate <objx@proton.me>

COPYRIGHT

    BOTL is Public Domain.
