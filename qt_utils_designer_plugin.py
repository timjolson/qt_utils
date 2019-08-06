from qt_utils.designer import WidgetPluginFactory

from qt_utils.widgets import \
    (VerticalLine, HorizontalLine, VerticalLabel, VerticalTitleBar, HorizontalTitleBar,
     VCollapsibleDock, HCollapsibleDock, CollapsibleGroupBox, DictComboBox, RemoteRadioButton)

VLinePlugin = WidgetPluginFactory(
    VerticalLine, toolTip='Vertical Line', isContainer=False)
HLinePlugin = WidgetPluginFactory(
    HorizontalLine, toolTip='Horizontal Line', isContainer=False)
VLabelPlugin = WidgetPluginFactory(
    VerticalLabel, toolTip='QLabel with vertical text', isContainer=False)
VTitleBarPlugin = WidgetPluginFactory(
    VerticalTitleBar, toolTip='Clickable Vertical Title Bar', isContainer=False)
HTitleBarPlugin = WidgetPluginFactory(
    HorizontalTitleBar, toolTip='Clickable Horizontal Title Bar', isContainer=False)
DictComboBoxPlugin = WidgetPluginFactory(
    DictComboBox, toolTip='QComboBox, python usage allows dict for options with custom data', isContainer=False)
RemoteRadioButtonPlugin = WidgetPluginFactory(
    RemoteRadioButton, toolTip='RadioButton with manual exclusivity via `friend` signal', isContainer=False)

CollapsibleGroupBoxPlugin = WidgetPluginFactory(CollapsibleGroupBox, toolTip='Collapsible GroupBox')
HCollapsibleDockPlugin = WidgetPluginFactory(HCollapsibleDock, toolTip='Collapsible DockWidget Horizontal Layout')
VCollapsibleDockPlugin = WidgetPluginFactory(VCollapsibleDock, toolTip='Collapsible DockWidget Vertical Layout')
def xml(self):
    xml = f'<widget class="{self.name()}" name="{self.name()}" >' \
        f'<widget class="QFrame" name="Contents" />' \
        f'</widget>'
    return xml
HCollapsibleDockPlugin.domXml = xml
VCollapsibleDockPlugin.domXml = xml
