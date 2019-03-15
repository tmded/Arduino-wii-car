import cwiid
import time
import serial

#connecting to the wiimote. This allows several attempts
# as first few often fail.
ser = serial.Serial('/dev/ttyACM0')
print 'Press 1+2 on your Wiimote now...'
wm = None
i=2
while not wm:
    try:
        wm=cwiid.Wiimote()
    except RuntimeError:
        if (i>5):
            quit()
            print "Error opening wiimote connection"
            print "attempt " + str(i)
            i +=1
wm.led =1
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
    print(wm.state['acc'][1])
    time.sleep(0.3)
