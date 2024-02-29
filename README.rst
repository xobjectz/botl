BOTL
####


NAME

::

    BOTL


INSTALL

::

    $ botl install rssbot
    $ botl ensurepath


SYNOPSIS

::

    botl <cmd> [key=val] [key==val]
    botld


DESCRIPTION

::

    BOTL is a python3 bot able to display rss feeds in your channel.

    BOTL comes with a cli to configure and a daemon to run in the
    background, hooking the daemon in systemd brings a 24/7 available
    rssbot in your channel.


COMMANDS

::

    cfg - irc configuration
    cmd - commands
    dpl - sets display items
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed


CONFIGURATION

irc

::

    $ botl cfg server=<server>
    $ botl cfg channel=<channel>
    $ botl cfg nick=<nick>

sasl

::

    $ botl pwd <nsvnick> <nspass>
    $ botl cfg password=<frompwd>

rss

::

    $ botl rss <url>
    $ botl dpl <url> <item1,item2>
    $ botl rem <url>
    $ botl nme <url> <name>


SYSTEMD

save the following it in /etc/systems/system/botl.service and
replace "<user>" with the user running pipx

::

    [Unit]
    Description=BOTLE
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.botl
    ExecStart=/home/<user>/.local/pipx/venvs/rssbot/bin/botld
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target


then run this

::

    $ mkdir ~/.botl
    $ sudo systemctl enable botl --now

default channel/server is #rssbot on localhost


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
