import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685(address=0x60, busnum=1)
pwm.set_pwm_freq(60)
while True:
    print str(1)
    pwm.set_pwm(8,4096, 0)
    pwm.set_pwm(9,0,4096)
    pwm.set_pwm(10,4096,0)
    time.sleep(1)
    print str(2)
    pwm.set_pwm(8, 4096, 0)
    pwm.set_pwm(9, 4096, 0)
    pwm.set_pwm(10, 4096, 0)
    time.sleep(1)
    print str(3)
    pwm.set_pwm(8, 4096, 0)
    pwm.set_pwm(9, 4096, 0)
    pwm.set_pwm(10, 0, 4096)
    time.sleep(1)
    print str(4)
    pwm.set_pwm(8, 4096, 0)
    pwm.set_pwm(9, 0, 4096)
    pwm.set_pwm(10, 0, 4096)
    time.sleep(1)
    print str(5)
    pwm.set_pwm(8, 0, 4096)
    pwm.set_pwm(9, 0, 4096)
    pwm.set_pwm(10, 4096, 0)
    time.sleep(1)
    print str(6)
    pwm.set_pwm(8, 0, 4096)
    pwm.set_pwm(9, 4096, 0)
    pwm.set_pwm(10, 4096, 0)
    time.sleep(1)
    print str(7)
    pwm.set_pwm(8, 0, 4096)
    pwm.set_pwm(9, 4096, 0)
    pwm.set_pwm(10, 0, 4096)
    time.sleep(1)
    print str(8)
    pwm.set_pwm(8, 0, 4096)
    pwm.set_pwm(9, 0, 4096)
    pwm.set_pwm(10, 0, 4096)
    time.sleep(1)
