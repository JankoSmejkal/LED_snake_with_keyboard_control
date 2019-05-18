# Import libraries
import RPi.GPIO as GPIO
import curses
import time

# Set up GPIO output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

# Initialise keyboard control
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Main loop
try:
    while True:
        # Switch off all LEDs
            GPIO.output(33,False)
            GPIO.output(35,False)
            GPIO.output(33,False)
            
            # Get keyboard key
            direction = screen.getch()
            
            # Move snake right by controlling GPIO pins output
            if direction == ord('r'):
                for x in range(3):
                    GPIO.output(37,True)
                    time.sleep(0.1)
                    GPIO.output(35,True)
                    time.sleep(0.1)
                    GPIO.output(33,True)
                    time.sleep(0.1)
                    GPIO.output(37,False)
                    time.sleep(0.1)
                    GPIO.output(35,False)
                    time.sleep(0.1)
                    GPIO.output(33,False)
                    time.sleep(1)
                    
            # Move snake left by controlling GPIO pins output
            if direction == ord('l'):
                for x in range(3):
                    GPIO.output(33,True)
                    time.sleep(0.1)
                    GPIO.output(35,True)
                    time.sleep(0.1)
                    GPIO.output(37,True)
                    time.sleep(0.1)
                    GPIO.output(33,False)
                    time.sleep(0.1)
                    GPIO.output(35,False)
                    time.sleep(0.1)
                    GPIO.output(37,False)
                    time.sleep(0.1)
                    time.sleep(1)
            
            # Move snake both ways by controlling GPIO pins output
            if direction == ord('b'):    
                for x in range (3):
                    GPIO.output(33,True)
                    time.sleep(0.1)
                    GPIO.output(35,True)
                    time.sleep(0.1)
                    GPIO.output(37,True)
                    time.sleep(0.1)
                    GPIO.output(33,False)
                    time.sleep(0.1)
                    GPIO.output(35,False)
                    time.sleep(0.1)
                    GPIO.output(37,False)
                    time.sleep(0.1)

                    GPIO.output(37,True)
                    time.sleep(0.1)
                    GPIO.output(35,True)
                    time.sleep(0.1)
                    GPIO.output(33,True)
                    time.sleep(0.1)
                    GPIO.output(37,False)
                    time.sleep(0.1)
                    GPIO.output(35,False)
                    time.sleep(0.1)
                    GPIO.output(33,False)
                    time.sleep(1)
            
            # Flash leds by controlling GPIO pins output
            if direction == ord('j'):
                for x in range (9):
                    GPIO.output(35,True)
                    time.sleep(0.1)
                    GPIO.output(35,False)
                    GPIO.output(33,True)
                    GPIO.output(37,True)
                    time.sleep(0.1)
                    GPIO.output(35,True)
                    GPIO.output(33,False)
                    GPIO.output(37,False)
                    
            # End process by pressing 'q'                  
            if direction == ord('q'):
                break

            
finally:
    # Close curses
    curses.nocbreak();screen.keypad(0);curses.echo();curses.endwin()

#Reset GPIO pins
GPIO.cleanup()
