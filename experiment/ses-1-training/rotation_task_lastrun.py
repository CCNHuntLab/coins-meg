#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Thu May 18 13:35:06 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
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
psychopyVersion = '2022.2.5'
expName = 'tmptmp'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/amyli/Desktop/LH-lab/rotation_task-vol-vajump-bi/rotation_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "instructions_1" ---
# Run 'Begin Experiment' code from code_begin_2
#import necessary packages
import numpy as np;
import os;

#keyboard constants
session = 1;
image = 2;
order = 2;

kb = keyboard.Keyboard()

if session == 1:
    keys_move = ['s', 'a'];
    keys_size = ['l', 'k'];
    key_right = 's';
    key_left = 'a';
    key_up = 'l';
    key_down = 'k';
if session == 2:
    keys_move = ['l', 'k'];
    keys_size = ['s', 'a'];
    key_right = 'l';
    key_left = 'k';
    key_up = 's';
    key_down = 'a';

#set constants for the experiment
ROTATION_SPEED = 1;
CIRCLE_RADIUS = 3;

SHIELD_GROWTH_SPEED = 20; #in degrees

minShieldDegrees = 20;
maxShieldDegrees = 60;

#initialise variables that will be updated as experiment progresses

#instructed training variables
training_loop_count = -1
target_orientation = 0

#shield variables
shieldDegrees = 40; #because it needs to be predefined
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;

#calculate the screen X and Y locations that correspond to the shield centre
shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldX = np.concatenate(([0],shieldX));
shieldY = np.concatenate(([0],shieldY));
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

shieldRotation = 360; #begin at top

#initialise list containing data to be saved
saveData = [["blockID","currentFrame","laserRotation","shieldRotation","shieldDegrees","currentHit","totalReward","sendTrigger","triggerValue","trueMean","trueVariance","volatility"]]
saveFilename = "savedData_" + str(expInfo['participant']) + str(expInfo['session']) + ".csv" #load stimulusStream into NumPy array

#reward variables
red_bar_length = 0;

wins = 0;

if wins == 0:
    bar_length = 0.5;

    totalReward_tot = 0;
    
    reward_change_colour = [1, -1, -1];
else:
    bar_length = 0.25;
    
    totalReward_tot = 0;
    reward_change_colour = [-1, -1, 1];

win.mouseVisible = False

totalReward_text = '';

progress_bar_length = 0;

