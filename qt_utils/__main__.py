from qt_utils.designer import install_plugin_files
import os

install_plugin_files(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'qt_utils_designer_plugin.py'))
