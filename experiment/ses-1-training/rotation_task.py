#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on Fri 27 May 2022 13:34:24 
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'tmptmp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/lil/projects/ccn/ContinuousValue/rotation/taskCodeBU/rotation_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='A mysterious radioactive substance has just landed on the surface of the Earth, and is emitting radiations harmful for us and our planet. You are tasked with protecting the Earth from these radiations, capturing as many of them as possible with an absorbing shield.\n\nBelow, you can see examples of the shield missing (left) and catching (right) the radiation.\n\n\n\n\n\n\n\n\nPress any key to start.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
shield_miss = visual.ImageStim(
    win=win,
    name='shield_miss', 
    image='images/shield_miss.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.12), size=(0.25, 0.282),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
shield_hit = visual.ImageStim(
    win=win,
    name='shield_hit', 
    image='images/shield_hit.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, -0.12), size=(0.25, 0.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "practiceMove_earth"
practiceMove_earthClock = core.Clock()
kb = keyboard.Keyboard()

#set constants for the experiment
ROTATION_SPEED = 1;
CIRCLE_RADIUS = 3;

#initialise variables that will be updated as experiment progresses
shieldDegrees = 45; #because it needs to be predefined
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;

#calculate the screen X and Y locations that correspond to the shield centre
shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldX = np.concatenate(([0],shieldX));
shieldY = np.concatenate(([0],shieldY));
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

shieldRotation = 0; #begin at top
shield_move = visual.ShapeStim(
    win=win, name='shield_move', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_centre_move = visual.ShapeStim(
    win=win, name='shield_centre_move', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
earth_move = visual.ImageStim(
    win=win,
    name='earth_move', units='cm', 
    image='images/earth.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(CIRCLE_RADIUS*2, CIRCLE_RADIUS*2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='You are preparing to defend the Earth. \n\nPlease practice by moving the shield using the left and right arrows.\n\n\n\n\n\nWhen you are ready to advance, press the space bar.',
    font='Open Sans',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_move = keyboard.Keyboard()

# Initialize components for Routine "practiceSize_earth"
practiceSize_earthClock = core.Clock()
shield_size = visual.ShapeStim(
    win=win, name='shield_size', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=shieldRotation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_centre_size = visual.ShapeStim(
    win=win, name='shield_centre_size', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=(1, 1),
    ori=shieldRotation, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
earth_size = visual.ImageStim(
    win=win,
    name='earth_size', units='cm', 
    image='images/earth.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(CIRCLE_RADIUS*2, CIRCLE_RADIUS*2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='You are preparing to defend the Earth. \n\nPlease practice by changing the shield size using the up and down arrows.\n\n\n\n\n\nWhen you are ready to advance, press the space bar.',
    font='Open Sans',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_size = keyboard.Keyboard()

# Initialize components for Routine "trial_earth"
trial_earthClock = core.Clock()
laser_2 = visual.ShapeStim(
    win=win, name='laser_2', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.4]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-1.0, interpolate=True)
shield_2 = visual.ShapeStim(
    win=win, name='shield_2', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
shield_centre_2 = visual.ShapeStim(
    win=win, name='shield_centre_2', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
shield_background_2 = visual.ShapeStim(
    win=win, name='shield_background_2', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
reward_text_2 = visual.TextStim(win=win, name='reward_text_2',
    text='',
    font='Open Sans',
    pos=(0, 0.02), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
earth_2 = visual.ImageStim(
    win=win,
    name='earth_2', units='cm', 
    image='images/earth.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(CIRCLE_RADIUS*2, CIRCLE_RADIUS*2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "trial_sun"
trial_sunClock = core.Clock()
shield_background_long_3 = visual.ShapeStim(
    win=win, name='shield_background_long_3', vertices=shieldCoords,units='cm', 
    size=(1.3, 1.3),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_3 = visual.ShapeStim(
    win=win, name='shield_3', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
shield_centre_3 = visual.ShapeStim(
    win=win, name='shield_centre_3', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
shield_background_short_3 = visual.ShapeStim(
    win=win, name='shield_background_short_3', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
laser_3 = visual.ShapeStim(
    win=win, name='laser_3', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=None, depth=-5.0, interpolate=True)
sun = visual.ImageStim(
    win=win,
    name='sun', units='cm', 
    image='images/sun_ppt.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "practiceMove_radio"
practiceMove_radioClock = core.Clock()
kb = keyboard.Keyboard()

#set constants for the experiment
ROTATION_SPEED = 1;
CIRCLE_RADIUS = 3;

#initialise variables that will be updated as experiment progresses
shieldDegrees = 45; #because it needs to be predefined
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;

#calculate the screen X and Y locations that correspond to the shield centre
shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldX = np.concatenate(([0],shieldX));
shieldY = np.concatenate(([0],shieldY));
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

shieldRotation = 0; #begin at top

#initialise list containing data to be saved
saveData = [["blockID","currentFrame","laserRotation","shieldRotation","shieldDegrees","currentHit","totalReward","sendTrigger","triggerValue"]]
saveFilename = "savedData_" + str(expInfo['participant']) + str(expInfo['session']) + ".csv" #load stimulusStream into NumPy array
shield_move_radio = visual.ShapeStim(
    win=win, name='shield_move_radio', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, -3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_centre_move_radio = visual.ShapeStim(
    win=win, name='shield_centre_move_radio', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
shield_background_short_move = visual.ShapeStim(
    win=win, name='shield_background_short_move', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, -3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
radioactive_move = visual.ImageStim(
    win=win,
    name='radioactive_move', units='cm', 
    image='images/radioactive1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -3), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
text_move_radio = visual.TextStim(win=win, name='text_move_radio',
    text='You must manoeuvre the shield. The more radiations you catch, the lesser the damage to the Earth. You are preparing using a shield around a harmless replication of the radioactive body. \n\nPlease practice by moving the shield using the left and right arrows.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_advance_move = visual.TextStim(win=win, name='text_advance_move',
    text='When you are ready to advance, press the space bar.',
    font='Open Sans',
    pos=(0, -0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_move_radio = keyboard.Keyboard()

# Initialize components for Routine "sizeExamples_ratio"
sizeExamples_ratioClock = core.Clock()
text_size_examples = visual.TextStim(win=win, name='text_size_examples',
    text='You can also control the size of the shield, meaning you can make it bigger or smaller to catch more radiations, but you have to be careful: the larger the shield, the weaker its capturing ability. That means using a smaller shield will be more difficult for capturing radiations, but also that these will do less damage than if a bigger shield captured them.\n\nBelow, you can see examples of a small (left), medium (centre), and large (right) shield.',
    font='Open Sans',
    pos=(0, 0.23), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_size_advance = visual.TextStim(win=win, name='text_size_advance',
    text='When you are ready to advance, press the space bar.',
    font='Open Sans',
    pos=(0, -0.34), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
shield_small = visual.ImageStim(
    win=win,
    name='shield_small', 
    image='images/shield_small.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, -0.13), size=(0.25, 0.235),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
shield_medium = visual.ImageStim(
    win=win,
    name='shield_medium', 
    image='images/shield_medium.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.13), size=(0.25, 0.235),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
shield_large = visual.ImageStim(
    win=win,
    name='shield_large', 
    image='images/shield_large.png', mask=None, anchor='center',
    ori=0.0, pos=(0.4, -0.13), size=(0.25, 0.235),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_size_examples = keyboard.Keyboard()

# Initialize components for Routine "practiceSize_radio"
practiceSize_radioClock = core.Clock()
shield_size_radio = visual.ShapeStim(
    win=win, name='shield_size_radio', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=shieldRotation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_centre_size_radio = visual.ShapeStim(
    win=win, name='shield_centre_size_radio', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=(1.1, 1.1),
    ori=shieldRotation, pos=(0, 0), anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
shield_background_short_size = visual.ShapeStim(
    win=win, name='shield_background_short_size', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=shieldRotation, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
radio_size = visual.ImageStim(
    win=win,
    name='radio_size', units='cm', 
    image='images/radioactive1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
text_radio_size = visual.TextStim(win=win, name='text_radio_size',
    text='You are preparing to capture the radiations using a shield around a harmless replication of the radioactive body. \n\nPlease practice by changing the shield size using the up and down arrows.\n\n\n\n\n\n\n\nWhen you are ready to advance, press the space bar.',
    font='Open Sans',
    pos=(0, 0.12), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_radio_size = keyboard.Keyboard()

# Initialize components for Routine "blockStartText"
blockStartTextClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="New block ahead.\n\nPress any key if you're ready to start.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial_radio"
trial_radioClock = core.Clock()
earth_background = visual.ImageStim(
    win=win,
    name='earth_background', 
    image='images/earth.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
harmless_area = visual.ShapeStim(
    win=win, name='harmless_area',units='cm', 
    size=(6.6, 6.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-2.0, interpolate=True)
shield = visual.ShapeStim(
    win=win, name='shield', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
shield_centre = visual.ShapeStim(
    win=win, name='shield_centre', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-4.0, interpolate=True)
shield_background_short = visual.ShapeStim(
    win=win, name='shield_background_short', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
laser = visual.ShapeStim(
    win=win, name='laser', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
laser_long = visual.ShapeStim(
    win=win, name='laser_long', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.4]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-7.0, interpolate=True)
radioactive = visual.ImageStim(
    win=win,
    name='radioactive', units='cm', 
    image='images/radioactive1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
trialTrigger = parallel.ParallelPort(address='0x4FF8')

# Initialize components for Routine "blockEndText"
blockEndTextClock = core.Clock()
textPause = visual.TextStim(win=win, name='textPause',
    text='Well done.\n\nTake a short break.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textContinue = visual.TextStim(win=win, name='textContinue',
    text='Press any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "expEndText"
expEndTextClock = core.Clock()
textEndExp = visual.TextStim(win=win, name='textEndExp',
    text='Well done. You completed all blocks.\n\nThank you',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [text, key_resp, shield_miss, shield_hit]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *shield_miss* updates
    if shield_miss.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shield_miss.frameNStart = frameN  # exact frame index
        shield_miss.tStart = t  # local t and not account for scr refresh
        shield_miss.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_miss, 'tStartRefresh')  # time at next scr refresh
        shield_miss.setAutoDraw(True)
    
    # *shield_hit* updates
    if shield_hit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shield_hit.frameNStart = frameN  # exact frame index
        shield_hit.tStart = t  # local t and not account for scr refresh
        shield_hit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_hit, 'tStartRefresh')  # time at next scr refresh
        shield_hit.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('shield_miss.started', shield_miss.tStartRefresh)
thisExp.addData('shield_miss.stopped', shield_miss.tStopRefresh)
thisExp.addData('shield_hit.started', shield_hit.tStartRefresh)
thisExp.addData('shield_hit.stopped', shield_hit.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceMove_earth"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_move.keys = []
    key_resp_move.rt = []
    _key_resp_move_allKeys = []
    # keep track of which components have finished
    practiceMove_earthComponents = [shield_move, shield_centre_move, earth_move, text_3, key_resp_move]
    for thisComponent in practiceMove_earthComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceMove_earthClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceMove_earth"-------
    while continueRoutine:
        # get current time
        t = practiceMove_earthClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceMove_earthClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=False)
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=False,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]=='right':
                shieldRotation += ROTATION_SPEED;
            if LRkeys_pressed[-1]=='left':
                shieldRotation -= ROTATION_SPEED;
        
        # *shield_move* updates
        if shield_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            shield_move.frameNStart = frameN  # exact frame index
            shield_move.tStart = t  # local t and not account for scr refresh
            shield_move.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_move, 'tStartRefresh')  # time at next scr refresh
            shield_move.setAutoDraw(True)
        if shield_move.status == STARTED:  # only update if drawing
            shield_move.setOri(shieldRotation, log=False)
        
        # *shield_centre_move* updates
        if shield_centre_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            shield_centre_move.frameNStart = frameN  # exact frame index
            shield_centre_move.tStart = t  # local t and not account for scr refresh
            shield_centre_move.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre_move, 'tStartRefresh')  # time at next scr refresh
            shield_centre_move.setAutoDraw(True)
        if shield_centre_move.status == STARTED:  # only update if drawing
            shield_centre_move.setPos((0, 0), log=False)
            shield_centre_move.setOri(shieldRotation, log=False)
        
        # *earth_move* updates
        if earth_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            earth_move.frameNStart = frameN  # exact frame index
            earth_move.tStart = t  # local t and not account for scr refresh
            earth_move.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earth_move, 'tStartRefresh')  # time at next scr refresh
            earth_move.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_move* updates
        waitOnFlip = False
        if key_resp_move.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_move.frameNStart = frameN  # exact frame index
            key_resp_move.tStart = t  # local t and not account for scr refresh
            key_resp_move.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_move, 'tStartRefresh')  # time at next scr refresh
            key_resp_move.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_move.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_move.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_move.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_move.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_move_allKeys.extend(theseKeys)
            if len(_key_resp_move_allKeys):
                key_resp_move.keys = _key_resp_move_allKeys[-1].name  # just the last key pressed
                key_resp_move.rt = _key_resp_move_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceMove_earthComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceMove_earth"-------
    for thisComponent in practiceMove_earthComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('shield_move.started', shield_move.tStartRefresh)
    trials.addData('shield_move.stopped', shield_move.tStopRefresh)
    trials.addData('shield_centre_move.started', shield_centre_move.tStartRefresh)
    trials.addData('shield_centre_move.stopped', shield_centre_move.tStopRefresh)
    trials.addData('earth_move.started', earth_move.tStartRefresh)
    trials.addData('earth_move.stopped', earth_move.tStopRefresh)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_move.keys in ['', [], None]:  # No response was made
        key_resp_move.keys = None
    trials.addData('key_resp_move.keys',key_resp_move.keys)
    if key_resp_move.keys != None:  # we had a response
        trials.addData('key_resp_move.rt', key_resp_move.rt)
    trials.addData('key_resp_move.started', key_resp_move.tStartRefresh)
    trials.addData('key_resp_move.stopped', key_resp_move.tStopRefresh)
    # the Routine "practiceMove_earth" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practiceSize_earth"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    kb = keyboard.Keyboard()
    
    #set constants for the experiment
    SHIELD_GROWTH_SPEED = 20; #in degrees
    CIRCLE_RADIUS = 3;
    
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 45; #because it needs to be predefined
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    
    minShieldDegrees = 25;
    maxShieldDegrees = 65;
    
    shieldRotation = 0; #begin at top
    key_resp_size.keys = []
    key_resp_size.rt = []
    _key_resp_size_allKeys = []
    # keep track of which components have finished
    practiceSize_earthComponents = [shield_size, shield_centre_size, earth_size, text_4, key_resp_size]
    for thisComponent in practiceSize_earthComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceSize_earthClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceSize_earth"-------
    while continueRoutine:
        # get current time
        t = practiceSize_earthClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceSize_earthClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        UDkeys_pressed = kb.getKeys(keyList=['up','down'],clear=True,waitRelease=False)
        
        if len(UDkeys_pressed)>0:
            if UDkeys_pressed[-1]=='up':
                shieldDegrees += SHIELD_GROWTH_SPEED;
            if UDkeys_pressed[-1]=='down':
                shieldDegrees -= SHIELD_GROWTH_SPEED;
        
        #set lower boundary on shieldWidth
        if shieldDegrees < minShieldDegrees:
            shieldDegrees = minShieldDegrees;
            
        #set upper boundary on shieldWidth
        if shieldDegrees > maxShieldDegrees:
            shieldDegrees = maxShieldDegrees;
            
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldX = np.concatenate(([0],shieldX));
        shieldY = np.concatenate(([0],shieldY));
        shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
        
        # *shield_size* updates
        if shield_size.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            shield_size.frameNStart = frameN  # exact frame index
            shield_size.tStart = t  # local t and not account for scr refresh
            shield_size.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_size, 'tStartRefresh')  # time at next scr refresh
            shield_size.setAutoDraw(True)
        if shield_size.status == STARTED:  # only update if drawing
            shield_size.setVertices(shieldCoords, log=False)
        
        # *shield_centre_size* updates
        if shield_centre_size.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            shield_centre_size.frameNStart = frameN  # exact frame index
            shield_centre_size.tStart = t  # local t and not account for scr refresh
            shield_centre_size.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre_size, 'tStartRefresh')  # time at next scr refresh
            shield_centre_size.setAutoDraw(True)
        if shield_centre_size.status == STARTED:  # only update if drawing
            shield_centre_size.setPos((0, 0), log=False)
        
        # *earth_size* updates
        if earth_size.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            earth_size.frameNStart = frameN  # exact frame index
            earth_size.tStart = t  # local t and not account for scr refresh
            earth_size.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earth_size, 'tStartRefresh')  # time at next scr refresh
            earth_size.setAutoDraw(True)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_size* updates
        waitOnFlip = False
        if key_resp_size.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_size.frameNStart = frameN  # exact frame index
            key_resp_size.tStart = t  # local t and not account for scr refresh
            key_resp_size.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_size, 'tStartRefresh')  # time at next scr refresh
            key_resp_size.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_size.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_size.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_size.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_size.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_size_allKeys.extend(theseKeys)
            if len(_key_resp_size_allKeys):
                key_resp_size.keys = _key_resp_size_allKeys[-1].name  # just the last key pressed
                key_resp_size.rt = _key_resp_size_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceSize_earthComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceSize_earth"-------
    for thisComponent in practiceSize_earthComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('shield_size.started', shield_size.tStartRefresh)
    trials.addData('shield_size.stopped', shield_size.tStopRefresh)
    trials.addData('shield_centre_size.started', shield_centre_size.tStartRefresh)
    trials.addData('shield_centre_size.stopped', shield_centre_size.tStopRefresh)
    trials.addData('earth_size.started', earth_size.tStartRefresh)
    trials.addData('earth_size.stopped', earth_size.tStopRefresh)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_size.keys in ['', [], None]:  # No response was made
        key_resp_size.keys = None
    trials.addData('key_resp_size.keys',key_resp_size.keys)
    if key_resp_size.keys != None:  # we had a response
        trials.addData('key_resp_size.rt', key_resp_size.rt)
    trials.addData('key_resp_size.started', key_resp_size.tStartRefresh)
    trials.addData('key_resp_size.stopped', key_resp_size.tStopRefresh)
    # the Routine "practiceSize_earth" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_earth"-------
    continueRoutine = True
    # update component parameters for each repeat
    import pandas as pd;
    import numpy as np;
    import math;
    import os;
    
    kb = keyboard.Keyboard()
    rootdir = os.getcwd()
    
    #set constants for the experiment
    ROTATION_SPEED = 1;
    SHIELD_GROWTH_SPEED = 20; #in degrees
    SHIELD_DECAY_RATE = 0.99; #decay rate after hitting shield
    CIRCLE_RADIUS = 3;
    
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 45; #because it needs to be predefined
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    shieldRedness = 0;
    minShieldDegrees = 25;
    maxShieldDegrees = 65;
    totalReward = 0;
    
    #initialise list containing data to be saved
    saveData = [["currentFrame","laserRotation","shieldRotation","shieldDegrees","currentHit","totalReward"]]
    saveFilename = "savedData.csv"#load stimulusStream into NumPy array
    
    #load stimulusStream into NumPy array
    stimStreamPath = os.path.join(rootdir,'stimgen',blockFileName)
    storedStream_np = np.loadtxt(stimStreamPath,delimiter=",")
    #storedStream_np = np.loadtxt('/Users/lhunt/home/python/PsychoPy/experiments/rotation_task/stimgen/rotation_stream.csv',delimiter=",");
    
    #calculate the total number of frames in the experiment
    nFrames = np.shape(storedStream_np)[0] - 1;
    currentFrame = 0;
    laserRotation = storedStream_np[0,1];
    shieldRotation = 0; #begin at top
    
    #update variables to draw polygon
    laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
    laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
    
    laser_2.setPos((0, 0))
    laser_2.setSize((1, 1))
    # keep track of which components have finished
    trial_earthComponents = [laser_2, shield_2, shield_centre_2, shield_background_2, reward_text_2, earth_2]
    for thisComponent in trial_earthComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_earthClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_earth"-------
    while continueRoutine:
        # get current time
        t = trial_earthClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_earthClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=False)
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=False,waitRelease=False)
        
        UDkeys_pressed = kb.getKeys(keyList=['up','down'],clear=True,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]=='right':
                shieldRotation += ROTATION_SPEED;
            if LRkeys_pressed[-1]=='left':
                shieldRotation -= ROTATION_SPEED;
        if len(UDkeys_pressed)>0:
            if UDkeys_pressed[-1]=='up':
                shieldDegrees += SHIELD_GROWTH_SPEED;
            if UDkeys_pressed[-1]=='down':
                shieldDegrees -= SHIELD_GROWTH_SPEED;
        
        #set lower boundary on shieldWidth
        if shieldDegrees < minShieldDegrees:
            shieldDegrees = minShieldDegrees;
            
        #set upper boundary on shieldWidth
        if shieldDegrees > maxShieldDegrees:
            shieldDegrees = maxShieldDegrees;
            
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldX = np.concatenate(([0],shieldX));
        shieldY = np.concatenate(([0],shieldY));
        shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
        
        
        
        if currentFrame<nFrames:
            laserRotation = storedStream_np[currentFrame,1];
        
        #calculate whether shield is currently hit by laser
        currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            update = (minShieldDegrees/50)/shieldDegrees;
            shieldRedness = min(shieldRedness + update,2);
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            #laserColour = [1,-1,-1];
        else:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            #laserColour = [1,1,1];
        
        totalReward = totalReward + shieldRedness/100;
        textReward = str(round(totalReward, 1))
        
        if currentFrame<nFrames:
            saveData.append([currentFrame,laserRotation,shieldRotation,shieldDegrees,currentHit,totalReward])
            currentFrame = currentFrame + 1;
        
        
        # *laser_2* updates
        if laser_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser_2.frameNStart = frameN  # exact frame index
            laser_2.tStart = t  # local t and not account for scr refresh
            laser_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser_2, 'tStartRefresh')  # time at next scr refresh
            laser_2.setAutoDraw(True)
        if laser_2.status == STARTED:
            if frameN >= (laser_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser_2.tStop = t  # not accounting for scr refresh
                laser_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser_2, 'tStopRefresh')  # time at next scr refresh
                laser_2.setAutoDraw(False)
        if laser_2.status == STARTED:  # only update if drawing
            laser_2.setOri(laserRotation, log=False)
            laser_2.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
        
        # *shield_2* updates
        if shield_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_2.frameNStart = frameN  # exact frame index
            shield_2.tStart = t  # local t and not account for scr refresh
            shield_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_2, 'tStartRefresh')  # time at next scr refresh
            shield_2.setAutoDraw(True)
        if shield_2.status == STARTED:
            if frameN >= (shield_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_2.tStop = t  # not accounting for scr refresh
                shield_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_2, 'tStopRefresh')  # time at next scr refresh
                shield_2.setAutoDraw(False)
        if shield_2.status == STARTED:  # only update if drawing
            shield_2.setFillColor(shieldColour, log=False)
            shield_2.setOri(shieldRotation, log=False)
            shield_2.setVertices(shieldCoords, log=False)
            shield_2.setLineColor([0, 0, 0], log=False)
        
        # *shield_centre_2* updates
        if shield_centre_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_centre_2.frameNStart = frameN  # exact frame index
            shield_centre_2.tStart = t  # local t and not account for scr refresh
            shield_centre_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre_2, 'tStartRefresh')  # time at next scr refresh
            shield_centre_2.setAutoDraw(True)
        if shield_centre_2.status == STARTED:
            if frameN >= (shield_centre_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_centre_2.tStop = t  # not accounting for scr refresh
                shield_centre_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_centre_2, 'tStopRefresh')  # time at next scr refresh
                shield_centre_2.setAutoDraw(False)
        if shield_centre_2.status == STARTED:  # only update if drawing
            shield_centre_2.setPos((0, 0), log=False)
            shield_centre_2.setOri(shieldRotation, log=False)
        
        # *shield_background_2* updates
        if shield_background_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_background_2.frameNStart = frameN  # exact frame index
            shield_background_2.tStart = t  # local t and not account for scr refresh
            shield_background_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_background_2, 'tStartRefresh')  # time at next scr refresh
            shield_background_2.setAutoDraw(True)
        if shield_background_2.status == STARTED:
            if frameN >= (shield_background_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_background_2.tStop = t  # not accounting for scr refresh
                shield_background_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_background_2, 'tStopRefresh')  # time at next scr refresh
                shield_background_2.setAutoDraw(False)
        if shield_background_2.status == STARTED:  # only update if drawing
            shield_background_2.setFillColor([0, 0, 0], log=False)
            shield_background_2.setOri(shieldRotation, log=False)
            shield_background_2.setVertices(shieldCoords, log=False)
            shield_background_2.setLineColor([0, 0, 0], log=False)
        
        # *reward_text_2* updates
        if reward_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reward_text_2.frameNStart = frameN  # exact frame index
            reward_text_2.tStart = t  # local t and not account for scr refresh
            reward_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_text_2, 'tStartRefresh')  # time at next scr refresh
            reward_text_2.setAutoDraw(True)
        if reward_text_2.status == STARTED:
            if frameN >= (reward_text_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                reward_text_2.tStop = t  # not accounting for scr refresh
                reward_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reward_text_2, 'tStopRefresh')  # time at next scr refresh
                reward_text_2.setAutoDraw(False)
        if reward_text_2.status == STARTED:  # only update if drawing
            reward_text_2.setText(textReward, log=False)
        
        # *earth_2* updates
        if earth_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            earth_2.frameNStart = frameN  # exact frame index
            earth_2.tStart = t  # local t and not account for scr refresh
            earth_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earth_2, 'tStartRefresh')  # time at next scr refresh
            earth_2.setAutoDraw(True)
        if earth_2.status == STARTED:
            if frameN >= (earth_2.frameNStart + nFrames):
                # keep track of stop time/frame for later
                earth_2.tStop = t  # not accounting for scr refresh
                earth_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(earth_2, 'tStopRefresh')  # time at next scr refresh
                earth_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_earthComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_earth"-------
    for thisComponent in trial_earthComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    
    trials.addData('laser_2.started', laser_2.tStartRefresh)
    trials.addData('laser_2.stopped', laser_2.tStopRefresh)
    trials.addData('shield_2.started', shield_2.tStartRefresh)
    trials.addData('shield_2.stopped', shield_2.tStopRefresh)
    trials.addData('shield_centre_2.started', shield_centre_2.tStartRefresh)
    trials.addData('shield_centre_2.stopped', shield_centre_2.tStopRefresh)
    trials.addData('shield_background_2.started', shield_background_2.tStartRefresh)
    trials.addData('shield_background_2.stopped', shield_background_2.tStopRefresh)
    trials.addData('reward_text_2.started', reward_text_2.tStartRefresh)
    trials.addData('reward_text_2.stopped', reward_text_2.tStopRefresh)
    trials.addData('earth_2.started', earth_2.tStartRefresh)
    trials.addData('earth_2.stopped', earth_2.tStopRefresh)
    # the Routine "trial_earth" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_sun"-------
    continueRoutine = True
    # update component parameters for each repeat
    import pandas as pd;
    import numpy as np;
    import math;
    import os;
    
    kb = keyboard.Keyboard()
    rootdir = os.getcwd()
    
    #set constants for the experiment
    ROTATION_SPEED = 1;
    SHIELD_GROWTH_SPEED = 20; #in degrees
    SHIELD_DECAY_RATE = 0.99; #decay rate after hitting shield
    CIRCLE_RADIUS = 3;
    
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 45; #because it needs to be predefined
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    shieldRedness = 0;
    minShieldDegrees = 25;
    maxShieldDegrees = 65;
    totalReward = 0;
    
    #initialise list containing data to be saved
    saveData = [["currentFrame","laserRotation","shieldRotation","shieldDegrees","currentHit","totalReward"]]
    saveFilename = "savedData.csv"#load stimulusStream into NumPy array
    
    #load stimulusStream into NumPy array
    stimStreamPath = os.path.join(rootdir,'stimgen',blockFileName)
    storedStream_np = np.loadtxt(stimStreamPath,delimiter=",")
    #storedStream_np = np.loadtxt('/Users/lhunt/home/python/PsychoPy/experiments/rotation_task/stimgen/rotation_stream.csv',delimiter=",");
    
    #calculate the total number of frames in the experiment
    nFrames = np.shape(storedStream_np)[0] - 1;
    currentFrame = 0;
    laserRotation = storedStream_np[0,1];
    shieldRotation = 0; #begin at top
    
    #update variables to draw polygon
    laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
    laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
    
    laser_3.setPos((0, 0))
    laser_3.setSize((1, 1))
    # keep track of which components have finished
    trial_sunComponents = [shield_background_long_3, shield_3, shield_centre_3, shield_background_short_3, laser_3, sun]
    for thisComponent in trial_sunComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_sunClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_sun"-------
    while continueRoutine:
        # get current time
        t = trial_sunClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_sunClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=True,waitRelease=False)
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=['right','left'],clear=False,waitRelease=False)
        
        UDkeys_pressed = kb.getKeys(keyList=['up','down'],clear=True,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]=='right':
                shieldRotation += ROTATION_SPEED;
            if LRkeys_pressed[-1]=='left':
                shieldRotation -= ROTATION_SPEED;
        if len(UDkeys_pressed)>0:
            if UDkeys_pressed[-1]=='up':
                shieldDegrees += SHIELD_GROWTH_SPEED;
            if UDkeys_pressed[-1]=='down':
                shieldDegrees -= SHIELD_GROWTH_SPEED;
        
        #set lower boundary on shieldWidth
        if shieldDegrees < minShieldDegrees:
            shieldDegrees = minShieldDegrees;
            
        #set upper boundary on shieldWidth
        if shieldDegrees > maxShieldDegrees:
            shieldDegrees = maxShieldDegrees;
            
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldX = np.concatenate(([0],shieldX));
        shieldY = np.concatenate(([0],shieldY));
        shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
        
        
        
        if currentFrame<nFrames:
            laserRotation = storedStream_np[currentFrame,1];
        
        #calculate whether shield is currently hit by laser
        currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            update = (minShieldDegrees/50)/shieldDegrees;
            shieldRedness = min(shieldRedness + update,2);
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            #laserColour = [1,-1,-1];
        else:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            #laserColour = [1,1,1];
        
        totalReward = totalReward + shieldRedness/100;
        textReward = str(round(totalReward, 1))
        
        if currentFrame<nFrames:
            saveData.append([currentFrame,laserRotation,shieldRotation,shieldDegrees,currentHit,totalReward])
            currentFrame = currentFrame + 1;
        
        
        # *shield_background_long_3* updates
        if shield_background_long_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_background_long_3.frameNStart = frameN  # exact frame index
            shield_background_long_3.tStart = t  # local t and not account for scr refresh
            shield_background_long_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_background_long_3, 'tStartRefresh')  # time at next scr refresh
            shield_background_long_3.setAutoDraw(True)
        if shield_background_long_3.status == STARTED:
            if frameN >= (shield_background_long_3.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_background_long_3.tStop = t  # not accounting for scr refresh
                shield_background_long_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_background_long_3, 'tStopRefresh')  # time at next scr refresh
                shield_background_long_3.setAutoDraw(False)
        if shield_background_long_3.status == STARTED:  # only update if drawing
            shield_background_long_3.setFillColor([0, 0, 0], log=False)
            shield_background_long_3.setOri(shieldRotation, log=False)
            shield_background_long_3.setVertices(shieldCoords, log=False)
            shield_background_long_3.setLineColor([0, 0, 0], log=False)
        
        # *shield_3* updates
        if shield_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_3.frameNStart = frameN  # exact frame index
            shield_3.tStart = t  # local t and not account for scr refresh
            shield_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_3, 'tStartRefresh')  # time at next scr refresh
            shield_3.setAutoDraw(True)
        if shield_3.status == STARTED:
            if frameN >= (shield_3.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_3.tStop = t  # not accounting for scr refresh
                shield_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_3, 'tStopRefresh')  # time at next scr refresh
                shield_3.setAutoDraw(False)
        if shield_3.status == STARTED:  # only update if drawing
            shield_3.setFillColor(shieldColour, log=False)
            shield_3.setOri(shieldRotation, log=False)
            shield_3.setVertices(shieldCoords, log=False)
            shield_3.setLineColor([0, 0, 0], log=False)
        
        # *shield_centre_3* updates
        if shield_centre_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_centre_3.frameNStart = frameN  # exact frame index
            shield_centre_3.tStart = t  # local t and not account for scr refresh
            shield_centre_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre_3, 'tStartRefresh')  # time at next scr refresh
            shield_centre_3.setAutoDraw(True)
        if shield_centre_3.status == STARTED:
            if frameN >= (shield_centre_3.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_centre_3.tStop = t  # not accounting for scr refresh
                shield_centre_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_centre_3, 'tStopRefresh')  # time at next scr refresh
                shield_centre_3.setAutoDraw(False)
        if shield_centre_3.status == STARTED:  # only update if drawing
            shield_centre_3.setPos((0, 0), log=False)
            shield_centre_3.setOri(shieldRotation, log=False)
        
        # *shield_background_short_3* updates
        if shield_background_short_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_background_short_3.frameNStart = frameN  # exact frame index
            shield_background_short_3.tStart = t  # local t and not account for scr refresh
            shield_background_short_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_background_short_3, 'tStartRefresh')  # time at next scr refresh
            shield_background_short_3.setAutoDraw(True)
        if shield_background_short_3.status == STARTED:
            if frameN >= (shield_background_short_3.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_background_short_3.tStop = t  # not accounting for scr refresh
                shield_background_short_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_background_short_3, 'tStopRefresh')  # time at next scr refresh
                shield_background_short_3.setAutoDraw(False)
        if shield_background_short_3.status == STARTED:  # only update if drawing
            shield_background_short_3.setFillColor([0, 0, 0], log=False)
            shield_background_short_3.setOri(shieldRotation, log=False)
            shield_background_short_3.setVertices(shieldCoords, log=False)
            shield_background_short_3.setLineColor([0, 0, 0], log=False)
        
        # *laser_3* updates
        if laser_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser_3.frameNStart = frameN  # exact frame index
            laser_3.tStart = t  # local t and not account for scr refresh
            laser_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser_3, 'tStartRefresh')  # time at next scr refresh
            laser_3.setAutoDraw(True)
        if laser_3.status == STARTED:
            if frameN >= (laser_3.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser_3.tStop = t  # not accounting for scr refresh
                laser_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser_3, 'tStopRefresh')  # time at next scr refresh
                laser_3.setAutoDraw(False)
        if laser_3.status == STARTED:  # only update if drawing
            laser_3.setOri(laserRotation, log=False)
            laser_3.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.2]], log=False)
        
        # *sun* updates
        if sun.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sun.frameNStart = frameN  # exact frame index
            sun.tStart = t  # local t and not account for scr refresh
            sun.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sun, 'tStartRefresh')  # time at next scr refresh
            sun.setAutoDraw(True)
        if sun.status == STARTED:
            if frameN >= (sun.frameNStart + nFrames):
                # keep track of stop time/frame for later
                sun.tStop = t  # not accounting for scr refresh
                sun.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sun, 'tStopRefresh')  # time at next scr refresh
                sun.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_sunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_sun"-------
    for thisComponent in trial_sunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    
    trials.addData('shield_background_long_3.started', shield_background_long_3.tStartRefresh)
    trials.addData('shield_background_long_3.stopped', shield_background_long_3.tStopRefresh)
    trials.addData('shield_3.started', shield_3.tStartRefresh)
    trials.addData('shield_3.stopped', shield_3.tStopRefresh)
    trials.addData('shield_centre_3.started', shield_centre_3.tStartRefresh)
    trials.addData('shield_centre_3.stopped', shield_centre_3.tStopRefresh)
    trials.addData('shield_background_short_3.started', shield_background_short_3.tStartRefresh)
    trials.addData('shield_background_short_3.stopped', shield_background_short_3.tStopRefresh)
    trials.addData('laser_3.started', laser_3.tStartRefresh)
    trials.addData('laser_3.stopped', laser_3.tStopRefresh)
    trials.addData('sun.started', sun.tStartRefresh)
    trials.addData('sun.stopped', sun.tStopRefresh)
    # the Routine "trial_sun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials'


# ------Prepare to start Routine "practiceMove_radio"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_move_radio.keys = []
key_resp_move_radio.rt = []
_key_resp_move_radio_allKeys = []
# keep track of which components have finished
practiceMove_radioComponents = [shield_move_radio, shield_centre_move_radio, shield_background_short_move, radioactive_move, text_move_radio, text_advance_move, key_resp_move_radio]
for thisComponent in practiceMove_radioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceMove_radioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceMove_radio"-------
while continueRoutine:
    # get current time
    t = practiceMove_radioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceMove_radioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #first, find out if L/R keys have been *released*
    LRkeys_released = kb.getKeys(keyList=['1','2'],clear=True,waitRelease=True)
    if len(LRkeys_released)>0: #if so, then flush out the keys one final time
        LRkeys_pressed = kb.getKeys(keyList=['1','2'],clear=True,waitRelease=False)
    else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
        LRkeys_pressed = kb.getKeys(keyList=['1','2'],clear=False,waitRelease=False)
    
    #if key is pressed, rotate cursor
    #using most recently pressed key
    if len(LRkeys_pressed)>0:
        if LRkeys_pressed[-1]=='1':
            shieldRotation += ROTATION_SPEED;
        if LRkeys_pressed[-1]=='2':
            shieldRotation -= ROTATION_SPEED;
    
    # *shield_move_radio* updates
    if shield_move_radio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_move_radio.frameNStart = frameN  # exact frame index
        shield_move_radio.tStart = t  # local t and not account for scr refresh
        shield_move_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_move_radio, 'tStartRefresh')  # time at next scr refresh
        shield_move_radio.setAutoDraw(True)
    if shield_move_radio.status == STARTED:  # only update if drawing
        shield_move_radio.setOri(shieldRotation, log=False)
    
    # *shield_centre_move_radio* updates
    if shield_centre_move_radio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_centre_move_radio.frameNStart = frameN  # exact frame index
        shield_centre_move_radio.tStart = t  # local t and not account for scr refresh
        shield_centre_move_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_centre_move_radio, 'tStartRefresh')  # time at next scr refresh
        shield_centre_move_radio.setAutoDraw(True)
    if shield_centre_move_radio.status == STARTED:  # only update if drawing
        shield_centre_move_radio.setPos((0, -3), log=False)
        shield_centre_move_radio.setOri(shieldRotation, log=False)
    
    # *shield_background_short_move* updates
    if shield_background_short_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_background_short_move.frameNStart = frameN  # exact frame index
        shield_background_short_move.tStart = t  # local t and not account for scr refresh
        shield_background_short_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_background_short_move, 'tStartRefresh')  # time at next scr refresh
        shield_background_short_move.setAutoDraw(True)
    if shield_background_short_move.status == STARTED:  # only update if drawing
        shield_background_short_move.setFillColor([0, 0, 0], log=False)
        shield_background_short_move.setOri(shieldRotation, log=False)
        shield_background_short_move.setVertices(shieldCoords, log=False)
        shield_background_short_move.setLineColor([0, 0, 0], log=False)
    
    # *radioactive_move* updates
    if radioactive_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        radioactive_move.frameNStart = frameN  # exact frame index
        radioactive_move.tStart = t  # local t and not account for scr refresh
        radioactive_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radioactive_move, 'tStartRefresh')  # time at next scr refresh
        radioactive_move.setAutoDraw(True)
    
    # *text_move_radio* updates
    if text_move_radio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_move_radio.frameNStart = frameN  # exact frame index
        text_move_radio.tStart = t  # local t and not account for scr refresh
        text_move_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_move_radio, 'tStartRefresh')  # time at next scr refresh
        text_move_radio.setAutoDraw(True)
    
    # *text_advance_move* updates
    if text_advance_move.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_advance_move.frameNStart = frameN  # exact frame index
        text_advance_move.tStart = t  # local t and not account for scr refresh
        text_advance_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_advance_move, 'tStartRefresh')  # time at next scr refresh
        text_advance_move.setAutoDraw(True)
    
    # *key_resp_move_radio* updates
    waitOnFlip = False
    if key_resp_move_radio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_move_radio.frameNStart = frameN  # exact frame index
        key_resp_move_radio.tStart = t  # local t and not account for scr refresh
        key_resp_move_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_move_radio, 'tStartRefresh')  # time at next scr refresh
        key_resp_move_radio.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_move_radio.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_move_radio.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_move_radio.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_move_radio.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_move_radio_allKeys.extend(theseKeys)
        if len(_key_resp_move_radio_allKeys):
            key_resp_move_radio.keys = _key_resp_move_radio_allKeys[-1].name  # just the last key pressed
            key_resp_move_radio.rt = _key_resp_move_radio_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceMove_radioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceMove_radio"-------
for thisComponent in practiceMove_radioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('shield_move_radio.started', shield_move_radio.tStartRefresh)
thisExp.addData('shield_move_radio.stopped', shield_move_radio.tStopRefresh)
thisExp.addData('shield_centre_move_radio.started', shield_centre_move_radio.tStartRefresh)
thisExp.addData('shield_centre_move_radio.stopped', shield_centre_move_radio.tStopRefresh)
thisExp.addData('shield_background_short_move.started', shield_background_short_move.tStartRefresh)
thisExp.addData('shield_background_short_move.stopped', shield_background_short_move.tStopRefresh)
thisExp.addData('radioactive_move.started', radioactive_move.tStartRefresh)
thisExp.addData('radioactive_move.stopped', radioactive_move.tStopRefresh)
thisExp.addData('text_move_radio.started', text_move_radio.tStartRefresh)
thisExp.addData('text_move_radio.stopped', text_move_radio.tStopRefresh)
thisExp.addData('text_advance_move.started', text_advance_move.tStartRefresh)
thisExp.addData('text_advance_move.stopped', text_advance_move.tStopRefresh)
# check responses
if key_resp_move_radio.keys in ['', [], None]:  # No response was made
    key_resp_move_radio.keys = None
thisExp.addData('key_resp_move_radio.keys',key_resp_move_radio.keys)
if key_resp_move_radio.keys != None:  # we had a response
    thisExp.addData('key_resp_move_radio.rt', key_resp_move_radio.rt)
thisExp.addData('key_resp_move_radio.started', key_resp_move_radio.tStartRefresh)
thisExp.addData('key_resp_move_radio.stopped', key_resp_move_radio.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceMove_radio" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sizeExamples_ratio"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_size_examples.keys = []
key_resp_size_examples.rt = []
_key_resp_size_examples_allKeys = []
# keep track of which components have finished
sizeExamples_ratioComponents = [text_size_examples, text_size_advance, shield_small, shield_medium, shield_large, key_resp_size_examples]
for thisComponent in sizeExamples_ratioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sizeExamples_ratioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sizeExamples_ratio"-------
while continueRoutine:
    # get current time
    t = sizeExamples_ratioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sizeExamples_ratioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_size_examples* updates
    if text_size_examples.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_size_examples.frameNStart = frameN  # exact frame index
        text_size_examples.tStart = t  # local t and not account for scr refresh
        text_size_examples.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_size_examples, 'tStartRefresh')  # time at next scr refresh
        text_size_examples.setAutoDraw(True)
    
    # *text_size_advance* updates
    if text_size_advance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_size_advance.frameNStart = frameN  # exact frame index
        text_size_advance.tStart = t  # local t and not account for scr refresh
        text_size_advance.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_size_advance, 'tStartRefresh')  # time at next scr refresh
        text_size_advance.setAutoDraw(True)
    
    # *shield_small* updates
    if shield_small.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shield_small.frameNStart = frameN  # exact frame index
        shield_small.tStart = t  # local t and not account for scr refresh
        shield_small.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_small, 'tStartRefresh')  # time at next scr refresh
        shield_small.setAutoDraw(True)
    
    # *shield_medium* updates
    if shield_medium.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shield_medium.frameNStart = frameN  # exact frame index
        shield_medium.tStart = t  # local t and not account for scr refresh
        shield_medium.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_medium, 'tStartRefresh')  # time at next scr refresh
        shield_medium.setAutoDraw(True)
    
    # *shield_large* updates
    if shield_large.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shield_large.frameNStart = frameN  # exact frame index
        shield_large.tStart = t  # local t and not account for scr refresh
        shield_large.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_large, 'tStartRefresh')  # time at next scr refresh
        shield_large.setAutoDraw(True)
    
    # *key_resp_size_examples* updates
    waitOnFlip = False
    if key_resp_size_examples.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_size_examples.frameNStart = frameN  # exact frame index
        key_resp_size_examples.tStart = t  # local t and not account for scr refresh
        key_resp_size_examples.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_size_examples, 'tStartRefresh')  # time at next scr refresh
        key_resp_size_examples.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_size_examples.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_size_examples.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_size_examples.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_size_examples.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_size_examples_allKeys.extend(theseKeys)
        if len(_key_resp_size_examples_allKeys):
            key_resp_size_examples.keys = _key_resp_size_examples_allKeys[-1].name  # just the last key pressed
            key_resp_size_examples.rt = _key_resp_size_examples_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sizeExamples_ratioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sizeExamples_ratio"-------
