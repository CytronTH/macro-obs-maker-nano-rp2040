import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import neopixel
import simpleio

TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4

# Initialize LEDs
# LEDs placement on Maker Pi RP2040
button_1p = board.GP2
button_2p = board.GP3
button_3p = board.GP4
button_4p = board.GP5
button_5p = board.GP6
button_6p = board.GP7
button_7p = board.GP8
button_8p = board.GP9

led_pin = board.GP11
num_led = 2
ORDER = neopixel.RGB

led = neopixel.NeoPixel(
    led_pin, num_led, brightness=0.5, auto_write=False, pixel_order=ORDER
    )

PIEZO_PIN = board.GP22
START_TONE_FREQ = [ 523,  # C4
              659,  # D4
              784,  # E4
]
BUTTON_TONE_FREQ = [ 784,  # C4
              659,  # D4
]

keyboard = Keyboard(usb_hid.devices)

button_1 = digitalio.DigitalInOut(button_1p)
button_2 = digitalio.DigitalInOut(button_2p)
button_3 = digitalio.DigitalInOut(button_3p)
button_4 = digitalio.DigitalInOut(button_4p)
button_5 = digitalio.DigitalInOut(button_5p)
button_6 = digitalio.DigitalInOut(button_6p)
button_7 = digitalio.DigitalInOut(button_7p)
button_8 = digitalio.DigitalInOut(button_8p)

button_1.direction = digitalio.Direction.INPUT
button_2.direction = digitalio.Direction.INPUT
button_3.direction = digitalio.Direction.INPUT
button_4.direction = digitalio.Direction.INPUT
button_5.direction = digitalio.Direction.INPUT
button_6.direction = digitalio.Direction.INPUT
button_7.direction = digitalio.Direction.INPUT
button_8.direction = digitalio.Direction.INPUT

button_1.pull = digitalio.Pull.DOWN
button_2.pull = digitalio.Pull.DOWN
button_3.pull = digitalio.Pull.DOWN
button_4.pull = digitalio.Pull.DOWN
button_5.pull = digitalio.Pull.DOWN
button_6.pull = digitalio.Pull.DOWN
button_7.pull = digitalio.Pull.DOWN
button_8.pull = digitalio.Pull.DOWN
def start_sound():
    for i in range(len(START_TONE_FREQ)):
        simpleio.tone(PIEZO_PIN, START_TONE_FREQ[i], duration=0.2)
def button_press_sound():
    for i in range(len(BUTTON_TONE_FREQ)):
        simpleio.tone(PIEZO_PIN, BUTTON_TONE_FREQ[i], duration=0.2)
start_sound()
while True:
    if button_1.value:
        print("button 1 pressed")
        led.fill((154, 0, 255))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F3)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F3)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_2.value:
        print("button 2 pressed")
        led.fill((0, 255, 255))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F4)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F4)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_3.value:
        print("button 3 pressed")
        led.fill((0, 17, 255))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F5)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F5)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_4.value:
        print("button 4 pressed")
        led.fill((0, 255, 51))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F6)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F6)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_5.value:
        print("button 5 pressed")
        led.fill((0, 255, 247))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F7)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F7)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_6.value:
        print("button 6 pressed")
        led.fill((255, 119, 0))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F8)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F8)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_7.value:
        print("button 7 pressed")
        led.fill((255, 0, 0))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F9)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F9)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    if button_8.value:
        print("button 8 pressed")
        led.fill((0, 145, 255))
        led.show()
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.F10)
        button_press_sound()
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.F10)
        time.sleep(1)
        led.fill((0, 0, 0))
        led.show()
        
    time.sleep(0.1)

