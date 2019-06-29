from qt_utils.designer import WidgetPluginFactory

from qt_utils.widgets import \
    (VerticalLine, HorizontalLine, VerticalLabel, VerticalTitleBar,
     HorizontalTitleBar, VCollapsibleDockWidget, HCollapsibleDockWidget)
from entryWidget import \
    AutoColorLineEdit, EntryWidget, LabelLineEdit, ButtonLineEdit, ButtonEntryWidget
from sympyEntryWidget import \
    SympyAutoColorLineEdit, SympyEntryWidget, SympyLabelLineEdit, SympySymbolLineEdit


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

HCollapsibleDockPlugin = WidgetPluginFactory(HCollapsibleDockWidget, toolTip='Collapsible DockWidget Horizontal Layout')
VCollapsibleDockPlugin = WidgetPluginFactory(VCollapsibleDockWidget, toolTip='Collapsible DockWidget Vertical Layout')
def xml(self):
    xml = f'<widget class="{self.name()}" name="{self.name()}" >' \
        f'<widget class="QFrame" name="Contents" />' \
        f'</widget>'
    return xml
HCollapsibleDockPlugin.domXml = xml
VCollapsibleDockPlugin.domXml = xml

AutoColorLineEditPlugin = WidgetPluginFactory(AutoColorLineEdit, toolTip='QLineEdit with automatic colors')
LabelLineEditPlugin = WidgetPluginFactory(LabelLineEdit, toolTip='QLabel and AutoColorLineEdit')
ButtonLabelLineEditPlugin = WidgetPluginFactory(ButtonLineEdit, toolTip='QPushButton and AutoColorLineEdit')
EntryWidgetPlugin = WidgetPluginFactory(EntryWidget, toolTip='LabelLineEdit and QComboBox')
ButtonEntryWidgetPlugin = WidgetPluginFactory(ButtonEntryWidget, toolTip='ButtonLineEdit and QComboBox')

SympyAutoColorLineEditPlugin = WidgetPluginFactory(SympyAutoColorLineEdit,
                                                   toolTip='QLineEdit with Sympy error checking and automatic colors')
SympyLabelLineEditPlugin = WidgetPluginFactory(SympyLabelLineEdit,
                                               toolTip='QLabel and SympyAutoColorLineEdit')
SympySymbolLineEditPlugin = WidgetPluginFactory(SympySymbolLineEdit,
                                                toolTip='SympyLabelLineEdit for creating sympy.Symbol')
SympyEntryWidgetPlugin = WidgetPluginFactory(SympyEntryWidget,
                                             toolTip='SympyLabelLineEdit and QComboBox for unit conversions')
