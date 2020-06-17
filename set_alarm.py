import simpleaudio as sa
import sched
import time

def set_alarm(settime, audiofile, message):
    while True:
         if time.time() == settime:
             print(message)
             wave_obj = sa.WaveObject.from_wave_file(audiofile)
             play_obj = wave_obj.play()
             play_obj.wait_done()
             break


set_alarm(time.time()+5, "file_example_WAV_1MG.wav", "Wake up!")
