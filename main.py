import sounddevice as sd
import numpy as np
import pygame

def detect_sound_callback(indata, frames, time, status):
    # This callback function is called for each audio block received

    # Set a threshold to detect when the sound is above a certain level
    threshold = 0.02


    # Calculate the root mean square (RMS) to measure the audio intensity
    rms = np.sqrt(np.mean(indata**2))

    # If the RMS value exceeds the threshold, consider it a2
    # sound event
    
    if rms > threshold:
        print("Sound detected!")
        play_notification()

def play_notification():
    # Specify the path to the notification sound file
    notification_sound_path = "alarm4.mp3"

    # Initialize pygame mixer
    pygame.mixer.init()


    # Load the sound file
    sound = pygame.mixer.Sound(notification_sound_path)

    # Play the sound
    sound.play()

def main():
    # Set the sample rate and duration for recording
    sample_rate = 44100  # Hz
    duration = 18000  # seconds

    # Set up the microphone input stream with the callback function
    with sd.InputStream(callback=detect_sound_callback, channels=1, samplerate=sample_rate):
        print("Listening for sounds...")
        sd.sleep(duration * 1000)  # Sleep for the specified duration

if __name__ == "__main__":
    main()



