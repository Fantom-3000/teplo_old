from PyQt5 import QtWidgets, QtCore, QtGui
import sys

def btn_raschet_clk():
    v1 = float(edit_v1.text())
    v2 = float(edit_v2.text())
    t1 = float(edit_t1.text())
    t2 = float(edit_t2.text())
    w = float(edit_w1.text())

    v3 = v1 + v2 # 
    t = (t1 * v1 + t2 * v2) / (v1 + v2) #
    t3 = t1 - t # 
    w1 = 0.00117 * v3 * (t1 - t) / w
    

    label_v4.setText(str(v3))
    label_r1.setText('Температура воды уменьшится на ' + str(t3) + ' градусов')
    label_r2.setText('и будет равна ' + str(t) + ' градуса')
    label_w3.setText(str(60 * w1) + ' минут и будет затрачено ' + str(w*w1) + ' кВт')
    

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.resize(500, 300)
window.setWindowTitle('Калькулятор смешения горячей и холодной воды')

hbox_1 = QtWidgets.QHBoxLayout()
hbox_2 = QtWidgets.QHBoxLayout()

vbox_1 = QtWidgets.QVBoxLayout()
vbox_2 = QtWidgets.QVBoxLayout()

label_t1 = QtWidgets.QLabel('Температура горячей воды - t1')
label_t2 = QtWidgets.QLabel('Температура холодной воды - t2')

label_v1 = QtWidgets.QLabel('Объем горячей воды - V1')
label_v2 = QtWidgets.QLabel('Объем холодной воды')
label_v3 = QtWidgets.QLabel('Общий объем воды:')
label_v4 = QtWidgets.QLabel('0')
label_w1 = QtWidgets.QLabel('Мощность ТЭНа, кВт')
label_w2 = QtWidgets.QLabel('Для подогрева воды до необходимой темературы необходимо')
label_w3 = QtWidgets.QLabel()
label_f1 = QtWidgets.QLabel('Формула расчета:')
label_f2 = QtWidgets.QLabel('t = (t1 * V1 + t2 * V2) / (V1 + V2)')
label_r1 = QtWidgets.QLabel('Температура воды уменьшится на ... градусов')
label_r2 = QtWidgets.QLabel('и будет равна ... градуса')

edit_t1 = QtWidgets.QLineEdit('60')
edit_t2 = QtWidgets.QLineEdit('15')
edit_v1 = QtWidgets.QLineEdit('70')
edit_v2 = QtWidgets.QLineEdit('10')
edit_w1 = QtWidgets.QLineEdit('1.5')

btn_raschet = QtWidgets.QPushButton('Расчитать')

vbox_1.addWidget(label_t1)
vbox_1.addWidget(edit_t1)
vbox_1.addWidget(label_v1)
vbox_1.addWidget(edit_v1)
vbox_1.addWidget(label_t2)
vbox_1.addWidget(edit_t2)
vbox_1.addWidget(label_v2)
vbox_1.addWidget(edit_v2)
vbox_1.addWidget(label_w1)
vbox_1.addWidget(edit_w1)
vbox_1.addWidget(btn_raschet)

vbox_2.addWidget(label_v3)
vbox_2.addWidget(label_v4)
vbox_2.addWidget(label_f1)
vbox_2.addWidget(label_f2)
vbox_2.addWidget(label_r1)
vbox_2.addWidget(label_r2)
vbox_2.addWidget(label_w2)
vbox_2.addWidget(label_w3)

hbox_1.addLayout(vbox_1)
hbox_1.addLayout(vbox_2)

window.setLayout(hbox_1)
window.show()

btn_raschet.clicked.connect(btn_raschet_clk)

sys.exit(app.exec_())