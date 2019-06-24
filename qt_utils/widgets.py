from PyQt5 import QtWidgets, Qt, QtCore, QtGui
from qt_utils.entrywidget.entryWidget import \
    (AutoColorLineEdit, LabelLineEdit, EntryWidget, ButtonLineEdit, ButtonEntryWidget)
from qt_utils.sympyentrywidget.sympyEntryWidget import \
    (SympyAutoColorLineEdit, SympyLabelLineEdit, SympySymbolLineEdit, SympyEntryWidget)
from qt_utils.adjustablewidget.adjustableWidget import AdjustableMixin, AdjustableImage, AdjustableContainer


class HorizontalLine(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(HorizontalLine, self).__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)


class VerticalLine(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(VerticalLine, self).__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)


class VerticalLabel(QtWidgets.QLabel):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        if self.text() == '':
            self.setText('VerticalLabel')
        self._textAngle = 270

    def sizeHint(self):
        size = super().sizeHint()
        return QtCore.QSize(size.height(), size.width())

    def minimumSizeHint(self):
        size = super().minimumSizeHint()
        return QtCore.QSize(size.height(), size.width())

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        rect = self.rect()
        painter.translate(rect.center())
        painter.rotate(self._textAngle)
        rect = QtCore.QRectF(rect.x(), rect.y(), rect.height(), rect.width())
        painter.translate(-rect.center())

        txtopt = QtGui.QTextOption(self.alignment())
        painter.drawText(rect, self.text(), txtopt)
        self.drawFrame(painter)


class _TitleBarHelper(QtWidgets.QWidget):
    clicked = Qt.pyqtSignal()
    DownArrow = QtCore.Qt.DownArrow
    RightArrow = QtCore.Qt.RightArrow
    LeftArrow = QtCore.Qt.LeftArrow
    UpArrow = QtCore.Qt.UpArrow

    def __init__(self, parent=None, text=None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self._setupUi(text)

    def setArrowType(self, arrow_type):
        self.button.setArrowType(arrow_type)

    def setText(self, text):
        self.label.setText(text)

    def mousePressEvent(self, event=None):
        self._mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event=None):
        if hasattr(self, '_mouse_press_pos') and self._mouse_press_pos is not None:
            self._mouse_press_pos = None
            self.clicked.emit()


class VerticalTitleBar(_TitleBarHelper):
    def _setupUi(self, text):
        label = VerticalLabel(text or "Label Text")
        label.mousePressEvent = lambda e: self.mousePressEvent(e)
        label.mouseReleaseEvent = lambda e: self.mouseReleaseEvent(e)
        self.label = label

        button = QtWidgets.QToolButton()
        button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        arrow_type = QtCore.Qt.RightArrow
        button.setArrowType(arrow_type)
        button.setStyleSheet("QToolButton {border: none;}")
        button.clicked.connect(self.clicked.emit)
        self.button = button

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 10, 0, 0)
        layout.addWidget(self.label)
        layout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout = layout


class HorizontalTitleBar(_TitleBarHelper):
    def _setupUi(self, text):
        label = QtWidgets.QLabel(text or "Label Text")
        label.mousePressEvent = lambda e: self.mousePressEvent(e)
        label.mouseReleaseEvent = lambda e: self.mouseReleaseEvent(e)
        self.label = label

        button = QtWidgets.QToolButton()
        button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        arrow_type = QtCore.Qt.DownArrow
        button.setArrowType(arrow_type)
        button.setStyleSheet("QToolButton {border: none;}")
        button.clicked.connect(self.clicked.emit)
        self.button = button

        layout = QtWidgets.QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.setAlignment(QtCore.Qt.AlignLeft)
        self.layout = layout


