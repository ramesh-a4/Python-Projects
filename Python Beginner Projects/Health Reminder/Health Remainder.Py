# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:17:18 2022

@author: 7CNanda
"""
from pygame import mixer
#import datetime
import time

def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        st=input('Énter the code to stop')
        if st==stopper:
            mixer.music.stop()
            break
        else:
            if st=='stop':
                mixer.music.stop()
                return 'stop'
        
def log(file,st):
    fhand = open(file,'a')
    s=f'\n{st} and logged at {time.ctime()}'
    fhand.write(s)
    
   
if __name__ == '__main__':
    init_water=time.time()
    init_eyes=time.time()
    init_exercise=time.time()
    eyesecs=5
    physecs=10
    watersecs=15
    t=time.localtime()
    x=t.tm_hour
    glass=0
    if (x>9 and x<17):
        while True:
            if time.time()-init_water>watersecs:
                if glass<2:
                    print('It\'s time to drink water.Enter drank to stop the alarm' )
                    st=music('water.mp3','drank')
                    glass+=1
                    init_water=time.time()
                    log('water.txt','water drank\t')
                    if st=='stop':
                        print('Alarm stopped forceably')
                        break
                elif glass==2:
                    glass+=1
                    print('Daily requirement of water for body is reached')
                    print('Hence water remender alarm is disabled')
                
                
            if time.time()-init_water>eyesecs:
                print('It\'s time to do eye exercise.Enter done to stop the alarm' )
                st=music('eyes.mp3','done')
                init_eyes=time.time()
                log('eyes.txt','eye exercise done\t')
                if st=='stop':
                    print('Alarm stopped forceably')
                    break
                
            if time.time()-init_water>physecs:
                print('It\'s time to do phy exercise.Enter done to stop the alarm' )
                st=music('physical.mp3','done')
                init_exercise=time.time()
                log('physical.txt','physical exe done \t')
                if st=='stop':
                    print('Alarm stopped forceably')
                    break
        
    else:
        print('This is not a working hour in the company')
        print('So,alarms can\'t be turned on')
            
            
            
            
            
            
            
            
            
            
            