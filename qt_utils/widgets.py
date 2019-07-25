from PyQt5 import QtWidgets, Qt, QtCore, QtGui
import logging


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

        self.drawFrame(QtWidgets.QStylePainter(self))


class _TitleBarHelper(QtWidgets.QWidget):
    clicked = Qt.pyqtSignal([],[bool])
    DownArrow = QtCore.Qt.DownArrow
    RightArrow = QtCore.Qt.RightArrow
    LeftArrow = QtCore.Qt.LeftArrow
    UpArrow = QtCore.Qt.UpArrow

    def __init__(self, parent=None, text=None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setupUi(text)
        self._mousePressPos = None

    def setArrowType(self, arrow_type):
        self.button.setArrowType(arrow_type)

    def setText(self, text):
        self.label.setText(text)

    def text(self):
        return self.label.text()

    def mousePressEvent(self, event=None):
        self._mousePressPos = event.pos()

    def mouseReleaseEvent(self, event=None):
        if self._mousePressPos is not None:
            self._mousePressPos = None
            self.clicked[bool].emit(True)
            self.clicked.emit()


class VerticalTitleBar(_TitleBarHelper):
    def setupUi(self, text):
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
    def setupUi(self, text):
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
        self._configedAnimation = False  # if widget has been collapsed/expanded once
        self._collapsedSize = kwargs.pop('collapsedSize', 20)
        self._setupTitleBar()

        self._setupToggleAnimation(kwargs.pop('animationDuration', 200))

        self.windowTitleChanged.connect(self.titleBarWidget().setText)
        self.setWindowTitle(kwargs.pop('title', 'Collapsible'))

        self._configArrow(self.collapsed)

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
        self._configArrow(checked)
        direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
        self.toggleAnimation.setDirection(direction)
        self.toggleAnimation.start()

    def setTitle(self, title):
        self.titleBarWidget().setText(title)

    def title(self):
        return self.titleBarWidget().text()

    collapsed = Qt.pyqtProperty(bool, lambda s:s._collapsed, lambda s, c:s.collapse(c))
    collapsedSize = Qt.pyqtProperty(int, lambda s:s._collapsedSize, lambda s, p:s.setCollapsedSize(p))


class HCollapsibleDock(_CollapsibleDockHelper):
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
        if collapse == self.collapsed:
            return
        if collapse is True:
            self._configAnimation(self.size().height(), self.collapsedSize)
            self._doAnimation(collapse)
        else:  # collapse is False:
            if self._configedAnimation is False:
                self._configAnimation(self.widget().minimumSizeHint().height(), self.collapsedSize)
                self._configedAnimation = True
            self._doAnimation(collapse)
        self._collapsed = collapse

    def _configArrow(self, checked):
        arrow_type = QtCore.Qt.RightArrow if checked else QtCore.Qt.DownArrow
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


class VCollapsibleDock(_CollapsibleDockHelper):
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
        if collapse == self.collapsed:
            return
        if collapse is True:
            self._configAnimation(self.size().width(), self.collapsedSize)
            self._doAnimation(collapse)
        else:  # collapse is False:
            if self._configedAnimation is False:
                self._configAnimation(self.widget().minimumSizeHint().width(), self.collapsedSize)
                self._configedAnimation = True
            self._doAnimation(collapse)
        self._collapsed = collapse

    def _configArrow(self, checked):
        arrow_type = QtCore.Qt.UpArrow if checked else QtCore.Qt.RightArrow
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


class CollapsibleGroupBox(QtWidgets.QGroupBox):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self._collapsed = kwargs.pop('collapsed', False)
        self._inited = False  # if widget has been collapsed/expanded once
        self._collapsedSize = kwargs.pop('collapsedSize', 25)
        self._configedAnimation = False  # if widget has been collapsed/expanded once
        self._setupToggleAnimation(kwargs.pop('animationDuration', 200))
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.setCheckable(True)
        self.setChecked(True)
        self.toggled.connect(self.toggle)

    collapsed = property(lambda s:s._collapsed, lambda s, c:s.collapse(c))
    collapsedSize = Qt.pyqtProperty(int, lambda s:s._collapsedSize, lambda s, p:s.setCollapsedSize(p))

    @QtCore.pyqtSlot()
    def toggle(self):
        self.collapse(not self.collapsed)

    @QtCore.pyqtSlot()
    def expand(self, expand=True):
        self.collapse(not expand)

    @QtCore.pyqtSlot()
    def collapse(self, collapse=True):
        if collapse == self.collapsed:
            return
        if collapse is True:
            self._configAnimation(self.size().height(), self.collapsedSize)
            self._doAnimation(collapse)
        else:  # collapse is False:
            if self._configedAnimation is False:
                self._configAnimation(self.minimumSizeHint().height(), self.collapsedSize)
                self._configedAnimation = True
            self._doAnimation(collapse)
        self._collapsed = collapse

    def _configAnimation(self, start, end):
        for i in range(self.toggleAnimation.animationCount()):
            anim = self.toggleAnimation.animationAt(i)
            anim.setDuration(self.animationDuration)
            anim.setStartValue(start)
            anim.setEndValue(end)

    def _doAnimation(self, checked):
        direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
        self.toggleAnimation.setDirection(direction)
        self.toggleAnimation.start()

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
        # toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self.widget(), b"maximumHeight"))


class DictComboBox(QtWidgets.QComboBox):
    dataChanged = Qt.pyqtSignal([],[object])

    def __init__(self, parent, **kwargs):
        options = kwargs.pop('options', dict())
        QtWidgets.QComboBox.__init__(self, parent)
        self.currentIndexChanged.connect(lambda i: self.dataChanged[object].emit(self.itemData(i)))
        self.currentIndexChanged.connect(lambda i: self.dataChanged.emit())
        self.setDuplicatesEnabled(False)
        self.setAllItems(options)

    def addItems(self, textToDataDict=None, **kwargs):
        self.insertItems(self.count()-1, textToDataDict, **kwargs)

    def insertItems(self, index, textToDataDict=None, **kwargs):
        if textToDataDict is None:
            textToDataDict = kwargs
        if not isinstance(textToDataDict, dict):
            if hasattr(textToDataDict, '__iter__'):
                textToDataDict = {k: k for k in textToDataDict}

        super().insertItems(index, list(textToDataDict.keys()))
        for k, v in textToDataDict.items():
            super().setItemData(self.findText(k), v, QtCore.Qt.UserRole)

    def itemData(self, index, role=QtCore.Qt.UserRole):
        return super().itemData(index, role)

    def currentData(self, role=QtCore.Qt.UserRole):
        return super().currentData(role)

    def allItems(self):
        return {self.itemText(i):self.itemData(i) for i in range(self.count())}

    def setAllItems(self, textToDataDict=None, **kwargs):
        self.blockSignals(True)
        self.clear()
        self.insertItems(0, textToDataDict, **kwargs)
        self.setCurrentIndex(0)
        self.blockSignals(False)
        self.currentTextChanged[str].emit(self.itemText(0))
        self.currentIndexChanged.emit(0)

    def setCurrentText(self, text):
        self.blockSignals(True)
        super().setCurrentText(text)
        self.blockSignals(False)
        self.currentTextChanged[str].emit(text)
        self.currentIndexChanged[int].emit(self.currentIndex())


__all__ = ['HorizontalLine', 'VerticalLine', 'VerticalLabel', 'VerticalTitleBar', 'HorizontalTitleBar',
           'HCollapsibleDock', 'VCollapsibleDock', 'CollapsibleGroupBox', 'DictComboBox'
           ]