for thisComponent in sizeExamples_ratioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_size_examples.started', text_size_examples.tStartRefresh)
thisExp.addData('text_size_examples.stopped', text_size_examples.tStopRefresh)
thisExp.addData('text_size_advance.started', text_size_advance.tStartRefresh)
thisExp.addData('text_size_advance.stopped', text_size_advance.tStopRefresh)
thisExp.addData('shield_small.started', shield_small.tStartRefresh)
thisExp.addData('shield_small.stopped', shield_small.tStopRefresh)
thisExp.addData('shield_medium.started', shield_medium.tStartRefresh)
thisExp.addData('shield_medium.stopped', shield_medium.tStopRefresh)
thisExp.addData('shield_large.started', shield_large.tStartRefresh)
thisExp.addData('shield_large.stopped', shield_large.tStopRefresh)
# check responses
if key_resp_size_examples.keys in ['', [], None]:  # No response was made
    key_resp_size_examples.keys = None
thisExp.addData('key_resp_size_examples.keys',key_resp_size_examples.keys)
if key_resp_size_examples.keys != None:  # we had a response
    thisExp.addData('key_resp_size_examples.rt', key_resp_size_examples.rt)
thisExp.addData('key_resp_size_examples.started', key_resp_size_examples.tStartRefresh)
thisExp.addData('key_resp_size_examples.stopped', key_resp_size_examples.tStopRefresh)
thisExp.nextEntry()
# the Routine "sizeExamples_ratio" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceSize_radio"-------
continueRoutine = True
# update component parameters for each repeat

