from PyQt5.QtDesigner import QExtensionFactory, \
    QPyDesignerTaskMenuExtension, QDesignerFormWindowInterface
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QAction, QDialog, QGridLayout, QDialogButtonBox
from PyQt5.QtGui import QPixmap
from qt_utils.designer import WidgetPluginFactory
from qt_utils.designer.sample_widgets import GeoLocationWidget, GlobeWidget


# Define the image used for the icon.
_logo_32x32_xpm = [
    "32 32 118 2",
    "AB c #010101", "AD c #030303", "AE c #040404", "AH c #070707",
    "AI c #080808", "AJ c #090909", "AN c #0d0d0d", "AO c #0e0e0e",
    "AP c #0f0f0f", "AQ c #101010", "AR c #111111", "AS c #121212",
    "AT c #131313", "AU c #141414", "AV c #151515", "AX c #171717",
    "AY c #181818", "AZ c #191919", "BA c #1a1a1a", "BB c #1b1b1b",
    "BC c #1c1c1c", "BD c #1d1d1d", "BE c #1e1e1e", "BF c #1f1f1f",
    "BK c #242424", "BL c #252525", "BM c #262626", "BN c #272727",
    "BO c #282828", "BU c #2e2e2e", "BW c #303030", "BX c #313131",
    "BZ c #333333", "CF c #393939", "CI c #3c3c3c", "CK c #3e3e3e",
    "CL c #3f3f3f", "CM c #404040", "CN c #414141", "CO c #424242",
    "CP c #434343", "CR c #454545", "DG c #545454", "DH c #555555",
    "DI c #565656", "DJ c #575757", "DK c #585858", "DN c #5b5b5b",
    "DO c #5c5c5c", "DP c #5d5d5d", "DQ c #5e5e5e", "DR c #5f5f5f",
    "DS c #606060", "DT c #616161", "DU c #626262", "DY c #666666",
    "EA c #686868", "ED c #6b6b6b", "EE c #6c6c6c", "EI c #707070",
    "EL c #737373", "EQ c #787878", "ET c #7b7b7b", "EU c #7c7c7c",
    "FA c #828282", "FB c #838383", "FD c #858585", "FF c #878787",
    "FG c #888888", "FI c #8a8a8a", "FK c #8c8c8c", "FL c #8d8d8d",
    "FO c #909090", "FS c #949494", "FY c #9a9a9a", "FZ c #9b9b9b",
    "GB c #9d9d9d", "GC c #9e9e9e", "GF c #a1a1a1", "GH c #a3a3a3",
    "GR c #adadad", "GU c #b0b0b0", "GV c #b1b1b1", "GY c #b4b4b4",
    "GZ c #b5b5b5", "HB c #b7b7b7", "HC c #b8b8b8", "HE c #bababa",
    "HL c #c1c1c1", "HO c #c4c4c4", "HP c #c5c5c5", "HU c #cacaca",
    "HY c #cecece", "HZ c #cfcfcf", "IB c #d1d1d1", "IC c #d2d2d2",
    "ID c #d3d3d3", "IE c #d4d4d4", "IG c #d6d6d6", "IH c #d7d7d7",
    "II c #d8d8d8", "IJ c #d9d9d9", "IK c #dadada", "IL c #dbdbdb",
    "IM c #dcdcdc", "IO c #dedede", "IS c #e2e2e2", "JB c #ebebeb",
    "JC c #ececec", "JD c #ededed", "JE c #eeeeee", "JF c #efefef",
    "JH c #f1f1f1", "JP c #f9f9f9", "JR c #fbfbfb", "JT c #fdfdfd",
    "JU c #fefefe", "JV c #ffffff",
    "JVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJVJVJVJVJVIMFDCMBLBLCNFFIOJVJVJVJVJVJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJVJVJDDOANABADAJAZAZAJADABAODPJFJVJVJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJRDUADBEDSBDHEJVJVJVJVHCBCDTBDADDYJTJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVIKAVARGZHZBEILJVJVJVJVJVJVIIBFICGYAQAYIOJVJVJVJVJVJV",
    "JVJVJVJVJVHUAHCRJRJRBUHEJVJVJVJVJVJVJVJVHBBXJRJRCOAIHYJVJVJVJVJV",
    "JVJVJVJVIKAHDUJVJVFYDKJVJVJVJVJVJVJVJVJVJVDIGBJVJVDQAIIOJVJVJVJV",
    "JVJVJVJRAVCRJVJVJTBLIIJBHLGFFKFAFAFKGFHLJCIEBNJTJVJVCMAYJTJVJVJV",
    "JVJVJVDUARJRJVJTFKBBBKAOCFDOEDEQEUELDQCLAUBLAZFOJTJVJPAPEAJVJVJV",
    "JVJVJDADGZJRFYBKBADGIJJUJVJVJVJVJVJVJVJVJUILDIBBBMFZJRGUADJFJVJV",
    "JVJVDOBEHZBUDHHZBKIMJVJVJVJVJVJVJVJVJVJVJVJVIJBMIGDJBWIBBCDRJVJV",
    "JVJVANDSBDGVJVJBAUJUJVJVJVJVJVJVJVJVJVJVJVJVJUATJEJVHCBEDQAPJVJV",
    "JVIMABAZIDJVJVHLCLJVJVJVJVJVJVJVJVJVJVJVJVJVJVCIHOJVJVIJBCABISJV",
    "JVFDADGVJVJVJVGFDQJVJVJVJVJVJVJVJVJVJVJVJVJVJVDOGHJVJVJVHBADFGJV",
    "JVCMAIJUJVJVJVFKELJVJVJVJVJVJVJVJVJVJVJVJVJVJVEIFLJVJVJVJVAICPJV",
    "JVBLAXJVJVJVJVFAEUJVJVJVJVJVJVJVJVJVJVJVJVJVJVETFBJVJVJVJVAZBMJV",
    "JVBLAZJVJVJVJVFAEUJVJVJVJVJVJVJVJVJVJVJVJVJVJVETFBJVJVJVJVAZBMJV",
    "JVCNAJJVJVJVJVFKELJVJVJVJVJVJVJVJVJVJVJVJVJVJVEIFLJVJVJVJUAICPJV",
    "JVFFADHCJVJVJVGFDQJVJVJVJVJVJVJVJVJVJVJVJVJVJVDNGHJVJVJVGZADFIJV",
    "JVIOABBCIIJVJVHLCLJVJVJVJVJVJVJVJVJVJVJVJVJVJVCIHPJVJVIHBCABISJV",
    "JVJVAODTBFHBJVJCAUJUJVJVJVJVJVJVJVJVJVJVJVJVJUASJEJVGZBFDSAPJVJV",
    "JVJVDPBDICBXDIIEBLILJVJVJVJVJVJVJVJVJVJVJVJVIJBNICDGBZIEBBDTJVJV",
    "JVJVJFADGYJRGBBNAZDIIJJUJVJVJVJVJVJVJVJVJUIJDGBABOGCJRGRAEJHJVJV",
    "JVJVJVDYAQJRJVJTFOBBBMATCIDOEIETETEIDNCIATBNBAFSJTJVJPAOEEJVJVJV",
    "JVJVJVJTAYCOJVJVJTBMIGJEHOGHFLFBFBFLGHHPJEICBOJTJVJVCKBAJTJVJVJV",
    "JVJVJVJVIOAIDQJVJVFZDJJVJVJVJVJVJVJVJVJVJVDGGCJVJVDOAIISJVJVJVJV",
    "JVJVJVJVJVHYAICNJRJRBWHCJVJVJVJVJVJVJVJVGZBZJRJPCKAIHZJVJVJVJVJV",
    "JVJVJVJVJVJVIOAYAPGUIBBEIJJVJVJVJVJVJVIHBFIEGRAOBAISJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJTEAADBCDQBCHBJVJVJVJUGZBCDSBBAEEEJTJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJVJVJFDRAPABADAIAZAZAIADABAPDTJHJVJVJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJVJVJVJVJVISFGCPBMBMCPFIISJVJVJVJVJVJVJVJVJVJVJVJV",
    "JVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJVJV"]


