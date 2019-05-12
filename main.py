# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from scipy.integrate import *
import numpy as np


class Ui_Form(object):
    def __init__(self):
        self.W = QtWidgets.QDoubleSpinBox(Form)
        self.H = QtWidgets.QDoubleSpinBox(Form)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_22 = QtWidgets.QLabel(Form)
        self.dY = QtWidgets.QDoubleSpinBox(Form)
        self.mu = QtWidgets.QDoubleSpinBox(Form)
        self.label_21 = QtWidgets.QLabel(Form)
        self.dX = QtWidgets.QDoubleSpinBox(Form)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_16 = QtWidgets.QLabel(Form)
        self.M = QtWidgets.QDoubleSpinBox(Form)
        self.k4 = QtWidgets.QDoubleSpinBox(Form)
        self.label_15 = QtWidgets.QLabel(Form)
        self.m = QtWidgets.QDoubleSpinBox(Form)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_10 = QtWidgets.QLabel(Form)
        self.k3 = QtWidgets.QDoubleSpinBox(Form)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_8 = QtWidgets.QLabel(Form)
        self.k2 = QtWidgets.QDoubleSpinBox(Form)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_5 = QtWidgets.QLabel(Form)
        self.k1 = QtWidgets.QDoubleSpinBox(Form)
        self.label_4 = QtWidgets.QLabel(Form)
        self.btn_pause = QtWidgets.QPushButton(Form)
        self.btn_start = QtWidgets.QPushButton(Form)
        self.btn_hide = QtWidgets.QPushButton(Form)

        self.chartView = QtChart.QChartView(Form)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.chart = self.chartView.chart()
        self.chart.legend().setVisible(False)
        self.axisX = QtChart.QValueAxis()
        self.axisY = QtChart.QValueAxis()

        self.mass_series = QtChart.QScatterSeries()
        self.trajectory_series = QtChart.QLineSeries()
        self.box_series = QtChart.QLineSeries()
        self.s1_series = QtChart.QLineSeries()
        self.s2_series = QtChart.QLineSeries()
        self.s3_series = QtChart.QLineSeries()
        self.s4_series = QtChart.QLineSeries()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.total_time = .0

        self.runge_kutta = ode(self.f)
        self.runge_kutta.set_integrator('dopri5')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.btn_start.setGeometry(QtCore.QRect(690, 506, 100, 24))
        self.btn_start.setObjectName("btn_start")
        self.btn_pause.setGeometry(QtCore.QRect(690, 538, 100, 24))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_hide.setGeometry(QtCore.QRect(690, 570, 100, 24))
        self.btn_hide.setObjectName("btn_hide")
        self.label_4.setGeometry(QtCore.QRect(20, 508, 31, 16))
        self.label_4.setObjectName("label_4")
        self.k1.setGeometry(QtCore.QRect(50, 506, 100, 22))
        self.k1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.k1.setDecimals(2)
        self.k1.setMinimum(0.0)
        self.k1.setSingleStep(0.5)
        self.k1.setProperty("value", 9.0)
        self.k1.setObjectName("k1")
        self.chartView.setGeometry(QtCore.QRect(20, 10, 761, 491))
        self.chartView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chartView.setObjectName("graphicsView")
        self.label_5.setGeometry(QtCore.QRect(155, 508, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(155, 540, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7.setGeometry(QtCore.QRect(20, 540, 31, 16))
        self.label_7.setObjectName("label_7")
        self.k2.setGeometry(QtCore.QRect(50, 538, 100, 22))
        self.k2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.k2.setDecimals(2)
        self.k2.setMinimum(0.0)
        self.k2.setSingleStep(0.5)
        self.k2.setProperty("value", 1.0)
        self.k2.setObjectName("k2")
        self.label_8.setGeometry(QtCore.QRect(155, 572, 31, 16))
        self.label_8.setObjectName("label_8")
        self.label_9.setGeometry(QtCore.QRect(20, 572, 31, 16))
        self.label_9.setObjectName("label_9")
        self.k3.setGeometry(QtCore.QRect(50, 570, 100, 22))
        self.k3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.k3.setDecimals(2)
        self.k3.setMinimum(0.0)
        self.k3.setSingleStep(0.5)
        self.k3.setProperty("value", 5.0)
        self.k3.setObjectName("k3")
        self.label_10.setGeometry(QtCore.QRect(335, 508, 31, 16))
        self.label_10.setObjectName("label_10")
        self.label_11.setGeometry(QtCore.QRect(335, 540, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12.setGeometry(QtCore.QRect(200, 540, 31, 16))
        self.label_12.setObjectName("label_12")
        self.label_13.setGeometry(QtCore.QRect(200, 572, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14.setGeometry(QtCore.QRect(200, 508, 31, 16))
        self.label_14.setObjectName("label_14")
        self.m.setGeometry(QtCore.QRect(230, 538, 100, 22))
        self.m.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.m.setDecimals(0)
        self.m.setMinimum(1.0)
        self.m.setMaximum(100000.0)
        self.m.setProperty("value", 300.0)
        self.m.setObjectName("m")
        self.label_15.setGeometry(QtCore.QRect(335, 572, 31, 16))
        self.label_15.setObjectName("label_15")
        self.k4.setGeometry(QtCore.QRect(230, 506, 100, 22))
        self.k4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.k4.setDecimals(2)
        self.k4.setMinimum(0.0)
        self.k4.setSingleStep(0.5)
        self.k4.setProperty("value", 7.0)
        self.k4.setObjectName("k4")
        self.M.setGeometry(QtCore.QRect(230, 570, 100, 22))
        self.M.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.M.setDecimals(0)
        self.M.setMinimum(1.0)
        self.M.setMaximum(100000.0)
        self.M.setProperty("value", 800.0)
        self.M.setObjectName("M")
        self.label_16.setGeometry(QtCore.QRect(515, 508, 31, 16))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17.setGeometry(QtCore.QRect(515, 540, 31, 16))
        self.label_17.setObjectName("label_17")
        self.label_18.setGeometry(QtCore.QRect(380, 540, 31, 16))
        self.label_18.setObjectName("label_18")
        self.label_19.setGeometry(QtCore.QRect(380, 572, 31, 16))
        self.label_19.setObjectName("label_19")
        self.label_20.setGeometry(QtCore.QRect(380, 508, 31, 16))
        self.label_20.setObjectName("label_20")
        self.dX.setGeometry(QtCore.QRect(410, 538, 100, 22))
        self.dX.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.dX.setDecimals(0)
        self.dX.setMinimum(-100.0)
        self.dX.setMaximum(100.0)
        self.dX.setProperty("value", 3.0)
        self.dX.setObjectName("dX")
        self.label_21.setGeometry(QtCore.QRect(515, 572, 31, 16))
        self.label_21.setObjectName("label_21")
        self.mu.setGeometry(QtCore.QRect(410, 506, 100, 22))
        self.mu.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.mu.setDecimals(2)
        self.mu.setMinimum(0.0)
        self.mu.setSingleStep(0.1)
        self.mu.setProperty("value", 0.2)
        self.mu.setObjectName("mu")
        self.dY.setGeometry(QtCore.QRect(410, 570, 100, 22))
        self.dY.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.dY.setDecimals(0)
        self.dY.setMinimum(-100.0)
        self.dY.setMaximum(100.0)
        self.dY.setProperty("value", 5.0)
        self.dY.setObjectName("dY")
        self.label_22.setGeometry(QtCore.QRect(540, 540, 31, 16))
        self.label_22.setObjectName("label_22")
        self.label_23.setGeometry(QtCore.QRect(675, 540, 31, 16))
        self.label_23.setObjectName("label_23")
        self.label_24.setGeometry(QtCore.QRect(540, 508, 31, 16))
        self.label_24.setObjectName("label_24")
        self.label_25.setGeometry(QtCore.QRect(675, 508, 31, 16))
        self.label_25.setObjectName("label_25")
        self.H.setGeometry(QtCore.QRect(570, 506, 100, 22))
        self.H.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.H.setDecimals(0)
        self.H.setMinimum(0.0)
        self.H.setMaximum(100.0)
        self.H.setProperty("value", 40.0)
        self.H.setObjectName("H")
        self.W.setGeometry(QtCore.QRect(570, 538, 100, 22))
        self.W.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.W.setDecimals(0)
        self.W.setMinimum(0.0)
        self.W.setMaximum(100.0)
        self.W.setProperty("value", 40.0)
        self.W.setObjectName("W")

        # add Axis
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.k1, self.k2)
        Form.setTabOrder(self.k2, self.k3)
        Form.setTabOrder(self.k3, self.k4)
        Form.setTabOrder(self.k4, self.m)
        Form.setTabOrder(self.m, self.M)
        Form.setTabOrder(self.M, self.mu)
        Form.setTabOrder(self.mu, self.dX)
        Form.setTabOrder(self.dX, self.dY)
        Form.setTabOrder(self.dY, self.H)
        Form.setTabOrder(self.H, self.W)
        Form.setTabOrder(self.W, self.btn_start)
        Form.setTabOrder(self.btn_start, self.btn_pause)

        self.W.editingFinished.connect(self.on_W_editing_finished)
        self.H.editingFinished.connect(self.on_H_editing_finished)
        self.timer.timeout.connect(self.on_timer_tick)
        self.dX.editingFinished.connect(self.on_dX_editing_finished)
        self.dY.editingFinished.connect(self.on_dY_editing_finished)
        self.btn_start.released.connect(self.on_start_clicked)
        self.btn_pause.released.connect(self.on_pause_clicked)
        self.btn_hide.released.connect(self.on_hide_clicked)

        self.on_W_editing_finished()
        self.on_H_editing_finished()

        self.chart.addSeries(self.s1_series)
        self.s1_series.attachAxis(self.axisX)
        self.s1_series.attachAxis(self.axisY)
        self.s1_series.setColor(QtGui.QColor("blue"))

        self.chart.addSeries(self.s2_series)
        self.s2_series.attachAxis(self.axisX)
        self.s2_series.attachAxis(self.axisY)
        self.s2_series.setColor(QtGui.QColor("blue"))

        self.chart.addSeries(self.s3_series)
        self.s3_series.attachAxis(self.axisX)
        self.s3_series.attachAxis(self.axisY)
        self.s3_series.setColor(QtGui.QColor("blue"))

        self.chart.addSeries(self.s4_series)
        self.s4_series.attachAxis(self.axisX)
        self.s4_series.attachAxis(self.axisY)
        self.s4_series.setColor(QtGui.QColor("blue"))

        self.chart.addSeries(self.trajectory_series)
        self.trajectory_series.attachAxis(self.axisX)
        self.trajectory_series.attachAxis(self.axisY)

        self.chart.addSeries(self.box_series)
        self.box_series.attachAxis(self.axisX)
        self.box_series.attachAxis(self.axisY)
        self.box_series.setColor(QtGui.QColor("black"))

        self.chart.addSeries(self.mass_series)
        self.mass_series.attachAxis(self.axisX)
        self.mass_series.attachAxis(self.axisY)
        self.mass_series.setMarkerShape(QtChart.QScatterSeries.MarkerShapeRectangle)
        self.mass_series.setMarkerSize(10)

        self.btn_pause.setDisabled(True)

        self.redraw(self.dX.value(), self.dY.value(), 0, 0)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Груз на пружинках в коробке"))
        self.btn_start.setText(_translate("Form", "Старт"))
        self.btn_pause.setText(_translate("Form", "Пауза"))
        self.label_4.setText(_translate("Form", "k1="))
        self.label_5.setText(_translate("Form", "Н/м"))
        self.label_6.setText(_translate("Form", "Н/м"))
        self.label_7.setText(_translate("Form", "k2="))
        self.label_8.setText(_translate("Form", "Н/м"))
        self.label_9.setText(_translate("Form", "k3="))
        self.label_10.setText(_translate("Form", "Н/м"))
        self.label_11.setText(_translate("Form", "г"))
        self.label_12.setText(_translate("Form", "m="))
        self.label_13.setText(_translate("Form", "M="))
        self.label_14.setText(_translate("Form", "k4="))
        self.label_15.setText(_translate("Form", "г"))
        self.label_17.setText(_translate("Form", "см"))
        self.label_18.setText(_translate("Form", "dX="))
        self.label_19.setText(_translate("Form", "dY="))
        self.label_20.setText(_translate("Form", "mu="))
        self.label_21.setText(_translate("Form", "см"))
        self.label_22.setText(_translate("Form", "W="))
        self.label_23.setText(_translate("Form", "см"))
        self.label_24.setText(_translate("Form", "H="))
        self.label_25.setText(_translate("Form", "см"))

    def redraw(self, x, y, xb, yb):
        self.trajectory_series.append(xb, yb)

        self.mass_series.clear()
        self.mass_series.append(x, y)

        self.box_series.clear()
        h = self.H.value() / 2
        w = self.W.value() / 2
        self.box_series.append(xb + w, yb + h)
        self.box_series.append(xb + w, yb - h)
        self.box_series.append(xb - w, yb - h)
        self.box_series.append(xb - w, yb + h)
        self.box_series.append(xb + w, yb + h)

        self.s1_series.clear()
        self.s1_series.append(x, y)
        self.s1_series.append(xb, yb + h)

        self.s2_series.clear()
        self.s2_series.append(x, y)
        self.s2_series.append(xb + w, yb)

        self.s3_series.clear()
        self.s3_series.append(x, y)
        self.s3_series.append(xb, yb - h)

        self.s4_series.clear()
        self.s4_series.append(x, y)
        self.s4_series.append(xb - w, yb)

    def on_timer_tick(self):
        self.runge_kutta.integrate(self.total_time)
        self.total_time += 0.1
        self.redraw(self.runge_kutta.y[0], self.runge_kutta.y[1], self.runge_kutta.y[2], self.runge_kutta.y[3])

    def on_W_editing_finished(self):
        self.chart.axisX().setRange(-self.W.value() - 25, self.W.value() + 25)
        self.on_dX_editing_finished()

    def on_H_editing_finished(self):
        self.chart.axisY().setRange(-self.H.value() - 25, self.H.value() + 25)
        self.on_dY_editing_finished()

    def on_dX_editing_finished(self):
        if abs(self.dX.value()) > self.W.value() / 2 - 1:
            temp = self.dX.value() / abs(self.dX.value()) * self.W.value() / 2 - 1
            self.dX.setValue(temp)
        self.redraw(self.dX.value(), self.dY.value(), 0, 0)

    def on_dY_editing_finished(self):
        if abs(self.dY.value()) > self.H.value() / 2 - 1:
            temp = self.dY.value() / abs(self.dY.value()) * self.H.value() / 2 - 1
            self.dY.setValue(temp)
        self.redraw(self.dX.value(), self.dY.value(), 0, 0)

    def on_start_clicked(self):
        if not self.btn_pause.isEnabled():
            self.runge_kutta.set_initial_value([self.dX.value(), self.dY.value(), 0, 0, 0, 0, 0, 0], 0)
        self.set_disabled_splin_boxes(True)
        self.timer.start()
        self.btn_start.setDisabled(True)
        self.btn_pause.setText("Пауза")
        self.btn_pause.setDisabled(False)

    def on_pause_clicked(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_start.setDisabled(False)
            self.btn_pause.setText("Стоп")
        else:
            self.btn_pause.setDisabled(True)
            self.btn_start.setDisabled(False)
            self.btn_pause.setText("Пауза")
            self.set_disabled_splin_boxes(False)
            self.total_time = .0
            self.trajectory_series.clear()
            self.redraw(self.dX.value(), self.dY.value(), 0, 0)
            print("______stop")

    def on_hide_clicked(self):
        self.mass_series.clear()
        self.box_series.clear()
        self.s1_series.clear()
        self.s2_series.clear()
        self.s3_series.clear()
        self.s4_series.clear()

    def set_disabled_splin_boxes(self, value):
        self.k1.setDisabled(value)
        self.k2.setDisabled(value)
        self.k3.setDisabled(value)
        self.k4.setDisabled(value)
        self.m.setDisabled(value)
        self.M.setDisabled(value)
        self.mu.setDisabled(value)
        self.dX.setDisabled(value)
        self.dY.setDisabled(value)
        self.H.setDisabled(value)
        self.W.setDisabled(value)

    # система уравнений
    def f(self, t, Y):

        def ftr(f):
            _f = self.mu.value() * (self.m.value() + self.M.value()) * 9.81
            max_value = abs(f)
            if _f > max_value:
                return -max_value
            return -_f

        f1x = self.k1.value() * (Y[0] - Y[2]) * (
                self.H.value() / np.sqrt(np.power(Y[0] - Y[2], 2) + np.power(Y[3] + self.H.value() - Y[1], 2)) - 1)

        f2x = -1 * self.k2.value() * (Y[2] - Y[0] + self.W.value()) * (
                self.W.value() / np.sqrt(np.power(Y[2] - Y[0] + self.W.value(), 2) + np.power(Y[1] - Y[3], 2)))

        f3x = -1 * self.k3.value() * (Y[0] - Y[2]) * (1 - self.H.value() / np.sqrt(
            np.power(Y[0] - Y[2], 2) + np.power(Y[1] + self.H.value() - Y[3], 2)))

        f4x = -1 * self.k4.value() * (Y[2] - Y[0] + self.W.value()) * (1 - self.W.value() / np.sqrt(
            np.power(Y[0] - Y[2] + self.W.value(), 2) + np.power(Y[1] - Y[3], 2)))

        fy1 = -1 * self.k1.value() * (Y[3] - Y[1] + self.H.value()) * (self.H.value() / np.sqrt(
            np.power(Y[0] - Y[2], 2) + np.power(Y[3] + self.H.value() - Y[1], 2)) - 1)

        fy2 = self.k2.value() * (Y[1] - Y[3]) * (
                self.W.value() / np.sqrt(np.power(Y[2] - Y[0] + self.W.value(), 2) + np.power(Y[1] - Y[3], 2)))

        fy3 = -1 * self.k3.value() * (Y[1] - Y[3] + self.H.value()) * (1 - self.H.value() / np.sqrt(
            np.power(Y[0] - Y[2], 2) + np.power(Y[1] + self.H.value() - Y[3], 2)))

        fy4 = -1 * self.k4.value() * (Y[1] - Y[3]) * (1 - self.W.value() / np.sqrt(
            np.power(Y[0] - Y[2] + self.W.value(), 2) + np.power(Y[1] - Y[3], 2)))

        fx = f1x + f2x + f3x + f4x
        fy = fy1 + fy2 + fy3 + fy4

        vvx = .0
        vvy = .0

        if Y[6] != 0 or Y[7] != 0:
            vvx = Y[6] / np.sqrt(Y[6] * Y[6] + Y[7] * Y[7])
            vvy = Y[7] / np.sqrt(Y[6] * Y[6] + Y[7] * Y[7])

        ftr_x = ftr(fx) * vvx
        ftr_y = ftr(fy) * vvy

        return [Y[4], Y[5], Y[6], Y[7], fx / self.m.value(), fx / self.m.value(), (-fx + ftr_x) / self.M.value(),
                (-fy + ftr_y) / self.M.value()]


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
