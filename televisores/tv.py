class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV._numTV += 1

    @classmethod
    def setNumTV(cls, num):
        cls._numTV = num
    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control

    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio

    def setVolumen(self, vol):
        self._volumen = vol
    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):
        if 0 < canal < 120 and self.getEstado():
            self._canal = canal
    def getCanal(self):
        return self._canal


    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    def getEstado(self):
        return self._estado


    def canalUp(self):
        if self._canal < 120 and self.getEstado():
            self._canal += 1
    def canalDown(self):
        if self._canal > 1 and self.getEstado():
            self._canal -= 1

    def volumenUp(self):
        if self._volumen < 7 and self.getEstado():
            self._volumen += 1
    def volumenDown(self):
        if self._volumen > 0 and self.getEstado():
            self._volumen -= 1