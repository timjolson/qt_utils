import pytest
import sys

# test helpers
from generalUtils.helpers_for_tests import *
from generalUtils.helpers_for_qt_tests import *
from entryWidget.helpers import *

# color helpers
from generalUtils.qt_utils import getCurrentColor

# class to test
from entryWidget import AutoColorLineEdit

# Qt stuff
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

# logging stuff
import logging

# logging.basicConfig(stream=sys.stdout, filename='/logs/AutoColorLineEdit.log', level=logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = QApplication(sys.argv)


def test_setAutoColors(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    widget.setAutoColors(test_color_dict_good)

# check colors when blank, enabled
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  test_color_dict_good['blank'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] ==  test_color_dict_good['blank'][1]
# with error
    widget.setError(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error'][1]
# error & readonly
    widget.setReadOnly(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# readonly
    widget.setError(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['readonly'][1]
# regular
    widget.setReadOnly(False)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['blank'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['blank'][1]


# check colors when blank, disabled
    widget.setEnabled(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] ==  test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] ==  test_color_dict_good['disabled'][1]
# with error
    widget.setError(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# error & readonly
    widget.setReadOnly(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# readonly
    widget.setError(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['disabled'][1]
# regular
    widget.setReadOnly(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['disabled'][1]



    widget.setReadOnly(False)
    widget.setEnabled(True)
    qtbot.keyClick(widget._editBox, 'a')
# check colors when not blank, enabled
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['default'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['default'][1]
# with error
    widget.setError(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error'][1]
# error & readonly
    widget.setReadOnly(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# readonly
    widget.setError(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['readonly'][1]
# regular
    widget.setReadOnly(False)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['default'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['default'][1]


# check colors when not blank, disabled
    widget.setEnabled(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['disabled'][1]
# with error
    widget.setError(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# error & readonly
    widget.setReadOnly(True)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict_good['error-readonly'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['error-readonly'][1]
# readonly
    widget.setError(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['disabled'][1]
# regular
    widget.setReadOnly(False)
    assert getCurrentColor(widget._editBox, 'Window')[1] == test_color_dict_good['disabled'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict_good['disabled'][1]


# check auto colors after manual colors
    widget = AutoColorLineEdit()
    show(locals())
    widget.setColors(test_color_tuple)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_tuple[0]
    assert widget._manualColors is True
    widget.setAutoColors()
    assert widget._manualColors is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict['blank'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict['blank'][1]
    qtbot.keyClick(widget._editBox, 'a')
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_dict['default'][0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_dict['default'][1]

    with pytest.raises(AssertionError):
        widget.setAutoColors(test_color_tuple)
    with pytest.raises(AssertionError):
        widget.setAutoColors(test_color_dict_bad)


def test_setText(qtbot):
    widget = AutoColorLineEdit()
    widget.setText(test_strings[1])
    show(locals())
    assert widget.text() == test_strings[1]


def test_setReadOnly(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    widget.setReadOnly(True)
    assert widget.isReadOnly() is True

    widget = AutoColorLineEdit()
    show(locals())
    widget.setReadOnly(False)
    assert widget.isReadOnly() is False


def test_setColors(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    assert widget._manualColors is False

    widget.setColors(test_color_tuple)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_tuple[0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_tuple[1]
    assert widget._manualColors is True

    widget.setColors(test_color_tuple_good)
    assert getCurrentColor(widget._editBox, 'Window')[0][0] == test_color_tuple_good[0]
    assert getCurrentColor(widget._editBox, 'WindowText')[0][0] == test_color_tuple_good[1]
    assert widget._manualColors is True

    with pytest.raises(AssertionError):
        widget.setColors(test_color_tuple_bad)

def test_setOnTextChanged(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    widget.setOnTextChanged(change_title_on_typing)

    qtbot.keyClick(widget._editBox, 'a')
    assert widget.text() == 'a'
    assert widget.windowTitle() == 'a'

    qtbot.keyClick(widget._editBox, 'b')
    assert widget.text() == 'ab'
    assert widget.windowTitle() == 'ab'

    widget.setText(test_strings[0])
    assert widget.text() == test_strings[0]
    assert widget.windowTitle() == test_strings[0]


def test_setOnEditingFinished(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    widget.setOnEditingFinished(change_title_on_typing)

    qtbot.keyClick(widget._editBox, 'a')
    assert widget.text() == 'a'
    assert widget.windowTitle() == ''
    qtbot.keyClick(widget._editBox, 'b')
    assert widget.text() == 'ab'
    assert widget.windowTitle() == ''

    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Return)
    assert widget.text() == 'ab'
    assert widget.windowTitle() == 'ab'

    widget.setText(test_strings[0])
    assert widget.text() == test_strings[0]
    assert widget.windowTitle() == test_strings[0]


def test_setError(qtbot):
    widget = AutoColorLineEdit()
    show(locals())
    widget.setError(True)
    assert widget.getError() and widget.hasError() is True and widget.isError() is True
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    widget.setError(False)
    assert widget.getError() is False and widget.hasError() is False and widget.isError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['blank'][0]

    widget.setError(True)
    assert widget.getError() and widget.hasError() is True and widget.isError() is True
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    widget.setError(False)
    assert widget.getError() is False and widget.hasError() is False and widget.isError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['blank'][0]

def test_setIsError(qtbot):
    widget = AutoColorLineEdit()
    widget.setIsError(check_error_typed)
    show(locals())

    qtbot.keyClicks(widget._editBox, 'error')
    assert widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Backspace)
    assert widget.getError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]

    widget.setText('')
    widget.setLiveErrorChecking(False)
    qtbot.keyClicks(widget._editBox, 'error')
    assert widget.getError() is False and widget.hasError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Return)
    assert widget.hasError()
    assert widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Backspace)
    assert widget.hasError() and widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    assert widget.hasError() and widget.getError()
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Return)
    assert widget.getError() is False and widget.hasError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]


def test_setOnError(qtbot):
    widget = AutoColorLineEdit()
    widget.setOnError(set_title_on_error)
    show(locals())

    assert widget.getError() is False
    widget.setError(False)
    assert widget.getError() is False
    widget.setError(True)
    assert widget.windowTitle() == 'ERROR'


def test_liveErrorChecking(qtbot):
    widget = AutoColorLineEdit()
    widget.setLiveErrorChecking(False)
    widget.setIsError(check_error_typed)
    show(locals())

    qtbot.keyClicks(widget._editBox, 'error')
    assert widget.getError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Return)
    assert widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Backspace)
    assert widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Return)
    assert widget.getError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]

    widget = AutoColorLineEdit()
    widget.setLiveErrorChecking(True)
    widget.setIsError(check_error_typed)
    show(locals())
    qtbot.keyClicks(widget._editBox, 'error')
    assert widget.getError()
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['error'][0]
    qtbot.keyPress(widget._editBox, QtCore.Qt.Key_Backspace)
    assert widget.getError() is False
    assert getCurrentColor(widget._editBox, 'Window')[0][0] ==  widget.defaultColors['default'][0]

