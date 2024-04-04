# This file is placed in the Public Domain.
#
# pylint: disable=C.R,W0105


"repeater"


from .timer  import Timer
from .thread import launch


class Repeater(Timer):

    "Repeater"

    def run(self):
        launch(self.start)
        super().run()


"interface"


def __dir__():
    return (
        'Repeater',
    )


__all__ = __dir__()