kb = keyboard.Keyboard()

#set constants for the experiment
SHIELD_GROWTH_SPEED = 20; #in degrees

minShieldDegrees = 25;
maxShieldDegrees = 65;
key_resp_radio_size.keys = []
key_resp_radio_size.rt = []
_key_resp_radio_size_allKeys = []
# keep track of which components have finished
practiceSize_radioComponents = [shield_size_radio, shield_centre_size_radio, shield_background_short_size, radio_size, text_radio_size, key_resp_radio_size]
for thisComponent in practiceSize_radioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceSize_radioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceSize_radio"-------
while continueRoutine:
    # get current time
    t = practiceSize_radioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceSize_radioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    UDkeys_pressed = kb.getKeys(keyList=['3','4'],clear=True,waitRelease=False)
    
    if len(UDkeys_pressed)>0:
        if UDkeys_pressed[-1]=='3':
            shieldDegrees += SHIELD_GROWTH_SPEED;
        if UDkeys_pressed[-1]=='4':
            shieldDegrees -= SHIELD_GROWTH_SPEED;
    
    #set lower boundary on shieldWidth
    if shieldDegrees < minShieldDegrees:
        shieldDegrees = minShieldDegrees;
        
    #set upper boundary on shieldWidth
    if shieldDegrees > maxShieldDegrees:
        shieldDegrees = maxShieldDegrees;
        
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    
    # *shield_size_radio* updates
    if shield_size_radio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_size_radio.frameNStart = frameN  # exact frame index
        shield_size_radio.tStart = t  # local t and not account for scr refresh
        shield_size_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_size_radio, 'tStartRefresh')  # time at next scr refresh
        shield_size_radio.setAutoDraw(True)
    if shield_size_radio.status == STARTED:  # only update if drawing
        shield_size_radio.setVertices(shieldCoords, log=False)
    
    # *shield_centre_size_radio* updates
    if shield_centre_size_radio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_centre_size_radio.frameNStart = frameN  # exact frame index
        shield_centre_size_radio.tStart = t  # local t and not account for scr refresh
        shield_centre_size_radio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_centre_size_radio, 'tStartRefresh')  # time at next scr refresh
        shield_centre_size_radio.setAutoDraw(True)
    
    # *shield_background_short_size* updates
    if shield_background_short_size.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_background_short_size.frameNStart = frameN  # exact frame index
        shield_background_short_size.tStart = t  # local t and not account for scr refresh
        shield_background_short_size.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_background_short_size, 'tStartRefresh')  # time at next scr refresh
        shield_background_short_size.setAutoDraw(True)
    if shield_background_short_size.status == STARTED:  # only update if drawing
        shield_background_short_size.setFillColor([0, 0, 0], log=False)
        shield_background_short_size.setVertices(shieldCoords, log=False)
        shield_background_short_size.setLineColor([0, 0, 0], log=False)
    
    # *radio_size* updates
    if radio_size.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        radio_size.frameNStart = frameN  # exact frame index
        radio_size.tStart = t  # local t and not account for scr refresh
        radio_size.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radio_size, 'tStartRefresh')  # time at next scr refresh
        radio_size.setAutoDraw(True)
    
    # *text_radio_size* updates
    if text_radio_size.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_radio_size.frameNStart = frameN  # exact frame index
        text_radio_size.tStart = t  # local t and not account for scr refresh
        text_radio_size.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_radio_size, 'tStartRefresh')  # time at next scr refresh
        text_radio_size.setAutoDraw(True)
    
    # *key_resp_radio_size* updates
    waitOnFlip = False
    if key_resp_radio_size.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_radio_size.frameNStart = frameN  # exact frame index
        key_resp_radio_size.tStart = t  # local t and not account for scr refresh
        key_resp_radio_size.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_radio_size, 'tStartRefresh')  # time at next scr refresh
        key_resp_radio_size.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_radio_size.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_radio_size.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_radio_size.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_radio_size.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_radio_size_allKeys.extend(theseKeys)
        if len(_key_resp_radio_size_allKeys):
            key_resp_radio_size.keys = _key_resp_radio_size_allKeys[-1].name  # just the last key pressed
            key_resp_radio_size.rt = _key_resp_radio_size_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceSize_radioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceSize_radio"-------
