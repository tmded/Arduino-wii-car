import cwiid
import time
import serial

def normalize(val):
   value = float(val-100)/float(150-100)
   
   return value


def get_motor_speeds(val):
    scalar = normalize(val)
    #print(scalar)
    m1 = min((255,(255 * scalar  * 2)))
    m2 = min((255,(255 * ( 1.0 - scalar ) * 2)))
    return m1, m2

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

wm.rpt_mode = cwiid.RPT_BTN| cwiid.RPT_ACC
ser.write('s')
stopped = False
timer = 0
while True:
    buttons = wm.state["buttons"]
    wii_acc_data = wm.state['acc']
    pressed = False
    changing = False
    if (buttons &cwiid.BTN_RIGHT):
        serial_msg = ("f")
        pressed=True
        changing = True
        print("UP")
        stopped = False
    if (buttons &cwiid.BTN_LEFT):
        serial_msg = ("b")
        pressed=True
        changing = True
        stopped = False
    if wii_acc_data[1] >=100 and wii_acc_data[1]<=150 and(buttons &cwiid.BTN_B ):
        if wii_acc_data[1]>125:
           serial_msg=('l')
        else:
           serial_msg = ('r')
        pressed=True
        changing = True
        stopped = False

    if not pressed and not stopped:
        serial_msg = ("s")
        pressed=True
        changing = True
        stopped = True
    if (buttons & cwiid.BTN_PLUS):
        break
        
    time.sleep(0.05)
    ser.write(serial_msg)

    timer+=1
    if wii_acc_data[1] >=100 and wii_acc_data[1]<=150 and not(buttons & cwiid.BTN_B):
        timer=0
        # m1= right motor/ENA | m2 = left motor/ENB
        ser.write('m')
        #print(ser.readline())
        m1,m2 = get_motor_speeds(int(wii_acc_data[1]))
        time.sleep(0.05)
        ser.write(str(int(m2)))
        ser.write('n')
        time.sleep(0.05)
        ser.write(str(int(m1)))
        #print("sent all variables")
    time.sleep(0.05)
        
    
    
                       