lossFactor = 0.003;
title = visual.TextBox2(
     win, text='Save-the-world task', font='Open Sans',
     pos=(0, 0.35),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='title',
     autoLog=True,
)
text_instructions_1 = visual.TextStim(win=win, name='text_instructions_1',
    text='Welcome to a new session of the save-the-world task!\n\u200b\nRemember, you can save the world (and make money!) by navigating your shield to where you expect radiation to be emitted.\n\nPress any key to start the session.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_i1 = keyboard.Keyboard()

# --- Initialize components for Routine "blockStartText" ---
radioactive_block_source = visual.ImageStim(
    win=win,
    name='radioactive_block_source', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text="New source ahead:\n\n\n\n\n\n\n\n\n\nPress any key if you're ready to start.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_blockStart = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
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
    win=win, name='shield', vertices=[[-0.5,-0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]],units='cm', 
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
shield_bg_short = visual.ShapeStim(
    win=win, name='shield_bg_short', vertices=[[-0.5,-0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
laser = visual.ShapeStim(
    win=win, name='laser', vertices=[[-0.5,-0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-6.0, interpolate=True)
laser_long = visual.ShapeStim(
    win=win, name='laser_long', vertices=[[-0.5,-0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-7.0, interpolate=True)
radioactive = visual.ImageStim(
    win=win,
    name='radioactive', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
reward_bar_red = visual.Rect(
    win=win, name='reward_bar_red',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0], anchor='bottom-center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
reward_bar = visual.Rect(
    win=win, name='reward_bar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0.6, -0.3), anchor='bottom-center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-10.0, interpolate=True)
progress_bar_edge = visual.Rect(
    win=win, name='progress_bar_edge',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(-0.4, -0.45), anchor='center-left',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='green', fillColor=[0, 0, 0],
    opacity=None, depth=-11.0, interpolate=True)
progress_bar = visual.Rect(
    win=win, name='progress_bar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(-0.4, -0.45), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=-12.0, interpolate=True)
reward_text_top = visual.TextStim(win=win, name='reward_text_top',
    text='',
    font='Open Sans',
    pos=(0.6, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
reward_text_bottom = visual.TextStim(win=win, name='reward_text_bottom',
    text='',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
start_text = visual.TextStim(win=win, name='start_text',
    text='Start',
    font='Open Sans',
    pos=(-0.47, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
end_text = visual.TextStim(win=win, name='end_text',
    text='End',
    font='Open Sans',
    pos=(0.47, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# --- Initialize components for Routine "blockEndText" ---
textPause = visual.TextStim(win=win, name='textPause',
    text='Well done.\n\nTake a short break.\n\nIn this block, you obtained:',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
reward_text = visual.TextStim(win=win, name='reward_text',
    text='',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textContinue = visual.TextStim(win=win, name='textContinue',
    text='Press any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_blockEnd = keyboard.Keyboard()

# --- Initialize components for Routine "expEndText" ---
textEndExp = visual.TextStim(win=win, name='textEndExp',
    text='Well done. You completed all blocks in this session.\n\nIn this session, you would have earned:\n\n\n\n\n\nThank you',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
finalReward_text = visual.TextStim(win=win, name='finalReward_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
title.reset()
key_resp_i1.keys = []
key_resp_i1.rt = []
_key_resp_i1_allKeys = []
# keep track of which components have finished
instructions_1Components = [title, text_instructions_1, key_resp_i1]
for thisComponent in instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'title.started')
        title.setAutoDraw(True)
    
    # *text_instructions_1* updates
    if text_instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_1.frameNStart = frameN  # exact frame index
        text_instructions_1.tStart = t  # local t and not account for scr refresh
        text_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instructions_1.started')
        text_instructions_1.setAutoDraw(True)
    
    # *key_resp_i1* updates
    waitOnFlip = False
    if key_resp_i1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_i1.frameNStart = frameN  # exact frame index
        key_resp_i1.tStart = t  # local t and not account for scr refresh
        key_resp_i1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_i1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_i1.started')
        key_resp_i1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_i1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_i1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_i1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_i1.getKeys(keyList=None, waitRelease=False)
        _key_resp_i1_allKeys.extend(theseKeys)
        if len(_key_resp_i1_allKeys):
            key_resp_i1.keys = _key_resp_i1_allKeys[-1].name  # just the last key pressed
            key_resp_i1.rt = _key_resp_i1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_1" ---
for thisComponent in instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_i1.keys in ['', [], None]:  # No response was made
    key_resp_i1.keys = None
thisExp.addData('key_resp_i1.keys',key_resp_i1.keys)
if key_resp_i1.keys != None:  # we had a response
    thisExp.addData('key_resp_i1.rt', key_resp_i1.rt)
thisExp.nextEntry()
# the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimgen/blocks_training2 - 2.csv'),
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
    
    # --- Prepare to start Routine "blockStartText" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_blockStart
    #determine radioactive source image
    rootdir = os.getcwd()
    sourceImageFile = os.path.join(rootdir,'images',sourceImage)
    radioactive_block_source.setImage(sourceImageFile)
    key_resp_blockStart.keys = []
    key_resp_blockStart.rt = []
    _key_resp_blockStart_allKeys = []
    # keep track of which components have finished
    blockStartTextComponents = [radioactive_block_source, text_2, key_resp_blockStart]
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
    frameN = -1
    
    # --- Run Routine "blockStartText" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *radioactive_block_source* updates
        if radioactive_block_source.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            radioactive_block_source.frameNStart = frameN  # exact frame index
            radioactive_block_source.tStart = t  # local t and not account for scr refresh
            radioactive_block_source.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive_block_source, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'radioactive_block_source.started')
            radioactive_block_source.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # *key_resp_blockStart* updates
        waitOnFlip = False
        if key_resp_blockStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockStart.frameNStart = frameN  # exact frame index
            key_resp_blockStart.tStart = t  # local t and not account for scr refresh
            key_resp_blockStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_blockStart.started')
            key_resp_blockStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_blockStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_blockStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_blockStart.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_blockStart.getKeys(keyList=None, waitRelease=False)
            _key_resp_blockStart_allKeys.extend(theseKeys)
            if len(_key_resp_blockStart_allKeys):
                key_resp_blockStart.keys = _key_resp_blockStart_allKeys[-1].name  # just the last key pressed
                key_resp_blockStart.rt = _key_resp_blockStart_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockStartTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockStartText" ---
    for thisComponent in blockStartTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_blockStart.keys in ['', [], None]:  # No response was made
        key_resp_blockStart.keys = None
    blocks.addData('key_resp_blockStart.keys',key_resp_blockStart.keys)
    if key_resp_blockStart.keys != None:  # we had a response
        blocks.addData('key_resp_blockStart.rt', key_resp_blockStart.rt)
    # the Routine "blockStartText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_changeLoss
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 20; #because it needs to be predefined
    
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    
    #load stimulusStream into NumPy array
    rootdir = os.getcwd()
    stimStreamPath = os.path.join(rootdir,'stimgen',blockFileName)
    storedStream_np = np.loadtxt(stimStreamPath,delimiter=",")
    
    shieldRotation = 360; #begin at top
    
    #calculate the total number of frames in the experiment
    nFrames = np.shape(storedStream_np)[0] - 1;
    currentFrame = 0;
    laserRotation = storedStream_np[0,1];
    trueMean = storedStream_np[0,0];
    trueVariance = storedStream_np[0,2];
    
    #update variables to draw polygon
    laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
    laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
    
    hit_i = 0
    first_hit = 0
    
    triggerValue = 11
    sendTrigger = True
    #start by sending a trigger when subject presses a button
    sendResponseTriggers = True
    
    square_colour = 'black';
    
    if wins == 0:
        
        bar_length = 0.5;
        top_amount = 1;
        bottom_amount = 0.8;
    
        totalReward = 1;
        
        reward_change_colour = [1, -1, -1];
    else:
        
        top_amount = 4;
        bottom_amount = 3;
        
        totalReward = 3.5;
        reward_change_colour = [-1, -1, 1];
    
    top_amount_text = "£%.2f" %(top_amount);
    bottom_amount_text = "£%.2f" %(bottom_amount);
    
    unique, counts = np.unique(storedStream_np, return_counts=True);
    laser_on = min(counts);
    laser_frame_ct = 0;
    
    laser.setAutoDraw(False);
    laser_long.setAutoDraw(False);
    
    progress_bar_length = 0;
    laser.setPos((0, 0))
    laser.setSize((1, 1))
    laser_long.setPos((0, 0))
    laser_long.setSize((1, 1))
    radioactive.setImage(sourceImageFile)
    # keep track of which components have finished
    trialComponents = [earth_background, harmless_area, shield, shield_centre, shield_bg_short, laser, laser_long, radioactive, reward_bar_red, reward_bar, progress_bar_edge, progress_bar, reward_text_top, reward_text_bottom, start_text, end_text]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_changeLoss
        #determine whether laser is crossing the shield
        if hit_i:
            hit_i = 0
        else:
            if first_hit:
                laser_long.setAutoDraw(True)
        
        if wins == 0:
            if bar_length <= 0:
                bar_length = 0.5;
                top_amount = top_amount - 0.2;
                bottom_amount = bottom_amount - 0.2;
                top_amount_text = "£%.2f" %(top_amount);
                bottom_amount_text = "£%.2f" %(bottom_amount);
            
        if wins == 1:
            if bar_length >= 0.5:
                bar_length = 0.001;
                top_amount = top_amount + 1;
                bottom_amount = bottom_amount + 1;
                top_amount_text = "£%.2f" %(top_amount);
                bottom_amount_text = "£%.2f" %(bottom_amount);
            if bar_length <= 0:
                bar_length = 0.5;
                top_amount = top_amount - 1;
                bottom_amount = bottom_amount - 1;
                top_amount_text = "£%.2f" %(top_amount);
                bottom_amount_text = "£%.2f" %(bottom_amount);
                
        if totalReward <= 0:
            if wins == 0:
                bar_length = 0.25;
                top_amount = 0.2;
                bottom_amount = 0.0;
                top_amount_text = "£%.2f" %(top_amount);
                bottom_amount_text = "£%.2f" %(bottom_amount);
                
                totalReward = 0.1;
            if wins == 1:
                bar_length = 0.00001;
                red_bar_length = 0;
                top_amount = 1;
                bottom_amount = 0;
                top_amount_text = "£%.2f" %(top_amount);
                bottom_amount_text = "£%.2f" %(bottom_amount);
                
                totalReward = 0;
                
        if square_colour == 'black':
            colour_id = 1
        if square_colour == 'white':
            colour_id = 2
        
        #do not send a trigger on every frame, only if laser position changes or subject presses a button
        sendTrigger = False
        keyReleaseThisFrame = False
        
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=keys_move,clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=True,waitRelease=False)
            triggerValue = 7
            sendTrigger = True
            keyReleaseThisFrame = True
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=False,waitRelease=False)
        
        UDkeys_pressed = kb.getKeys(keyList=keys_size,clear=True,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]==key_right:
                shieldRotation += ROTATION_SPEED;
                newTriggerValue = 3
            if LRkeys_pressed[-1]==key_left:
                shieldRotation -= ROTATION_SPEED;
                newTriggerValue = 4
            if sendResponseTriggers:
                triggerValue = newTriggerValue
                sendTrigger = True
                #stop triggering responses until key has been released again
                sendResponseTriggers = False
        
        if len(UDkeys_pressed)>0:
            if UDkeys_pressed[-1]==key_up:
                shieldDegrees += SHIELD_GROWTH_SPEED;
                triggerValue = 5
            if UDkeys_pressed[-1]==key_down:
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
            trueMean = storedStream_np[currentFrame,0];
            trueVariance = storedStream_np[currentFrame,2];
            if currentFrame > 0:
                if storedStream_np[currentFrame, 1] != storedStream_np[currentFrame - 1, 1]:
                    laser_frame_ct = 0;
                else:
                    laser_frame_ct = laser_frame_ct + 1;
        
                if laser_frame_ct <= laser_on:
                    laser.setAutoDraw(True);
                    laser_long.setAutoDraw(True);
                else:
                    laser.setAutoDraw(False);
                    laser_long.setAutoDraw(False);
        
        #calculate whether shield is currently hit by laser
        currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
        
        #determine whether laser position has changed
        if currentFrame == 0:
            if not sendTrigger:
                #we'll send different stim change triggers depending on hit/no-hit
                if currentHit:
                    triggerValue = 1
                else:
                    triggerValue = 2
        
                if colour_id == 1:
                    square_colour = 'white'
                elif colour_id == 2:
                    square_colour = 'black'
                
                sendTrigger = True
        
            if currentHit:
                if wins == 0:
                    if shieldDegrees == 20:
                        bar_length = bar_length;
                        totalReward = totalReward;
                        red_bar_length = 0;
                    if shieldDegrees == 40:
                        bar_length = bar_length - 2.5*(lossFactor/3);
                        totalReward = totalReward - lossFactor/3;
                        red_bar_length = 2.5*lossFactor/3;
                    if shieldDegrees == 60:
                        bar_length = bar_length - 2.5*(lossFactor/2);
                        totalReward = totalReward - lossFactor/2;
                        red_bar_length = 2.5*lossFactor/2;
                if wins == 1:
                    if shieldDegrees == 20:
                        bar_length = bar_length + 0.00003;
                        totalReward = totalReward + 2*0.00003;
                        red_bar_length = 0.00003*100;
                        reward_change_colour = [-1, 1, -1];
                    if shieldDegrees == 40:
                        bar_length = bar_length;
                        totalReward = totalReward;
                        red_bar_length = 0;
                        reward_change_colour = [-1, -1, 1];
                    if shieldDegrees == 60:
                        if totalReward > 0:
                            bar_length = bar_length - 0.00003;
                            totalReward = totalReward - 2*0.00003;
                            red_bar_length = 0.00003*100;
                        else:
                            bar_length = 0;
                            totalReward = 0;
                            red_bar_length = 0;
                        reward_change_colour = [1, -1, -1];
                        
            else:
                if totalReward > 0:
                    bar_length = bar_length - 2.5*lossFactor;
                    totalReward = totalReward - lossFactor;
                    red_bar_length = 2.5*lossFactor;
                else:
                    bar_length = 0.00001;
                    totalReward = 0;
                    red_bar_length = 0;
                if wins == 1:
                    reward_change_colour = [1, -1, -1];
        if currentFrame > 1:
            if storedStream_np[currentFrame,1] != storedStream_np[currentFrame-1,1]:
                #we only send a stimulus trigger if we don't already have a response to send
                if not sendTrigger:
                    #we'll send different stim change triggers depending on hit/no-hit
                    if currentHit:
                        triggerValue = 1
                    else:
                        triggerValue = 2
        
                    if colour_id == 1:
                        square_colour = 'white'
                    elif colour_id == 2:
                        square_colour = 'black'
                    
                    sendTrigger = True
                    
                if currentHit:
                    if wins == 0:
                        if shieldDegrees == 20:
                            bar_length = bar_length;
                            totalReward = totalReward;
                            red_bar_length = 0;
                        if shieldDegrees == 40:
                            bar_length = bar_length - 2.5*(lossFactor/3);
                            totalReward = totalReward - lossFactor/3;
                            red_bar_length = 2.5*lossFactor/3;
                        if shieldDegrees == 60:
                            bar_length = bar_length - 2.5*(lossFactor/2);
                            totalReward = totalReward - lossFactor/2;
                            red_bar_length = 2.5*lossFactor/2;
                    if wins == 1:
                        if shieldDegrees == 20:
                            bar_length = bar_length + 0.00003;
                            totalReward = totalReward + 2*0.00003;
                            red_bar_length = 0.00003*100;
                            reward_change_colour = [-1, 1, -1];
                        if shieldDegrees == 40:
                            bar_length = bar_length;
                            totalReward = totalReward;
                            red_bar_length = 0;
                            reward_change_colour = [-1, -1, 1];
                        if shieldDegrees == 60:
                            if totalReward > 0:
                                bar_length = bar_length - 0.00003;
                                totalReward = totalReward - 2*0.00003;
                                red_bar_length = 0.00003*100;
                            else:
                                bar_length = 0;
                                totalReward = 0;
                                red_bar_length = 0;
                            reward_change_colour = [1, -1, -1];
                            
                else:
                    if totalReward > 0:
                        bar_length = bar_length - 2.5*lossFactor;
                        totalReward = totalReward - lossFactor;
                        red_bar_length = 2.5*lossFactor;
                    else:
                        bar_length = 0.00001;
                        totalReward = 0;
                        red_bar_length = 0;
                    if wins == 1:
                        reward_change_colour = [1, -1, -1];
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            if shieldDegrees == 20:
                laser_long_opacity = 0;
            if shieldDegrees == 40:
                laser_long_opacity = 0.1;
            if shieldDegrees == 60:
                laser_long_opacity = 0.3;
        
            shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
            hit_i = 1
            first_hit = 1
        else:
            laser_long_opacity = 1
            
            shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
        
        if keyReleaseThisFrame:
            sendResponseTriggers = True
            
        if currentFrame<nFrames:
            saveData.append([blockID,currentFrame,laserRotation,shieldRotation,shieldDegrees,currentHit,totalReward,sendTrigger,triggerValue,trueMean,trueVariance,volatility])
            currentFrame = currentFrame + 1;
        else:
            triggerValue = 99
            sendTrigger = True
            
        progress_bar_length = progress_bar_length + 0.8/nFrames;
        
        # *earth_background* updates
        if earth_background.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            earth_background.frameNStart = frameN  # exact frame index
            earth_background.tStart = t  # local t and not account for scr refresh
            earth_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(earth_background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'earth_background.started')
            earth_background.setAutoDraw(True)
        if earth_background.status == STARTED:
            if frameN >= (earth_background.frameNStart + nFrames):
                # keep track of stop time/frame for later
                earth_background.tStop = t  # not accounting for scr refresh
                earth_background.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'earth_background.stopped')
                earth_background.setAutoDraw(False)
        
        # *harmless_area* updates
        if harmless_area.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            harmless_area.frameNStart = frameN  # exact frame index
            harmless_area.tStart = t  # local t and not account for scr refresh
            harmless_area.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(harmless_area, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'harmless_area.started')
            harmless_area.setAutoDraw(True)
        if harmless_area.status == STARTED:
            if frameN >= (harmless_area.frameNStart + nFrames):
                # keep track of stop time/frame for later
                harmless_area.tStop = t  # not accounting for scr refresh
                harmless_area.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'harmless_area.stopped')
                harmless_area.setAutoDraw(False)
        
        # *shield* updates
        if shield.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield.frameNStart = frameN  # exact frame index
            shield.tStart = t  # local t and not account for scr refresh
            shield.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'shield.started')
            shield.setAutoDraw(True)
        if shield.status == STARTED:
            if frameN >= (shield.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield.tStop = t  # not accounting for scr refresh
                shield.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shield.stopped')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'shield_centre.started')
            shield_centre.setAutoDraw(True)
        if shield_centre.status == STARTED:
            if frameN >= (shield_centre.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_centre.tStop = t  # not accounting for scr refresh
                shield_centre.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shield_centre.stopped')
                shield_centre.setAutoDraw(False)
        if shield_centre.status == STARTED:  # only update if drawing
            shield_centre.setPos((0, 0), log=False)
            shield_centre.setOri(shieldRotation, log=False)
        
        # *shield_bg_short* updates
        if shield_bg_short.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_bg_short.frameNStart = frameN  # exact frame index
            shield_bg_short.tStart = t  # local t and not account for scr refresh
            shield_bg_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_bg_short, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'shield_bg_short.started')
            shield_bg_short.setAutoDraw(True)
        if shield_bg_short.status == STARTED:
            if frameN >= (shield_bg_short.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_bg_short.tStop = t  # not accounting for scr refresh
                shield_bg_short.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shield_bg_short.stopped')
                shield_bg_short.setAutoDraw(False)
        if shield_bg_short.status == STARTED:  # only update if drawing
            shield_bg_short.setFillColor([0, 0, 0], log=False)
            shield_bg_short.setOri(shieldRotation, log=False)
            shield_bg_short.setVertices(shieldCoords, log=False)
            shield_bg_short.setLineColor([0, 0, 0], log=False)
        
        # *laser* updates
        if laser.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            laser.frameNStart = frameN  # exact frame index
            laser.tStart = t  # local t and not account for scr refresh
            laser.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'laser.started')
            laser.setAutoDraw(True)
        if laser.status == STARTED:
            if frameN >= (laser.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser.tStop = t  # not accounting for scr refresh
                laser.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'laser.stopped')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'laser_long.started')
            laser_long.setAutoDraw(True)
        if laser_long.status == STARTED:
            if frameN >= (laser_long.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser_long.tStop = t  # not accounting for scr refresh
                laser_long.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'laser_long.stopped')
                laser_long.setAutoDraw(False)
        if laser_long.status == STARTED:  # only update if drawing
            laser_long.setOpacity(laser_long_opacity, log=False)
            laser_long.setOri(laserRotation, log=False)
            laser_long.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
        
        # *radioactive* updates
        if radioactive.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            radioactive.frameNStart = frameN  # exact frame index
            radioactive.tStart = t  # local t and not account for scr refresh
            radioactive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'radioactive.started')
            radioactive.setAutoDraw(True)
        if radioactive.status == STARTED:
            if frameN >= (radioactive.frameNStart + nFrames):
                # keep track of stop time/frame for later
                radioactive.tStop = t  # not accounting for scr refresh
                radioactive.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'radioactive.stopped')
                radioactive.setAutoDraw(False)
        
        # *reward_bar_red* updates
        if reward_bar_red.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            reward_bar_red.frameNStart = frameN  # exact frame index
            reward_bar_red.tStart = t  # local t and not account for scr refresh
            reward_bar_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_bar_red, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reward_bar_red.started')
            reward_bar_red.setAutoDraw(True)
        if reward_bar_red.status == STARTED:
            if frameN >= (reward_bar_red.frameNStart + nFrames):
                # keep track of stop time/frame for later
                reward_bar_red.tStop = t  # not accounting for scr refresh
                reward_bar_red.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reward_bar_red.stopped')
                reward_bar_red.setAutoDraw(False)
        if reward_bar_red.status == STARTED:  # only update if drawing
            reward_bar_red.setFillColor(reward_change_colour, log=False)
            reward_bar_red.setPos((0.6, -0.3+bar_length), log=False)
            reward_bar_red.setSize((0.05, red_bar_length), log=False)
            reward_bar_red.setLineColor(reward_change_colour, log=False)
        
        # *reward_bar* updates
        if reward_bar.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            reward_bar.frameNStart = frameN  # exact frame index
            reward_bar.tStart = t  # local t and not account for scr refresh
            reward_bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_bar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reward_bar.started')
            reward_bar.setAutoDraw(True)
        if reward_bar.status == STARTED:
            if frameN >= (reward_bar.frameNStart + nFrames):
                # keep track of stop time/frame for later
                reward_bar.tStop = t  # not accounting for scr refresh
                reward_bar.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reward_bar.stopped')
                reward_bar.setAutoDraw(False)
        if reward_bar.status == STARTED:  # only update if drawing
            reward_bar.setSize((0.05, bar_length), log=False)
        
        # *progress_bar_edge* updates
        if progress_bar_edge.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            progress_bar_edge.frameNStart = frameN  # exact frame index
            progress_bar_edge.tStart = t  # local t and not account for scr refresh
            progress_bar_edge.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_bar_edge, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'progress_bar_edge.started')
            progress_bar_edge.setAutoDraw(True)
        if progress_bar_edge.status == STARTED:
            if frameN >= (progress_bar_edge.frameNStart + nFrames):
                # keep track of stop time/frame for later
                progress_bar_edge.tStop = t  # not accounting for scr refresh
                progress_bar_edge.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'progress_bar_edge.stopped')
                progress_bar_edge.setAutoDraw(False)
        if progress_bar_edge.status == STARTED:  # only update if drawing
            progress_bar_edge.setSize((0.8, 0.05), log=False)
        
        # *progress_bar* updates
        if progress_bar.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            progress_bar.frameNStart = frameN  # exact frame index
            progress_bar.tStart = t  # local t and not account for scr refresh
            progress_bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_bar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'progress_bar.started')
            progress_bar.setAutoDraw(True)
        if progress_bar.status == STARTED:
            if frameN >= (progress_bar.frameNStart + nFrames):
                # keep track of stop time/frame for later
                progress_bar.tStop = t  # not accounting for scr refresh
                progress_bar.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'progress_bar.stopped')
                progress_bar.setAutoDraw(False)
        if progress_bar.status == STARTED:  # only update if drawing
            progress_bar.setSize((progress_bar_length, 0.05), log=False)
        
        # *reward_text_top* updates
        if reward_text_top.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            reward_text_top.frameNStart = frameN  # exact frame index
            reward_text_top.tStart = t  # local t and not account for scr refresh
            reward_text_top.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_text_top, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reward_text_top.started')
            reward_text_top.setAutoDraw(True)
        if reward_text_top.status == STARTED:
            if frameN >= (reward_text_top.frameNStart + nFrames):
                # keep track of stop time/frame for later
                reward_text_top.tStop = t  # not accounting for scr refresh
                reward_text_top.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reward_text_top.stopped')
                reward_text_top.setAutoDraw(False)
        if reward_text_top.status == STARTED:  # only update if drawing
            reward_text_top.setText(top_amount_text, log=False)
        
        # *reward_text_bottom* updates
        if reward_text_bottom.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            reward_text_bottom.frameNStart = frameN  # exact frame index
            reward_text_bottom.tStart = t  # local t and not account for scr refresh
            reward_text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_text_bottom, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reward_text_bottom.started')
            reward_text_bottom.setAutoDraw(True)
        if reward_text_bottom.status == STARTED:
            if frameN >= (reward_text_bottom.frameNStart + nFrames):
                # keep track of stop time/frame for later
                reward_text_bottom.tStop = t  # not accounting for scr refresh
                reward_text_bottom.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reward_text_bottom.stopped')
                reward_text_bottom.setAutoDraw(False)
        if reward_text_bottom.status == STARTED:  # only update if drawing
            reward_text_bottom.setText(bottom_amount_text, log=False)
        
        # *start_text* updates
        if start_text.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            start_text.frameNStart = frameN  # exact frame index
            start_text.tStart = t  # local t and not account for scr refresh
            start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_text.started')
            start_text.setAutoDraw(True)
        if start_text.status == STARTED:
            if frameN >= (start_text.frameNStart + nFrames):
                # keep track of stop time/frame for later
                start_text.tStop = t  # not accounting for scr refresh
                start_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'start_text.stopped')
                start_text.setAutoDraw(False)
        
        # *end_text* updates
        if end_text.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.started')
            end_text.setAutoDraw(True)
        if end_text.status == STARTED:
            if frameN >= (end_text.frameNStart + nFrames):
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_text.stopped')
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_changeLoss
    totalReward_tot = totalReward_tot + totalReward;
    totalReward_text = "£%.2f" %(totalReward);
    
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blockEndText" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_blockEnd
    totalReward_text = "£%.2f" %(totalReward);
    reward_text.setText(totalReward_text)
    key_resp_blockEnd.keys = []
    key_resp_blockEnd.rt = []
    _key_resp_blockEnd_allKeys = []
    # keep track of which components have finished
    blockEndTextComponents = [textPause, reward_text, textContinue, key_resp_blockEnd]
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
    frameN = -1
    
    # --- Run Routine "blockEndText" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textPause.started')
            textPause.setAutoDraw(True)
        if textPause.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textPause.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textPause.tStop = t  # not accounting for scr refresh
                textPause.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPause.stopped')
                textPause.setAutoDraw(False)
        
        # *reward_text* updates
        if reward_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reward_text.frameNStart = frameN  # exact frame index
            reward_text.tStart = t  # local t and not account for scr refresh
            reward_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reward_text.started')
            reward_text.setAutoDraw(True)
        if reward_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reward_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                reward_text.tStop = t  # not accounting for scr refresh
                reward_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reward_text.stopped')
                reward_text.setAutoDraw(False)
        
        # *textContinue* updates
        if textContinue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            textContinue.frameNStart = frameN  # exact frame index
            textContinue.tStart = t  # local t and not account for scr refresh
            textContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textContinue.started')
            textContinue.setAutoDraw(True)
        
        # *key_resp_blockEnd* updates
        waitOnFlip = False
        if key_resp_blockEnd.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockEnd.frameNStart = frameN  # exact frame index
            key_resp_blockEnd.tStart = t  # local t and not account for scr refresh
            key_resp_blockEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_blockEnd.started')
            key_resp_blockEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_blockEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_blockEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_blockEnd.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_blockEnd.getKeys(keyList=None, waitRelease=False)
            _key_resp_blockEnd_allKeys.extend(theseKeys)
            if len(_key_resp_blockEnd_allKeys):
                key_resp_blockEnd.keys = _key_resp_blockEnd_allKeys[-1].name  # just the last key pressed
                key_resp_blockEnd.rt = _key_resp_blockEnd_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockEndTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockEndText" ---
    for thisComponent in blockEndTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_blockEnd.keys in ['', [], None]:  # No response was made
        key_resp_blockEnd.keys = None
    blocks.addData('key_resp_blockEnd.keys',key_resp_blockEnd.keys)
    if key_resp_blockEnd.keys != None:  # we had a response
        blocks.addData('key_resp_blockEnd.rt', key_resp_blockEnd.rt)
    # the Routine "blockEndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# --- Prepare to start Routine "expEndText" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_totRew
totRew_text = "£%.2f" %(totalReward_tot);
finalReward_text.setText(totRew_text)
# keep track of which components have finished
expEndTextComponents = [textEndExp, finalReward_text]
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
frameN = -1

# --- Run Routine "expEndText" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textEndExp.started')
        textEndExp.setAutoDraw(True)
    if textEndExp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndExp.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndExp.tStop = t  # not accounting for scr refresh
            textEndExp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textEndExp.stopped')
            textEndExp.setAutoDraw(False)
    
    # *finalReward_text* updates
    if finalReward_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalReward_text.frameNStart = frameN  # exact frame index
        finalReward_text.tStart = t  # local t and not account for scr refresh
        finalReward_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalReward_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finalReward_text.started')
        finalReward_text.setAutoDraw(True)
    if finalReward_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finalReward_text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            finalReward_text.tStop = t  # not accounting for scr refresh
            finalReward_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finalReward_text.stopped')
            finalReward_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expEndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "expEndText" ---
for thisComponent in expEndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
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
