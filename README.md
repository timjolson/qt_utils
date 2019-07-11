# qt_utils
PyQt5 utils, QtDesigner Plugin utils and examples

Installation

    git clone https://github.com/timjolson/qt_utils.git  # clone repo
    pip3 install qt_utils  # install (use -e if you want to edit/develop)
    sudo python3 -m qt_utils  # install plugin file for QtDesigner


Submodules

    utils  # functions, etc.
        loggableQtName  # property to add to QWidgets, getter returns string 'WidgetClass:ObjectName:'
        eventMatchesButtons  # test if a mouse/keyboard event matches a set of buttons
        eventIncludesButtons  # test if a mouse/keyboard event contains a set of buttons
        eventExcludesButtons  # test if a moust/keyboard event DOES NOT contain a set of buttons
        getCurrentColor  # get widget's color, area selection by QPalette.ColorRole or getattr(QPalette, str)
    
    colors  # color related functions
        colorList  # list of color tuples [[name1, ..., nameN], hexstring, (r,g,b)]
        hex_to_rgb  # convert hex string to (r,g,b)
        rgb_to_hex  # convert (r,g,b) to hex string
        findColor  # provide color (r,g,b)/#FFFFFF/name, get full color tuple from colorList
        tuple_distance  # calculate euclidean distance between tuples
        
    widgets  # collection of widgets
    qt_utils_designer_plugin.py  # plugin script for qtDesigner (install to system default with 'sudo python3 qt_utils')


Widgets in qt_utils.widgets

    VerticalLabel  # QLabel with rotated text
    CollapsibleGroupBox  # QGroupbox that collapses when unchecked
    DictComboBox  # QComboBox that accepts a dict's or kwargs to assign userData to items
    
    VerticalLine, HorizontalLine  # QFrame adjusted to match QtDesigner's line widgets
    VerticalTitleBar, HorizontalTitleBar  # QWidget with QLabel and indicator arrow, clickable
    VCollapsibleDock, HCollapsibleDock  # QDockWidget, custom clickable title bar, collapses/expands


Subpackages

    designer  # qtDesigner helpers and examples
        import_help  # string describing ways to import .ui with python
        WidgetPluginFactory  # factory function, returns a qtDesigner plugin class for integration
        install_plugin_files  # copy files to qtDesigner plugin directory (need permissions)
        compile_ui_file  # compile .ui files into .py
        get_designer_plugin_directory  # get string path to qtDesigner plugin directory
        *sample.ui  # example .ui using example widgets and plugins
        *sample_plugin.py  # example plugin classes for qtDesigner integration
        *sample_widgets.py  # example widgets for qtDesigner integration
            

*Plugin examples adapted from  https://doc.qt.io/archives/qq/qq26-pyqtdesigner.html
