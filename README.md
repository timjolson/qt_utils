# qt_utils
PyQt5 utils, QtDesigner Plugin utils and examples

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
            

*Plugin examples adapted from
https://doc.qt.io/archives/qq/qq26-pyqtdesigner.html
