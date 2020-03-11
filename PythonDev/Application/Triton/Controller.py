'''
Created on Feb 4, 2020

@author: matt
CAUTION: On windows, do not close using the "X" in the top right.  Use Ctrl-C or the Esc key to close properly
'''
from multiprocessing import Process
import threading
import time
import keyboard
from InputSystem import *
from DriveSystem import *
from OpticalSystem import *
from SandSystem import *
from HelperClasses import RepeatedTimer


INPUT_REFRESH_PERIOD = 1000     #ms
JOYSTICK_REFRESH_PERIOD = 3     #ms - can lag with high values due to pipe
MAIN_REFRESH_PERIOD =   250     #ms


inputSystem = InputSystem(0)

def DriveLoop():
    '''
    '''
    print("in driveloop")
    driveSystem = DriveSystem(0)
        
def OpticalLoop():
    '''
    '''

    print("in opticalloop")
    opticalSystem = OpticalSystem(0)
        
def SandLoop():
    '''
    '''

    print("in sandloop")
    sandSystem = SandSystem(0)
        
def InputLoop():
    '''
    '''
    print("in inputloop")
    #inputSystem = InputSystem(0)
    global inputSystem
    
    joystickRefresh = RepeatedTimer(JOYSTICK_REFRESH_PERIOD, inputSystem.updateJoystick)
    inputRefresh = RepeatedTimer(INPUT_REFRESH_PERIOD, inputSystem.updateValues)




    



#Start MultiProcessing Loops
if __name__ == '__main__':


    # freeze_support()
    DriveProcess = threading.Thread(target = DriveLoop, name = "DriveProcess")
    OpticalProcess = threading.Thread(target = OpticalLoop, name = "OpticalProcess")
    SandProcess = threading.Thread(target = SandLoop, name = "SandProcess")
    InputProcess = threading.Thread(target = InputLoop, name = "InputProcess")

    DriveProcess.daemon = True
    OpticalProcess.daemon = True
    SandProcess.daemon = True
    InputProcess.daemon = True

    DriveProcess.start()
    OpticalProcess.start()
    SandProcess.start()
    InputProcess.start()
    
    run = True
    #Main Loop
    while run == True and not keyboard.is_pressed('Escape'): #Not perfect, only ends when esc is held, not pressed
        time.sleep(MAIN_REFRESH_PERIOD/1000)
        #inputSystem.updateJoystick()
        print(inputSystem.strJoystickState())


