'''
Калькулятор смешения горячей и холодной воды с подсчетом затрат
времени и электроэнергии на подогрев воды до установленной температуры.

Автор: Fantom-3000
'''

from PyQt5 import QtWidgets, QtCore, QtGui
import sys

def btn_raschet_clk():
    v1 = float(edit_v1.text())
    v2 = float(edit_v2.text())
    t1 = float(edit_t1.text())
    t2 = float(edit_t2.text())
    w = float(edit_w1.text())

    v3 = v1 + v2 # Вычисление общего объема воды
    t = (t1 * v1 + t2 * v2) / (v1 + v2) # Вычисление конечной температуры воды после смешения
    t3 = t1 - t # Вычисление температуры температуры воды
    w1 = 0.00117 * v3 * (t1 - t) / w # Вычисление расходы электроэнергии на подогрев воды

    label_r1.setText('Общий объем воды - ' + str('%.1f' %v3) +' литров\n\n'
                    + 'Температура воды после смешения уменьшится на ' + str('%.1f' %t3) 
                    + ' градусов и будет равна ' + str('%.1f' %t) + ' градуса\n\n'
                    + 'Для подогрева воды до установленной темературы необходимо ' 
                    + str('%.1f' %(60 * w1)) + ' минут (' + str('%.1f' %w1) + ' часа) и будет затрачено ' 
                    + str('%.3f' %(w*w1)) + ' кВт')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    font1 = QtGui.QFont('Arial', 12)
    font2 = QtGui.QFont('Arial', 11, italic=True)
    window = QtWidgets.QWidget()
    window.resize(300, 500)
    window.setWindowTitle('Калькулятор смешения горячей и холодной воды')

    hbox_1 = QtWidgets.QVBoxLayout()
    hbox_2 = QtWidgets.QHBoxLayout()
    vbox_1 = QtWidgets.QVBoxLayout()
    vbox_2 = QtWidgets.QVBoxLayout()

    edit_t1 = QtWidgets.QLineEdit('60')
    edit_t1.setFont(font1)
    edit_t2 = QtWidgets.QLineEdit('15')
    edit_t2.setFont(font1)
    edit_v1 = QtWidgets.QLineEdit('70')
    edit_v1.setFont(font1)
    edit_v2 = QtWidgets.QLineEdit('10')
    edit_v2.setFont(font1)
    edit_w1 = QtWidgets.QLineEdit('1.5')
    edit_w1.setFont(font1)

    label_t1 = QtWidgets.QLabel('Температура горячей воды')
    label_t1.setBuddy(edit_t1)
    label_t1.setFont(font1)
    label_t2 = QtWidgets.QLabel('Температура холодной воды')
    label_t2.setBuddy(edit_t1)
    label_t2.setFont(font1)
    label_v1 = QtWidgets.QLabel('Объем горячей воды, л')
    label_v1.setBuddy(edit_v1)
    label_v1.setFont(font1)
    label_v2 = QtWidgets.QLabel('Объем холодной воды, л')
    label_v2.setBuddy(edit_v2)
    label_v2.setFont(font1)
    label_w1 = QtWidgets.QLabel('Мощность ТЭНа, кВт')
    label_w1.setBuddy(edit_w1)
    label_w1.setFont(font1)
    label_r1 = QtWidgets.QLabel()
    label_r1.setWordWrap(True)
    label_r1.setFont(font2)

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
    vbox_2.addWidget(label_r1)

    hbox_1.addLayout(vbox_1)
    hbox_1.addLayout(vbox_2)

    window.setLayout(hbox_1)
    window.show()

    btn_raschet.clicked.connect(btn_raschet_clk)

    sys.exit(app.exec_())
