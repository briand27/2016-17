import Adafruit_GPIO.I2C as I2C


class DistanceSensor(object):

    _addr = 0x53
    _distReg = 0x53
    _calibInt = 0
    _calibM = 1

    def __init__(self, addr):
        self._addr = addr
        self._i2cDev = I2C.Device(self._addr, I2C.get_default_bus())

    def setup(self):
        pass

    def getRawData(self):
        # reads 2 bytes from the data register
        #return self._i2cDev.readList(self._distReg, 2)
        return self._i2cDev.readU8(0xC0)

    def getData(self):
        return self._calibM * self.getRawData() + self._calibInt

    def setCalib(self, slope, intercept):
        self._calibInt = intercept
        self._calibM = slope