_logo = QPixmap(_logo_32x32_xpm)

GlobePlugin = WidgetPluginFactory(
    GlobeWidget, toolTip='Sphere of points with a highlighted location',
    icon=_logo, isContainer=False)


# TaskMenuExtension needs more work, does not seem to function in qtdesigner (may work in qtcreator)
class GeoLocationTaskMenuFactory(QExtensionFactory):
    """GeoLocationTaskMenuFactory(QExtensionFactory)

    Provides a task menu that can be used to access an editor dialog.
    """

    def __init__(self, parent=None):

        QExtensionFactory.__init__(self, parent)

    # This standard factory function returns an object to represent a task
    # menu entry.
    def createExtension(self, obj, iid, parent):

        if iid != "com.trolltech.Qt.Designer.TaskMenu":
            return None

        # We pass the instance of the custom widget to the object representing
        # the task menu entry so that the contents of the custom widget can be
        # modified.
        if isinstance(obj, GeoLocationWidget):
            return GeoLocationMenuEntry(obj, parent)

        return None


GeoLocationPlugin = WidgetPluginFactory(
    GeoLocationWidget, taskMenuFactoryClass=GeoLocationTaskMenuFactory,
    toolTip='SpinBoxes for Latitude and Longitude', icon=_logo,
    isContainer=True)