for thisComponent in practiceSize_radioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('shield_size_radio.started', shield_size_radio.tStartRefresh)
thisExp.addData('shield_size_radio.stopped', shield_size_radio.tStopRefresh)
thisExp.addData('shield_centre_size_radio.started', shield_centre_size_radio.tStartRefresh)
thisExp.addData('shield_centre_size_radio.stopped', shield_centre_size_radio.tStopRefresh)
thisExp.addData('shield_background_short_size.started', shield_background_short_size.tStartRefresh)
thisExp.addData('shield_background_short_size.stopped', shield_background_short_size.tStopRefresh)
thisExp.addData('radio_size.started', radio_size.tStartRefresh)
thisExp.addData('radio_size.stopped', radio_size.tStopRefresh)
thisExp.addData('text_radio_size.started', text_radio_size.tStartRefresh)
thisExp.addData('text_radio_size.stopped', text_radio_size.tStopRefresh)
# check responses
if key_resp_radio_size.keys in ['', [], None]:  # No response was made
    key_resp_radio_size.keys = None
thisExp.addData('key_resp_radio_size.keys',key_resp_radio_size.keys)
if key_resp_radio_size.keys != None:  # we had a response
    thisExp.addData('key_resp_radio_size.rt', key_resp_radio_size.rt)
