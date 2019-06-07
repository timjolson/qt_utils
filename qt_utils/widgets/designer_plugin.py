from qt_utils.widgets import QVLine, QHLine
from qt_utils.designer import WidgetPluginFactory


QVLinePlugin = WidgetPluginFactory(
    QVLine, toolTip='Vertical Line', isContainer=False)
QHLinePlugin = WidgetPluginFactory(
    QHLine, toolTip='Horizontal Line', isContainer=False)

# import submodule plugins
from qt_utils.verticallabelwidget.verticallabelwidget_plugin import QVLabelPlugin

