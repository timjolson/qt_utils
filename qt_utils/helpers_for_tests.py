from types import FunctionType
from .colors import colorList


def show(vars):
    """Help function to finish off tests, pass 'locals()' """
    qtbot, widget = vars['qtbot'], vars['widget']
    widget.show()
    qtbot.addWidget(widget)
    qtbot.waitExposed(widget)


def check_error_typed(widget, *args, **kwargs):
    """Returns 'ERROR' if widget.text() == 'error', False otherwise"""
    if widget.text() == 'error':
        widget.logger.debug('check_error_typed: '+'ERROR')
        return 'ERROR'
    widget.logger.debug('check_error_typed: ' + 'False')
    return False


def change_title_on_typing(widget):
    """Sets widget.window().setWindowTitle() to change window title to widget.text()"""
    widget.logger.debug('change title to: ' + widget.text())
    widget.window().setWindowTitle(widget.text())


def change_color_on_option(widget, *args, **kwargs):
    """Uses widget.setColors() to change QLineEdit colors to (widget.getSelected(), 'black')"""
    widget.logger.debug('change_color')
    widget.setColors((widget.getSelected(), 'black'))


def set_title_on_error(widget, *args, **kwargs):
    """Set window title to 'ERROR'"""
    widget.window().setWindowTitle('ERROR')


def do_whats_typed(widget, *args, **kwargs):
    """Performs an action on widget, depending on widget.text().
    'error': widget.setError(True)
    'fixed': widget.setReadOnly(True)
    'disabled': widget.setEnabled(False)
    'close': widget.window().close()
    'auto': widget.setAutoColors()
    'color': widget.setColors(('pink', 'black'))

    Otherwise:
        Provide a color name string (e.g. 'red' OR 'blue')
            widget.setColors((widget.text(), 'black'))
        No action specified for widget.text()
            pass
    """
    widget.logger.debug('do_whats_typed')
    do = {
        'error': (lambda x: widget.setError(True)),
        'fixed': (lambda x: widget.setReadOnly(True)),
        'disabled': (lambda x: widget.setEnabled(False)),
        'close': (lambda x: widget.window().close()),
        'auto': (lambda x: widget.setAutoColors()),
        'color': (lambda x: widget.setColors(('pink', 'black')))
    }
    if widget.text() in do.keys():
        do[widget.text()](widget)
    elif not widget.text() in do.keys() and widget.text().upper() in [i for c in colorList for i in c[0]]:
        widget.setColors((widget.text(), 'black'))
    else:
        pass


__all__ = [k for k, v in locals().items() if isinstance(v, (dict, tuple, list, FunctionType))]
