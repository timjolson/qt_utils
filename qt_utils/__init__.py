from qt_utils.colors import findColor
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import pyqtSignal

#TODO: make pytests for this module

@property
def loggableQtName(self):
    """Property to identify instance when logging or when searching in Qt for this widget.
    See objectName for Qt Objects.

    :return: string, f"{type(self).__name__}:{self.objectName()}"
        e.g. 'DraggableWidget:objectName'
    """
    return f"{type(self).__name__}:{self.objectName()}"


class ErrorMixin():
    hasError = pyqtSignal(object)
    errorChanged = pyqtSignal(object)
    errorCleared = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._error = None

    @classmethod
    def popArgs(cls, kwargs):
        """Pop out kwargs for __init__.

        :param kwargs: dict to remove arguments from
        :return: dict of args to pass to __init__
        """
        args = {}
        for k, v in cls.defaultArgs.items():
            args[k] = kwargs.pop(k, cls.defaultArgs[k])
        return args

    def getError(self):
        """Get object's error status.
        :return: any, error status
        """
        return self._error

    def setError(self, status):
        """Set object's error status.
        status != old_status -> emits errorChanged(status)
        bool(status)==True -> error ; emit hasError(status)
        bool(status)==False -> no error ; emit errorCleared

        :param status: any
        :return:
        """
        b = bool(status)

        if status != self._error:
            self._error = status
            self.errorChanged.emit(status)

            if status in [None, False]:
                self.errorCleared.emit()

        if b is True:
            self.hasError.emit(status)

    def clearError(self):
        """Reset error status to None
        :return:
        """
        self._error = None

    error = property(getError, setError, clearError)

    def errorCheck(self, *args, **kwargs):
        """Check whether object is in an error state.
        Does NOT update the object's error state.
        Override recommended.

        :return: bool
        """
        return bool(self._error)


def eventIncludesButtons(event, buttons):
    """Checks event for including buttons. Event must have all buttons/keys in buttons.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to, or int of Qt buttons
    :return: bool, True if all buttons are in event
    """
    stat = int(0)
    if isinstance(event, int):
        stat = int(event)
    else:
        if hasattr(event, 'buttons'):
            stat += int(event.buttons())
        elif hasattr(event, 'button'):
            stat += int(event.button())
        if hasattr(event, 'modifiers'):
            stat += int(event.modifiers())
    check = sum(buttons) if hasattr(buttons, '__iter__') else buttons
    return (stat & check) == check


def eventExcludesButtons(event, buttons):
    """Checks event for NOT having buttons. Event must NOT have all buttons/keys in buttons.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to, or int of Qt buttons
    :return: bool, True if all buttons are NOT in event
    """
    stat = int(0)
    if isinstance(event, int):
        stat = int(event)
    else:
        if hasattr(event, 'buttons'):
            stat += int(event.buttons())
        elif hasattr(event, 'button'):
            stat += int(event.button())
        if hasattr(event, 'modifiers'):
            stat += int(event.modifiers())
    check = sum(buttons) if hasattr(buttons, '__iter__') else buttons
    return (stat & check) == 0


def eventMatchesButtons(event, buttons):
    """Checks event for buttons. Event must have all buttons/keys in buttons, and no others.

    :param event: QEvent having .buttons(), .button(), and/or .modifiers()
    :param buttons: iterable of buttons/keys to compare to, or int of Qt buttons
    :return: bool, True if all buttons are in event, with no extra buttons or keys.
            False otherwise
    """
    stat = int(0)
    if isinstance(event, int):
        stat = int(event)
    else:
        if hasattr(event, 'buttons'):
            stat += int(event.buttons())
        elif hasattr(event, 'button'):
            stat += int(event.button())
        if hasattr(event, 'modifiers'):
            stat += int(event.modifiers())
    check = sum(buttons) if hasattr(buttons, '__iter__') else buttons
    return check == stat


def getCurrentColor(widget, color='Window'):
    """Returns the 'color' portion of 'widget's QPalette.

    :param widget: widget to get color from
    :param color: str or QPalette.ColorRole, portion of widget to get color from
        e.g. 'Window' or 'WindowText' or QtGui.QPalette.Background or QtGui.QPalette.Foreground
    :return: ( [possible color name strings], hex string, (r,g,b) )
    """
    if isinstance(color, str):
        return findColor(widget.palette().color(QPalette.__getattribute__(QPalette, color)).name()) or \
               findColor(widget.palette().color(QPalette.__getattribute__(QPalette, color)))
    elif isinstance(color, QPalette.ColorRole):
        return findColor(widget.palette().color(color).name())
    else:
        raise TypeError