class GeoLocationMenuEntry(QPyDesignerTaskMenuExtension):
    """GeoLocationMenuEntry(QPyDesignerTaskMenuExtension)

    Provides a task menu entry to enable details of the geographical location
    to be edited in a dialog.
    """

    def __init__(self, widget, parent):
        QPyDesignerTaskMenuExtension.__init__(self, parent)

        self.widget = widget

        # Create the action to be added to the form's existing task menu
        # and connect it to a slot in this class.
        self.editStateAction = QAction(self.tr("Update Location..."), self)
        self.connect(self.editStateAction, pyqtSignal("triggered()"),
                     self.updateLocation)

    def preferredEditAction(self):
        return self.editStateAction

    def taskActions(self):
        return [self.editStateAction]

    # The updateLocation() slot is called when the action that represents our
    # task menu entry is triggered. We open a dialog, passing the custom widget
    # as an argument.
    def updateLocation(self):
        dialog = GeoLocationDialog(self.widget)
        dialog.exec_()


class GeoLocationDialog(QDialog):
    """GeoLocationDialog(QDialog)

    Provides a dialog that is used to edit the contents of the custom widget.
    """

    def __init__(self, widget, parent=None):
        QDialog.__init__(self, parent)

        # We keep a reference to the widget in the form.
        self.widget = widget

        self.previewWidget = GeoLocationWidget()
        self.previewWidget.latitude = widget.latitude
        self.previewWidget.longitude = widget.longitude

        buttonBox = QDialogButtonBox()
        okButton = buttonBox.addButton(buttonBox.Ok)
        cancelButton = buttonBox.addButton(buttonBox.Cancel)

        self.connect(okButton, pyqtSignal("clicked()"),
                     self.updateWidget)
        self.connect(cancelButton, pyqtSignal("clicked()"),
                     self, pyqtSignal("reject()"))

        layout = QGridLayout()
        layout.addWidget(self.previewWidget, 1, 0, 1, 2)
        layout.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(layout)

        self.setWindowTitle(self.tr("Update Location"))

    # When we update the contents of the custom widget, we access its
    # properties via the QDesignerFormWindowInterface API so that Qt Designer
    # can integrate the changes we make into its undo-redo management.
    def updateWidget(self):
        formWindow = QDesignerFormWindowInterface.findFormWindow(self.widget)

        if formWindow:
            formWindow.cursor().setProperty("latitude",
                                            QVariant(self.previewWidget.latitude))
            formWindow.cursor().setProperty("longitude",
                                            QVariant(self.previewWidget.longitude))

        self.accept()
