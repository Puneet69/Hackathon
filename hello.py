import pyaudio
import numpy as np

def record_audio():
    duration = 5
    fs = 44100  # Sample rate
    audio_data = []

    p = pyaudio.PyAudio()

    # Get the default input and output device indices
    input_device_index = p.get_default_input_device_info()['index']
    output_device_index = p.get_default_output_device_info()['index']
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=fs,
                    input=True,
                    input_device_index=input_device_index,  # Set input device explicitly
                    frames_per_buffer=1024)
    
    print("Recording...")
    
    for _ in range(0, int(fs / 1024 * duration)):
        data = stream.read(1024)
        audio_data.append(np.frombuffer(data, dtype=np.int16))
    
    print("Finished recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    return np.concatenate(audio_data)

def detect_sound(audio_clip):
    # Replace with your machine learning model for sound detection
    # This is a placeholder function and should be implemented separately.
    return np.random.choice(["whistle", "toaster", "door_knock", "clapping", "other"])

def main():
    whistle_count = 0
    toaster_detected = False
    door_knock_detected = False
    clapping_detected = False
    required_consecutive_whistles = 3

    while True:
        audio_clip = record_audio()
        detected_sound = detect_sound(audio_clip)
        
        if detected_sound == "whistle":
            whistle_count += 1
            if whistle_count >= required_consecutive_whistles:
                print("Please turn off the gas")  
                break
        elif detected_sound == "toaster":
            if not toaster_detected:
                print("Please take out the bread") 
                toaster_detected = True
        elif detected_sound == "door_knock":
            if not door_knock_detected:
                print("Someone's knocking on the door")  
                door_knock_detected = True
        elif detected_sound == "clapping":
            if not clapping_detected:
                print("Someone is clapping")  
                clapping_detected = True
        else:
            whistle_count = 0
            toaster_detected = False
            door_knock_detected = False
            clapping_detected = False

if _name_ == "__main__":
    main()