class _CollapsibleDockHelper(QtWidgets.QDockWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self._collapsed = kwargs.pop('collapsed', False)
        self._inited = False  # if widget has been collapsed/expanded once
        self._collapsedSize = kwargs.pop('collapsed_size', 20)
        self._setupTitleBar()

        self._setupToggleAnimation(kwargs.pop('animationDuration', 200))

        self.windowTitleChanged.connect(self.titleBarWidget().setText)
        self.setWindowTitle(kwargs.pop('title', 'Collapsible'))

        self._configArrow(self.collapsed)

    collapsed = property(lambda s:s._collapsed, lambda s, c:s.collapse(c))
    collapsedSize = Qt.pyqtProperty(int, lambda s:s._collapsedSize, lambda s, p:s.setCollapsedSize(p))

    @QtCore.pyqtSlot()
    def toggle(self):
        self.collapse(not self.collapsed)

    @QtCore.pyqtSlot()
    def expand(self, expand=True):
        self.collapse(not expand)

    def _configAnimation(self, start, end):
        for i in range(self.toggleAnimation.animationCount()):
            anim = self.toggleAnimation.animationAt(i)
            anim.setDuration(self.animationDuration)
            anim.setStartValue(start)
            anim.setEndValue(end)

    def _doAnimation(self, checked):
        self.configArrow(checked)
        direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
        self.toggleAnimation.setDirection(direction)
        self.toggleAnimation.start()


class HCollapsibleDockWidget(_CollapsibleDockHelper):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def _setupTitleBar(self):
        title = HorizontalTitleBar(self)
        title.clicked.connect(self.toggle)
        self.setTitleBarWidget(title)

        frame = QtWidgets.QFrame(self)
        frame.setContentsMargins(0, 0, 0, 0)
        self.setWidget(frame)

    @QtCore.pyqtSlot()
    def collapse(self, collapse=True):
        if collapse == self.collapsed and self._inited is True:
            return
        elif collapse is True:
            self.configAnimation(self.size().height(), self.collapsedSize)
            self.doAnimation(collapse)
            # self.widget().setHidden(collapse)
        else:  # collapse is False:
            self.doAnimation(collapse)
            # self.widget().setHidden(collapse)
        self._collapsed = collapse
        self._inited = True

    def _configArrow(self, checked):
        arrow_type = Qt.RightArrow if checked else Qt.DownArrow
        self.titleBarWidget().setArrowType(arrow_type)

    @QtCore.pyqtSlot(int)
    def setCollapsedSize(self, px: int):
        self._collapsedSize = px
        if self.collapsed is True:
            self.setFixedHeight(px)

    def _setupToggleAnimation(self, duration):
        self.animationDuration = duration
        self.toggleAnimation = QtCore.QParallelAnimationGroup()

        toggleAnimation = self.toggleAnimation
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self.widget(), b"maximumHeight"))


class VCollapsibleDockWidget(_CollapsibleDockHelper):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.setFeatures(QtWidgets.QDockWidget.DockWidgetVerticalTitleBar)

    def _setupTitleBar(self):
        title = VerticalTitleBar(self)
        title.clicked.connect(self.toggle)
        self.setTitleBarWidget(title)

        frame = QtWidgets.QFrame(self)
        frame.setContentsMargins(0,0,0,0)
        self.setWidget(frame)

    @QtCore.pyqtSlot()
    def collapse(self, collapse=True):
        if collapse == self.collapsed and self._inited is True:
            return
        elif collapse is True:
            self.configAnimation(self.size().width(), self.collapsedSize)
            self.doAnimation(collapse)
            # self.widget().setHidden(collapse)
        else:  # collapse is False:
            self.doAnimation(collapse)
            # self.widget().setHidden(collapse)
        self._collapsed = collapse
        self._inited = True

    def _configArrow(self, checked):
        arrow_type = Qt.UpArrow if checked else Qt.RightArrow
        self.titleBarWidget().setArrowType(arrow_type)

    @QtCore.pyqtSlot(int)
    def setCollapsedSize(self, px: int):
        self._collapsedSize = px
        if self.collapsed is True:
            self.setFixedWidth(px)

    def _setupToggleAnimation(self, duration):
        self.animationDuration = duration
        self.toggleAnimation = QtCore.QParallelAnimationGroup()

        toggleAnimation = self.toggleAnimation
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumWidth"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumWidth"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self.widget(), b"maximumWidth"))


__all__ = ['HorizontalLine', 'VerticalLine', 'VerticalLabel', 'VerticalTitleBar', 'HorizontalTitleBar',
           'HCollapsibleDockWidget', 'VCollapsibleDockWidget', 'AutoColorLineEdit', 'EntryWidget',
           'LabelLineEdit', 'ButtonLineEdit', 'ButtonEntryWidget', 'SympyAutoColorLineEdit',
           'SympyEntryWidget', 'SympyLabelLineEdit', 'SympySymbolLineEdit', 'AdjustableMixin',
           'AdjustableContainer', 'AdjustableImage'
           ]