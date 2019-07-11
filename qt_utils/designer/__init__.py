from PyQt5 import QtGui
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
import os

__all__ = ['import_help', 'WidgetPluginFactory', 'install_plugin_files', 'compile_ui_files', 'get_designer_plugin_directory']

import_help = \
"""
Importing ui files can be done a few ways.

------------------------------------------
Method 1:
Import as class from compiled .py file

from mainwindow.mainwindow_ui import Ui_MainWindow

------------------------------------------
Method 2:
Import as class/type from .ui file

from PyQt5 import uic
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)

Ui_MainWindow.setupUi(instanceOfQtBaseClass)
OR
class MainWindow(QtBaseClass, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

------------------------------------------
Method 3:
Import as method from .ui file

from PyQt5 import uic
uic.loadUi(uiFile, someWidget)
OR
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(uiFile, self)

"""


def WidgetPluginFactory(widgetClass, widgetGroup='', taskMenuFactoryClass=None, icon='',
                        toolTip='', whatsThis='', isContainer=True):
    """
    Factory function. Creates a plugin class for qtDesigner integration.
    :param widgetClass: class, widget class
    :param widgetGroup: str, category in qtDesigner underwhich widget is listed
    :param taskMenuFactoryClass: class, extension for task menu actions (needs work)
    :param icon: str, list; str->file path becomesQIcon, list->becomes QPixmap
    :param toolTip: str, tip that appears when hovering over in qtDesigner widget list
    :param whatsThis: str, info to show for qtDesigner 'whats this?'
    :param isContainer: bool, the widget can contain other widgets
    :return: a plugin class for qtDesigner to use
    """
    class Klass(QPyDesignerCustomWidgetPlugin):
        def __init__(self, parent=None):
            """
            The __init__() method is only used to set up the plugin and define its
            initialized variable.

            Inspired by https://doc.qt.io/archives/qq/qq26-pyqtdesigner.html

            :param parent: ignored
            """
            QPyDesignerCustomWidgetPlugin.__init__(self)
            self.initialized = False

        def initialize(self, formEditor):
            """
            The initialize() and isInitialized() methods allow the plugin to set up
            any required resources, ensuring that this can only happen once for each
            plugin.
            :param formEditor: passed from qtcreator possibly
            :return:
            """

            if self.initialized:
                return

            # We register an extension factory to add an extension to each form's
            # task menu.
            manager = formEditor.extensionManager()
            if manager:
                if taskMenuFactoryClass:
                    self.factory = taskMenuFactoryClass(manager)
                    manager.registerExtensions(self.factory, __file__)

            self.initialized = True

        def isInitialized(self):
            return self.initialized

        def createWidget(self, parent):
            """
            This factory method creates new instances of our custom widget with the
            appropriate parent.
            """
            return widgetClass(parent=parent)

        def name(self):
            """
            This method returns the name of the custom widget class that is provided
            by this plugin.

            :return:
            """
            return type(self).__name__

        def group(self):
            """
            Returns the name of the group in Qt Designer's widget box that this
            widget belongs to.

            :return:
            """
            return widgetGroup or "Custom Widgets"

        def icon(self):
            """
            Returns the icon used to represent the custom widget in Qt Designer's
            widget box.

            :return:
            """
            return QtGui.QIcon(icon)

        def toolTip(self):
            """
            Returns a short description of the custom widget for use in a tool tip.

            :return:
            """
            return toolTip

        def whatsThis(self):
            """
            Returns a short description of the custom widget for use in a "What's
            This?" help message for the widget.

            :return:
            """
            return whatsThis

        def isContainer(self):
            """
            Returns True if the custom widget acts as a container for other widgets;
            otherwise returns False. Note that plugins for custom containers also
            need to provide an implementation of the QDesignerContainerExtension
            interface if they need to add custom editing support to Qt Designer.

            :return:
            """
            return isContainer

        def includeFile(self):
            """
            Returns the module containing the custom widget class. It may include
            a module path.

            :return:
            """
            return f'{widgetClass.__module__}'

        # def domXml(self):
        #     """
        #     Returns xml string of widget, preferably containing default values, etc.
        #     :return:
        #     """
        #     return "<widget class='{self.widgetClass.__name__}' name='{self.widgetClass.__name__} />"

    Klass.__name__ = widgetClass.__name__
    return Klass


def get_designer_plugin_directory():
    """
    Get directory to qtDesigner python plugin directory
    :return: str
    """
    from PyQt5.QtCore import QLibraryInfo
    info = QLibraryInfo.location(QLibraryInfo.PluginsPath)
    plugins_path = os.path.join(str(info), "designer", "python")
    return plugins_path


def install_plugin_files(files):
    """
    Copy files into qtDesigner plugin directory.
    *Extra permissions needed.
    *Prints each source and destination file.

    :param files: str or [str], file path(s) to copy to plugin directory
    :return:
    """
    plugins_path = get_designer_plugin_directory()

    if isinstance(files, str):
        files = [files]

    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)

    try:
        for plugin in files:
            path = os.path.abspath(plugin)
            directory, file_name = os.path.split(path)
            output_path = os.path.join(plugins_path, file_name)
            print("Copying", path, "to", plugins_path)
            open(output_path, "wb").write(open(path, "rb").read())
    except PermissionError:
        raise PermissionError("Run with write permissions to add widgets to qtDesigner in folder:\n\t" + \
                          plugins_path)


def compile_ui_files(files, output_files=None):
    """
    Compile .ui files into .py files.
    *Prints each source and destination file.

    Default .py files are 'ui_[ui filename minus extension].py

    :param files: str or [str], path(s) to .ui designer files
    :param output_files: str or [str], path(s) for compiled .py output files
    :return:
    """
    import PyQt5.uic

    if isinstance(files, str) and (isinstance(output_files, str) or output_files is None):
        files = [files]
        output_files = [output_files or None]
    if output_files is None:
        output_files = [None]

    for file, output in zip(files, output_files):
        path = os.path.abspath(file)
        directory, file_name = os.path.split(path)
        file_name = "ui_" + file_name.replace(".ui", os.extsep + "py")
        output_path = output or os.path.join(directory, file_name)

        print("Compiling", path, "to", output_path)
        input_file = open(path)
        output_file = open(output_path, "w")
        PyQt5.uic.compileUi(input_file, output_file)
        input_file.close()
        output_file.close()