thisExp.addData('key_resp_radio_size.started', key_resp_radio_size.tStartRefresh)
thisExp.addData('key_resp_radio_size.stopped', key_resp_radio_size.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceSize_radio" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimgen/blocks.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blockStartText"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    blockStartTextComponents = [text_2, key_resp_2]
    for thisComponent in blockStartTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockStartTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blockStartText"-------
    while continueRoutine:
        # get current time
        t = blockStartTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockStartTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockStartTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockStartText"-------
    for thisComponent in blockStartTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('text_2.started', text_2.tStartRefresh)
    blocks.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    blocks.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        blocks.addData('key_resp_2.rt', key_resp_2.rt)
    blocks.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    blocks.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "blockStartText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_radio"-------
    continueRoutine = True
    # update component parameters for each repeat
    import pandas as pd;
    import numpy as np;
    import math;
    import os;
    
    kb = keyboard.Keyboard()
    rootdir = os.getcwd()
    
    #set constants for the experiment
    SHIELD_DECAY_RATE = 0.99; #decay rate after hitting shield
    
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 45; #because it needs to be predefined
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    shieldRedness = 0;
    minShieldDegrees = 25;
    maxShieldDegrees = 65;
    totalReward = 0;
    
    #load stimulusStream into NumPy array
    stimStreamPath = os.path.join(rootdir,'stimgen',blockFileName)
    storedStream_np = np.loadtxt(stimStreamPath,delimiter=",")
    #storedStream_np = np.loadtxt('/Users/lhunt/home/python/PsychoPy/experiments/rotation_task/stimgen/rotation_stream.csv',delimiter=",");
    
    #calculate the total number of frames in the experiment
    nFrames = np.shape(storedStream_np)[0] - 1;
    currentFrame = 0;
    laserRotation = storedStream_np[0,1];
    shieldRotation = 0; #begin at top
    
    #update variables to draw polygon
    laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
    laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
    
    hit_i = 0
    first_hit = 0
    triggerValue = 11
    sendTrigger = True
    #start by sending a trigger when subject presses a button
    sendResponseTriggers = True
    laser.setPos((0, 0))
    laser.setSize((1, 1))
    laser_long.setPos((0, 0))
    laser_long.setSize((1, 1))
    # keep track of which components have finished
    trial_radioComponents = [earth_background, harmless_area, shield, shield_centre, shield_background_short, laser, laser_long, radioactive, trialTrigger]
    for thisComponent in trial_radioComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_radioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_radio"-------
    while continueRoutine:
        # get current time
        t = trial_radioClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_radioClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #determine whether laser is crossing the shield
        if hit_i:
            laser_long.setAutoDraw(False)
            hit_i = 0
        else:
            if first_hit:
                laser_long.setAutoDraw(True)
        
        #do not send a trigger on every frame, only if laser position changes or subject presses a button
        sendTrigger = False
        keyReleaseThisFrame = False
        
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=['1','2'],clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=['1','2'],clear=True,waitRelease=False)
            triggerValue = 7
            sendTrigger = True
            keyReleaseThisFrame = True
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=['1','2'],clear=False,waitRelease=False)
        
        UDkeys_pressed = kb.getKeys(keyList=['3','4'],clear=True,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]=='1':
                shieldRotation += ROTATION_SPEED;
                newTriggerValue = 3
            if LRkeys_pressed[-1]=='2':
                shieldRotation -= ROTATION_SPEED;
                newTriggerValue = 4
            if sendResponseTriggers:
                triggerValue = newTriggerValue
                sendTrigger = True
                #stop triggering responses until key has been released again
                sendResponseTriggers = False
             
        if len(UDkeys_pressed)>0:
            if UDkeys_pressed[-1]=='3':
                shieldDegrees += SHIELD_GROWTH_SPEED;
                triggerValue = 5
            if UDkeys_pressed[-1]=='4':
                shieldDegrees -= SHIELD_GROWTH_SPEED;
                triggerValue = 6
            sendTrigger = True
        
        #set lower boundary on shieldWidth
        if shieldDegrees < minShieldDegrees:
            shieldDegrees = minShieldDegrees;
            
        #set upper boundary on shieldWidth
        if shieldDegrees > maxShieldDegrees:
            shieldDegrees = maxShieldDegrees;
            
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldX = np.concatenate(([0],shieldX));
        shieldY = np.concatenate(([0],shieldY));
        shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
        
        if currentFrame<nFrames:
            laserRotation = storedStream_np[currentFrame,1];
        
        #calculate whether shield is currently hit by laser
        currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
        
        #determine whether laser position has changed
        if currentFrame > 1:
            if storedStream_np[currentFrame,1] != storedStream_np[currentFrame-1,1]:
                #we only send a stimulus trigger if we don't already have a response to send
                if not sendTrigger:
                    #we'll send different stim change triggers depending on hit/no-hit
                    if currentHit:
                        triggerValue = 1
                    else:
                        triggerValue = 2
                    sendTrigger = True
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            update = (minShieldDegrees/50)/shieldDegrees;
            shieldRedness = min(shieldRedness + update,2);
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            laser_long.setAutoDraw(False)
            hit_i = 1
            first_hit = 1
            #laserColour = [1,-1,-1];
        else:
            shieldRedness = shieldRedness*SHIELD_DECAY_RATE;
            shieldColour = [1, 1-shieldRedness, 1-shieldRedness];
            #laser_long.setAutoDraw(True)
            #laserColour = [1,1,1];
        
        totalReward = totalReward + shieldRedness/100;
        textReward = str(round(totalReward, 1))
        
        if keyReleaseThisFrame:
            sendResponseTriggers = True
            
        if currentFrame<nFrames:
            saveData.append([blockID,currentFrame,laserRotation,shieldRotation,shieldDegrees,currentHit,totalReward,sendTrigger,triggerValue])
            currentFrame = currentFrame + 1;
        
        
        # *earth_background* updates
        if earth_background.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            earth_background.frameNStart = frameN  # exact frame index
            earth_background.tStart = t  # local t and not account for scr refresh
            earth_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earth_background, 'tStartRefresh')  # time at next scr refresh
            earth_background.setAutoDraw(True)
        if earth_background.status == STARTED:
            if frameN >= (earth_background.frameNStart + nFrames):
                # keep track of stop time/frame for later
                earth_background.tStop = t  # not accounting for scr refresh
                earth_background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(earth_background, 'tStopRefresh')  # time at next scr refresh
                earth_background.setAutoDraw(False)
        
        # *harmless_area* updates
        if harmless_area.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            harmless_area.frameNStart = frameN  # exact frame index
            harmless_area.tStart = t  # local t and not account for scr refresh
            harmless_area.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(harmless_area, 'tStartRefresh')  # time at next scr refresh
            harmless_area.setAutoDraw(True)
        if harmless_area.status == STARTED:
            if frameN >= (harmless_area.frameNStart + nFrames):
                # keep track of stop time/frame for later
                harmless_area.tStop = t  # not accounting for scr refresh
                harmless_area.frameNStop = frameN  # exact frame index
                win.timeOnFlip(harmless_area, 'tStopRefresh')  # time at next scr refresh
                harmless_area.setAutoDraw(False)
        
        # *shield* updates
        if shield.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield.frameNStart = frameN  # exact frame index
            shield.tStart = t  # local t and not account for scr refresh
            shield.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield, 'tStartRefresh')  # time at next scr refresh
            shield.setAutoDraw(True)
        if shield.status == STARTED:
            if frameN >= (shield.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield.tStop = t  # not accounting for scr refresh
                shield.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield, 'tStopRefresh')  # time at next scr refresh
                shield.setAutoDraw(False)
        if shield.status == STARTED:  # only update if drawing
            shield.setFillColor(shieldColour, log=False)
            shield.setOri(shieldRotation, log=False)
            shield.setVertices(shieldCoords, log=False)
            shield.setLineColor([0, 0, 0], log=False)
        
        # *shield_centre* updates
        if shield_centre.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_centre.frameNStart = frameN  # exact frame index
            shield_centre.tStart = t  # local t and not account for scr refresh
            shield_centre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre, 'tStartRefresh')  # time at next scr refresh
            shield_centre.setAutoDraw(True)
        if shield_centre.status == STARTED:
            if frameN >= (shield_centre.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_centre.tStop = t  # not accounting for scr refresh
                shield_centre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_centre, 'tStopRefresh')  # time at next scr refresh
                shield_centre.setAutoDraw(False)
        if shield_centre.status == STARTED:  # only update if drawing
            shield_centre.setPos((0, 0), log=False)
            shield_centre.setOri(shieldRotation, log=False)
        
        # *shield_background_short* updates
        if shield_background_short.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_background_short.frameNStart = frameN  # exact frame index
            shield_background_short.tStart = t  # local t and not account for scr refresh
            shield_background_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_background_short, 'tStartRefresh')  # time at next scr refresh
            shield_background_short.setAutoDraw(True)
        if shield_background_short.status == STARTED:
            if frameN >= (shield_background_short.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_background_short.tStop = t  # not accounting for scr refresh
                shield_background_short.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_background_short, 'tStopRefresh')  # time at next scr refresh
                shield_background_short.setAutoDraw(False)
        if shield_background_short.status == STARTED:  # only update if drawing
            shield_background_short.setFillColor([0, 0, 0], log=False)
            shield_background_short.setOri(shieldRotation, log=False)
            shield_background_short.setVertices(shieldCoords, log=False)
            shield_background_short.setLineColor([0, 0, 0], log=False)
        
        # *laser* updates
        if laser.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser.frameNStart = frameN  # exact frame index
            laser.tStart = t  # local t and not account for scr refresh
            laser.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser, 'tStartRefresh')  # time at next scr refresh
            laser.setAutoDraw(True)
        if laser.status == STARTED:
            if frameN >= (laser.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser.tStop = t  # not accounting for scr refresh
                laser.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser, 'tStopRefresh')  # time at next scr refresh
                laser.setAutoDraw(False)
        if laser.status == STARTED:  # only update if drawing
            laser.setOri(laserRotation, log=False)
            laser.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.1]], log=False)
        
        # *laser_long* updates
        if laser_long.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser_long.frameNStart = frameN  # exact frame index
            laser_long.tStart = t  # local t and not account for scr refresh
            laser_long.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser_long, 'tStartRefresh')  # time at next scr refresh
            laser_long.setAutoDraw(True)
        if laser_long.status == STARTED:
            if frameN >= (laser_long.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser_long.tStop = t  # not accounting for scr refresh
                laser_long.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser_long, 'tStopRefresh')  # time at next scr refresh
                laser_long.setAutoDraw(False)
        if laser_long.status == STARTED:  # only update if drawing
            laser_long.setOri(laserRotation, log=False)
            laser_long.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
        
        # *radioactive* updates
        if radioactive.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            radioactive.frameNStart = frameN  # exact frame index
            radioactive.tStart = t  # local t and not account for scr refresh
            radioactive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive, 'tStartRefresh')  # time at next scr refresh
            radioactive.setAutoDraw(True)
        if radioactive.status == STARTED:
            if frameN >= (radioactive.frameNStart + nFrames):
                # keep track of stop time/frame for later
                radioactive.tStop = t  # not accounting for scr refresh
                radioactive.frameNStop = frameN  # exact frame index
                win.timeOnFlip(radioactive, 'tStopRefresh')  # time at next scr refresh
                radioactive.setAutoDraw(False)
        # *trialTrigger* updates
        if trialTrigger.status == NOT_STARTED and sendTrigger==True:
            # keep track of start time/frame for later
            trialTrigger.frameNStart = frameN  # exact frame index
            trialTrigger.tStart = t  # local t and not account for scr refresh
            trialTrigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialTrigger, 'tStartRefresh')  # time at next scr refresh
            trialTrigger.status = STARTED
            win.callOnFlip(trialTrigger.setData, int(triggerValue))
        if trialTrigger.status == STARTED:
            if frameN >= (trialTrigger.frameNStart + 0.5):
                # keep track of stop time/frame for later
                trialTrigger.tStop = t  # not accounting for scr refresh
                trialTrigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialTrigger, 'tStopRefresh')  # time at next scr refresh
                trialTrigger.status = FINISHED
                win.callOnFlip(trialTrigger.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_radioComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_radio"-------
    for thisComponent in trial_radioComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    
    blocks.addData('earth_background.started', earth_background.tStartRefresh)
    blocks.addData('earth_background.stopped', earth_background.tStopRefresh)
    blocks.addData('harmless_area.started', harmless_area.tStartRefresh)
    blocks.addData('harmless_area.stopped', harmless_area.tStopRefresh)
    blocks.addData('shield.started', shield.tStartRefresh)
    blocks.addData('shield.stopped', shield.tStopRefresh)
    blocks.addData('shield_centre.started', shield_centre.tStartRefresh)
    blocks.addData('shield_centre.stopped', shield_centre.tStopRefresh)
    blocks.addData('shield_background_short.started', shield_background_short.tStartRefresh)
    blocks.addData('shield_background_short.stopped', shield_background_short.tStopRefresh)
    blocks.addData('laser.started', laser.tStartRefresh)
    blocks.addData('laser.stopped', laser.tStopRefresh)
    blocks.addData('laser_long.started', laser_long.tStartRefresh)
    blocks.addData('laser_long.stopped', laser_long.tStopRefresh)
    blocks.addData('radioactive.started', radioactive.tStartRefresh)
    blocks.addData('radioactive.stopped', radioactive.tStopRefresh)
    if trialTrigger.status == STARTED:
        win.callOnFlip(trialTrigger.setData, int(0))
    blocks.addData('trialTrigger.started', trialTrigger.tStartRefresh)
    blocks.addData('trialTrigger.stopped', trialTrigger.tStopRefresh)
    # the Routine "trial_radio" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blockEndText"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    blockEndTextComponents = [textPause, textContinue, key_resp_3]
    for thisComponent in blockEndTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blockEndText"-------
    while continueRoutine:
        # get current time
        t = blockEndTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockEndTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPause* updates
        if textPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textPause.frameNStart = frameN  # exact frame index
            textPause.tStart = t  # local t and not account for scr refresh
            textPause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textPause, 'tStartRefresh')  # time at next scr refresh
            textPause.setAutoDraw(True)
        if textPause.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textPause.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textPause.tStop = t  # not accounting for scr refresh
                textPause.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textPause, 'tStopRefresh')  # time at next scr refresh
                textPause.setAutoDraw(False)
        
        # *textContinue* updates
        if textContinue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            textContinue.frameNStart = frameN  # exact frame index
            textContinue.tStart = t  # local t and not account for scr refresh
            textContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinue, 'tStartRefresh')  # time at next scr refresh
            textContinue.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockEndTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockEndText"-------
    for thisComponent in blockEndTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('textPause.started', textPause.tStartRefresh)
    blocks.addData('textPause.stopped', textPause.tStopRefresh)
    blocks.addData('textContinue.started', textContinue.tStartRefresh)
    blocks.addData('textContinue.stopped', textContinue.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    blocks.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        blocks.addData('key_resp_3.rt', key_resp_3.rt)
    blocks.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    blocks.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "blockEndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# ------Prepare to start Routine "expEndText"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
expEndTextComponents = [textEndExp]
for thisComponent in expEndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
expEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "expEndText"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = expEndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=expEndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndExp* updates
    if textEndExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndExp.frameNStart = frameN  # exact frame index
        textEndExp.tStart = t  # local t and not account for scr refresh
        textEndExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndExp, 'tStartRefresh')  # time at next scr refresh
        textEndExp.setAutoDraw(True)
    if textEndExp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndExp.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndExp.tStop = t  # not accounting for scr refresh
            textEndExp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndExp, 'tStopRefresh')  # time at next scr refresh
            textEndExp.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expEndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "expEndText"-------
for thisComponent in expEndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEndExp.started', textEndExp.tStartRefresh)
thisExp.addData('textEndExp.stopped', textEndExp.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
