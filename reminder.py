from pygame import mixer
from datetime import datetime
from time import time


def log(msg):
    print(f"{msg} at {datetime.now()}")

        
    
def musicOn(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inp=input()
        if inp==stopper:
            mixer.music.stop()
            break
   


init_water=time()
init_eye=time()
watersec=25
eyesec=12


while True:
    if time()-init_water > watersec:
        print("water time enter 'Wdone'")
        musicOn("reminder\\water.mp3" , "W")
        init_water=time()
        log("drank water ")
    elif time()-init_eye > eyesec:
        print("eye time enter 'Edone' ")
        musicOn("reminder\\water2.mp3" , "E")
        init_eye=time()
        log("done eye ")