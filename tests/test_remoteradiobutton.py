# from PyQt5 import QtWidgets, Qt
# from qt_utils.widgets import RemoteRadioButton
#
# app = Qt.QApplication([])
# win = QtWidgets.QWidget()
# win.setLayout(QtWidgets.QHBoxLayout(win))
#
# root = RemoteRadioButton(win, objectName='root radio button')
# root.hide()
# b1 = RemoteRadioButton(win, objectName='b1')
# b2 = RemoteRadioButton(win, friends=b1, objectName='b2')
# b3 = RemoteRadioButton(win, friends=(b2, b1), objectName='b3')
# b4 = RemoteRadioButton(objectName='b4')
# b5 = RemoteRadioButton(objectName='b5')
# b1.add_friends(b4, b5)
# b1.add_friends(root)
#
# # For QDesigner integration, dynamic friend discovery, not recommended for programmatic use
# # b1.friends.connect(b2.add_friends)
# # b2.friends.connect(b3.add_friends)
# # b3.friends.connect(b4.add_friends)
# # b4.friends.connect(b5.add_friends)
# # b5.friends.connect(b1.add_friends)
#
# # b1.radioChanged.connect(lambda o: print('selected', o.objectName()))
# root.radioChanged.connect(lambda o: print('selected', o.objectName()))
# root.radioChanged[str].connect(lambda s: print('selected [str]', s))
# # b3.radioChanged.connect(lambda o: print('selected', o.objectName()))
#
#
# win.layout().addWidget(b1)
# win.layout().addWidget(b2)
# win.layout().addWidget(b3)
# win.layout().addWidget(b4)
# win.layout().addWidget(b5)
# win.show()
# app.exec()