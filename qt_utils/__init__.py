from qt_utils.colors import findColor
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import pyqtSignal

#TODO: make pytests for this module

@property
def loggableQtName(self):
    """Property to identify instance when logging or when searching in Qt for this widget.
    See objectName for Qt Objects.

    :return: string, e.g.:
        'DraggableWidget'
        or
        'DraggableWidget:objectName'
    """
    on = self.objectName()
    return type(self).__name__ + (f":{on}" if on else "")


class ErrorMixin():
    """
    signals:
        hasError([]],[object],[str])  # emitted when bool(error status) is True
        errorChanged([],[object],[str])  # emitted when error status changes
        errorCleared  # emitted when bool(error status) is changed to False
    """
    hasError = pyqtSignal([],[object],[str])
    errorChanged = pyqtSignal([],[object],[str])
    errorCleared = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._error = None

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
            self.errorChanged[object].emit(status)
            self.errorChanged[str].emit(str(status))
            self.errorChanged.emit()

            if status in [None, False]:
                self.errorCleared.emit()

        if b is True:
            self.hasError[object].emit(status)
            self.hasError[str].emit(str(status))
            self.hasError.emit()

    def clearError(self):
        """Reset error status to None
        :return:
        """
        self.setError(None)

    error = property(getError, setError, clearError)

    def errorCheck(self, *args, **kwargs):
        """Checks whether object is in an error state.
        Does NOT update the object's error state.

        Recommend overriding to return any type of error status.

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
