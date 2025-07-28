# Raspberry Pi GPIO Drum Kit
# This program creates a digital drum kit using GPIO pins on a Raspberry Pi
# Each pin acts as a trigger for different drum sounds when activated

import RPi.GPIO as IO
import time
import pygame.mixer

# GPIO Configuration
# Change this number to adjust touch sensitivity threshold, 0 is default
# (note: Raspberry Pi GPIO doesn't have touch sensitivity, adjust if using a different sensor)
IO.setmode(IO.BCM)  # Use Broadcom pin numbering scheme

# Setup GPIO pins as inputs for drum triggers
# Each pin corresponds to a different drum sound
IO.setup(21, IO.IN)  # Drum pad 0
IO.setup(20, IO.IN)  # Drum pad 1
IO.setup(16, IO.IN)  # Drum pad 2
IO.setup(12, IO.IN)  # Drum pad 3
IO.setup(25, IO.IN)  # Drum pad 4
IO.setup(24, IO.IN)  # Drum pad 5
IO.setup(23, IO.IN)  # Drum pad 6
IO.setup(18, IO.IN)  # Drum pad 7

# Sound File Mapping
# Define drum sound file paths (use relative paths)
# Each index corresponds to a GPIO pin and its associated sound file
drum_sounds = {
    0: "snare-roll-84943.mp3",                    # Snare roll sound
    1: "mixkit-toy-drums-and-bell-ding-560.wav", # Toy drum with bell
    2: "mixkit-tribal-dry-drum-558.wav",         # Tribal dry drum
    3: "mixkit-short-bass-hit-2299.wav",         # Short bass hit
    4: "mixkit-hand-tribal-drum-562.wav",        # Hand tribal drum
    5: "bassdrum-10-45967.mp3",                  # Bass drum
    6: "fresh_snap-37385.mp3",                   # Snap sound
    7: "kick-183936.mp3",                        # Kick drum
}

# Audio System Initialization
pygame.mixer.init()  # Initialize pygame's audio mixer for sound playback

# Main Program Loop
while True:
    # Check each GPIO pin for input
    for index, pin in enumerate([21, 20, 16, 12, 25, 24, 23, 18]):
        # Check if the pin is HIGH (triggered)
        if IO.input(pin):
            # Debounce delay - wait 1ms to ensure stable input
            time.sleep(0.001)
            
            # Double-check the pin state to confirm trigger
            if IO.input(pin):
                # Get the corresponding sound file for this pin
                sound_file = drum_sounds.get(index, None)
                
                # If a valid sound file exists, play it
                if sound_file:
                    print(f"Playing sound: {sound_file}")
                    
                    # Load and play the sound
                    sound = pygame.mixer.Sound(sound_file)
                    sound.play()
                    
                    # Wait for the sound to finish playing completely
                    # This prevents overlapping sounds and ensures clean playback
                    time.sleep(sound.get_length())
    
    # Brief delay between loop iterations to prevent excessive CPU usage
    time.sleep(0.2)