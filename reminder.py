#!/usr/bin/python3
'''
A simple GUI reminder
Dependence:
    pymsgbox: use pip install pymsgbox to install
    winsound: depended only under windows, not tested
Use:
    python reminder.py [--title Reminder] [--text Reminder] [--interval 60] 
                       [--sound reminder.wav]
'''

import time
import os
import sys
import os
import pymsgbox


def showmsg(text='Reminder',title='Reminder'):
    '''
    Show Message
    '''
    ans = pymsgbox.confirm(text, title, ['Got it', 'Stop Reminder'])
    if ans == 'Stop Reminder':
        ans = 'n'
    else:
        ans = 'y'
    return(ans)
    
    
def playsd(sound='reminder.wav'):
    '''
    Play Sound
    '''
    if not os.path.exists(sound):
        print('Sound file not found!')
    else:
        if sys.platform[:5] == 'linux':
            if sys.version[0] == '3':
                os.popen('aplay -q '+sound)
            else:
                os.popen2('aplay -q '+sound)
        else:
            import winsound
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            
    
if __name__ == '__main__':

    interval = 60 # minutes
    title = 'Reminder'
    text = ''
    sound = 'reminder.wav'
    if len(sys.argv) < 2:
        pass
    else:
        args = sys.argv[1:]
        length = len(args)
        for i, item in enumerate(args):
            if item.startswith('--'):
                name = item[2:]
                if name.startswith('ti') and i+1 <= length:
                    if not args[i+1].startswith('--'):
                        title = args[i+1]
                if name.startswith('te') and i+1 <= length:
                    if not args[i+1].startswith('--'):
                        text = args[i+1]                        
                if name.startswith('in') and i+1 <= length:
                    if not args[i+1].startswith('--'):
                        try:
                            interval = float(args[i+1])  
                        except:
                            print('Illegal interval!')
                            sys.exit()
                if name.startswith('so') and i+1 <= length:
                    if not args[i+1].startswith('--'):
                        sound = args[i+1]
    if sys.platform[:5] == 'linux':
        sound = os.path.split(os.path.realpath(__file__))[0]+'/'+sound
    else:
        sound = os.path.split(os.path.realpath(__file__))[0]+'\\'+sound
    if text == '':
        text = 'You have been working for '+str(interval)+' minutes \n'+ \
                'It\'s time to walk and drink some water!'
    ans = 'y'
    while ans == 'y':
        time.sleep(interval*60.)
        playsd(sound=sound)
        time.sleep(0.2)
        ans = showmsg(text=text, title=title)                           
