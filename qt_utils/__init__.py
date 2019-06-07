from qt_utils.colors import findColor
from PyQt5.QtGui import QPalette

#TODO: make pytests for this module

@property
def loggableQtName(self):
    """Property to identify instance when logging or when searching in Qt for this widget.
    See objectName for Qt Objects.

    :return: string, f"{type(self).__name__}:{self.objectName()}:"
        e.g. 'DraggableWidget:objectName:'
    """
    return f"{type(self).__name__}:{self.objectName()}:"


def eventIncludesButtons(event, buttons):
    """Checks event for including buttons. Event must have all buttons/keys in buttons.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to
    :return: bool, True if all buttons are in event
    """
    stat = int(0)
    if hasattr(event, 'buttons'):
        stat += int(event.buttons())
    elif hasattr(event, 'button'):
        stat += int(event.button())
    if hasattr(event, 'modifiers'):
        stat += int(event.modifiers())
    check = sum(buttons)
    return (stat & check) == check


def eventExcludesButtons(event, buttons):
    """Checks event for NOT having buttons. Event must NOT have all buttons/keys in buttons.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to
    :return: bool, True if all buttons are NOT in event
    """
    stat = int(0)
    if hasattr(event, 'buttons'):
        stat += int(event.buttons())
    elif hasattr(event, 'button'):
        stat += int(event.button())
    if hasattr(event, 'modifiers'):
        stat += int(event.modifiers())
    check = sum(buttons)
    return (stat ^ check) == check


def eventMatchesButtons(event, buttons, excludeButtons=0):
    """Checks event for buttons. Event must have all buttons/keys in buttons, and no others.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to
    :param excludeButtons: iterable of buttons/keys to make sure are not in event
    :return: bool, True if all buttons are in event, with no extra buttons or keys.
            False otherwise
    """
    return eventIncludesButtons(event, buttons) and eventExcludesButtons(event, excludeButtons)


def getCurrentColor(widget, color='Window'):
    """Returns the 'color' portion of 'widget's QPalette.

    :param widget: widget to get color from
    :param color: str or QPalette.ColorRole, portion of widget to get color from
        e.g. 'Window' or 'WindowText' or QtGui.QPalette.Background or QtGui.QPalette.Foreground
    :return: ( [possible color name strings], hex string, (r,g,b) )
    """
    if isinstance(color, str):
        # return findColor(widget.palette().color(QPalette.__getattribute__(QPalette, color)).name())
        return findColor(widget.palette().color(QPalette.__getattribute__(QPalette, color)))
    elif isinstance(color, QPalette.ColorRole):
        return findColor(widget.palette().color(color).name())
    else:
        raise TypeError
