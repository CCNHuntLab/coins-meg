#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on May 18, 2023, at 15:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel, iohub, hardware
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
psychopyVersion = '2021.2.3'
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
    originPath='E:\\Experiments\\Lorenzo_Amy_COINS_MEG\\rotation_task_v2 (s001 14-7)\\rotation_task_v2\\rotation_task_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
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

# Setup eyetracking
ioDevice = 'eyetracker.hw.sr_research.eyelink.EyeTracker'
ioConfig = {
    ioDevice: {
        'name': 'tracker',
        'model_name': 'EYELINK 1000 DESKTOP',
        'simulation_mode': False,
        'network_settings': '100.1.1.1',
        'default_native_data_file_name': 'EXPFILE',
        'runtime_settings': {
            'sampling_rate': 1000.0,
            'track_eyes': 'BOTH',
            'sample_filtering': {
                'sample_filtering': 'FILTER_LEVEL_2',
                'elLiveFiltering': 'FILTER_LEVEL_OFF',
            },
            'vog_settings': {
                'pupil_measure_types': 'PUPIL_AREA',
                'tracking_mode': 'PUPIL_CR_TRACKING',
                'pupil_center_algorithm': 'ELLIPSE_FIT',
            }
        }
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions_1"
instructions_1Clock = core.Clock()
#import necessary packages
import numpy as np;
import os;

#keyboard constants
session = 1;

kb = keyboard.Keyboard()

if session == 1:
    keys_move = ['2', '1'];
    keys_size = ['4', '3'];
    key_right = '2';
    key_left = '1';
    key_up = '4';
    key_down = '3';
if session == 2:
    keys_move = ['4', '3'];
    keys_size = ['2', '1']
    key_right = '4';
    key_left = '3';
    key_up = '2';
    key_down = '1';

#set constants for the experiment
ROTATION_SPEED = 1;
CIRCLE_RADIUS = 3;

SHIELD_GROWTH_SPEED = 20; #in degrees

minShieldDegrees = 20;
maxShieldDegrees = 60;

#initialise variables that will be updated as experiment progresses

#shield variables
shieldDegrees = 40; #because it needs to be predefined
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;

#calculate the screen X and Y locations that correspond to the shield centre
shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
shieldX = np.concatenate(([0],shieldX));
shieldY = np.concatenate(([0],shieldY));
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

shieldRotation = 360; #begin at top

#initialise list containing data to be saved
saveData = [["blockID","currentFrame","laserRotation","shieldRotation","shieldDegrees","currentHit","totalReward","sendTrigger","triggerValue","trueMean","trueVariance","volatility", "eyePosition"]]
saveFilename = "savedData_" + str(expInfo['participant']) + str(expInfo['session']) + ".csv" #load stimulusStream into NumPy array

#reward variables
wins = 0;

if wins == 0:
    totalReward_tot = 0;
else:
    totalReward_tot = 0;

lossFactor = 0.003;

totalReward_text = '';
totRew_text = '';

win.mouseVisible = False

#progress circle variables
pc_orientation = 0;
pc_degrees = 0;
pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
pc_X = np.concatenate(([0],pc_X));
pc_Y = np.concatenate(([0],pc_Y));
pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))
text_instructions_1 = visual.TextStim(win=win, name='text_instructions_1',
    text='Beginning of a new session of the Save-the-world game.\n\nSave the world (and earn money) by navigating the shield to where you expect radiation to hit Earth.\u200b\n\nPress any key to start.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_i1 = keyboard.Keyboard()
instructions_trigger = parallel.ParallelPort(address='0x4FF8')

# Initialize components for Routine "blockStartText"
blockStartTextClock = core.Clock()
radioactive_block_source = visual.ImageStim(
    win=win,
    name='radioactive_block_source', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_sourceImage = visual.TextStim(win=win, name='text_sourceImage',
    text="Please remember to keep your eyes as fixed as possible on the centre of the screen.\n\nNew source ahead:\n\n\n\n\n\n\n\nPress any key if you're ready to start.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_blockStart = keyboard.Keyboard()
blockStart_trigger = parallel.ParallelPort(address='0x4FF8')

# Initialize components for Routine "trial"
trialClock = core.Clock()
harmless_area = visual.ShapeStim(
    win=win, name='harmless_area',units='cm', 
    size=(6.6, 6.6), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-1.0, interpolate=True)
shield = visual.ShapeStim(
    win=win, name='shield', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
shield_centre = visual.ShapeStim(
    win=win, name='shield_centre', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
shield_bg_short = visual.ShapeStim(
    win=win, name='shield_bg_short', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
laser = visual.ShapeStim(
    win=win, name='laser', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0],
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-5.0, interpolate=True)
laser_long = visual.ShapeStim(
    win=win, name='laser_long', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.4]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0],
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-6.0, interpolate=True)
progress_bar = visual.ShapeStim(
    win=win, name='progress_bar', vertices=pc_coords,units='cm', 
    size=(0.3, 0.3),
    ori=1.0, pos=(0, 0),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='green', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
radioactive = visual.ImageStim(
    win=win,
    name='radioactive', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
trialTrigger = parallel.ParallelPort(address='0x4FF8')

# Initialize components for Routine "blockEndText"
blockEndTextClock = core.Clock()
textPause = visual.TextStim(win=win, name='textPause',
    text='Well done. In this block, you earned:\n\n\n\n\n\n\nTake a short break.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
textReward = visual.TextStim(win=win, name='textReward',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
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
blockEnd_reward_trigger = parallel.ParallelPort(address='0x4FF8')

# Initialize components for Routine "sessionEndText"
sessionEndTextClock = core.Clock()
textEndSession = visual.TextStim(win=win, name='textEndSession',
    text='Well done. You completed one session. \nIn this session, you made:\n\n\n\n\nTake a break. ',
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
end_trigger = parallel.ParallelPort(address='0x4FF8')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_i1.keys = []
key_resp_i1.rt = []
_key_resp_i1_allKeys = []
# keep track of which components have finished
instructions_1Components = [text_instructions_1, key_resp_i1, instructions_trigger]
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
instructions_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_1"-------
while continueRoutine:
    # get current time
    t = instructions_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions_1* updates
    if text_instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_1.frameNStart = frameN  # exact frame index
        text_instructions_1.tStart = t  # local t and not account for scr refresh
        text_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_1, 'tStartRefresh')  # time at next scr refresh
        text_instructions_1.setAutoDraw(True)
    
    # *key_resp_i1* updates
    waitOnFlip = False
    if key_resp_i1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_i1.frameNStart = frameN  # exact frame index
        key_resp_i1.tStart = t  # local t and not account for scr refresh
        key_resp_i1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_i1, 'tStartRefresh')  # time at next scr refresh
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
    # *instructions_trigger* updates
    if instructions_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_trigger.frameNStart = frameN  # exact frame index
        instructions_trigger.tStart = t  # local t and not account for scr refresh
        instructions_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_trigger, 'tStartRefresh')  # time at next scr refresh
        instructions_trigger.status = STARTED
        win.callOnFlip(instructions_trigger.setData, int(100))
    if instructions_trigger.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_trigger.tStartRefresh + 0.05-frameTolerance:
            # keep track of stop time/frame for later
            instructions_trigger.tStop = t  # not accounting for scr refresh
            instructions_trigger.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_trigger, 'tStopRefresh')  # time at next scr refresh
            instructions_trigger.status = FINISHED
            win.callOnFlip(instructions_trigger.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_1"-------
for thisComponent in instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_instructions_1.started', text_instructions_1.tStartRefresh)
thisExp.addData('text_instructions_1.stopped', text_instructions_1.tStopRefresh)
# check responses
if key_resp_i1.keys in ['', [], None]:  # No response was made
    key_resp_i1.keys = None
thisExp.addData('key_resp_i1.keys',key_resp_i1.keys)
if key_resp_i1.keys != None:  # we had a response
    thisExp.addData('key_resp_i1.rt', key_resp_i1.rt)
thisExp.addData('key_resp_i1.started', key_resp_i1.tStartRefresh)
thisExp.addData('key_resp_i1.stopped', key_resp_i1.tStopRefresh)
thisExp.nextEntry()
if instructions_trigger.status == STARTED:
    win.callOnFlip(instructions_trigger.setData, int(0))
thisExp.addData('instructions_trigger.started', instructions_trigger.tStartRefresh)
thisExp.addData('instructions_trigger.stopped', instructions_trigger.tStopRefresh)
# the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimgen/blocks_main4 - 2 - P019.csv'),
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
    #determine radioactive source image
    rootdir = os.getcwd()
    sourceImageFile = os.path.join(rootdir,'images',sourceImage)
    radioactive_block_source.setImage(sourceImageFile)
    key_resp_blockStart.keys = []
    key_resp_blockStart.rt = []
    _key_resp_blockStart_allKeys = []
    # keep track of which components have finished
    blockStartTextComponents = [radioactive_block_source, text_sourceImage, key_resp_blockStart, blockStart_trigger]
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
        
        # *radioactive_block_source* updates
        if radioactive_block_source.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            radioactive_block_source.frameNStart = frameN  # exact frame index
            radioactive_block_source.tStart = t  # local t and not account for scr refresh
            radioactive_block_source.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive_block_source, 'tStartRefresh')  # time at next scr refresh
            radioactive_block_source.setAutoDraw(True)
        
        # *text_sourceImage* updates
        if text_sourceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sourceImage.frameNStart = frameN  # exact frame index
            text_sourceImage.tStart = t  # local t and not account for scr refresh
            text_sourceImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sourceImage, 'tStartRefresh')  # time at next scr refresh
            text_sourceImage.setAutoDraw(True)
        
        # *key_resp_blockStart* updates
        waitOnFlip = False
        if key_resp_blockStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockStart.frameNStart = frameN  # exact frame index
            key_resp_blockStart.tStart = t  # local t and not account for scr refresh
            key_resp_blockStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockStart, 'tStartRefresh')  # time at next scr refresh
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
        # *blockStart_trigger* updates
        if blockStart_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blockStart_trigger.frameNStart = frameN  # exact frame index
            blockStart_trigger.tStart = t  # local t and not account for scr refresh
            blockStart_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blockStart_trigger, 'tStartRefresh')  # time at next scr refresh
            blockStart_trigger.status = STARTED
            win.callOnFlip(blockStart_trigger.setData, int(10))
        if blockStart_trigger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blockStart_trigger.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                blockStart_trigger.tStop = t  # not accounting for scr refresh
                blockStart_trigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blockStart_trigger, 'tStopRefresh')  # time at next scr refresh
                blockStart_trigger.status = FINISHED
                win.callOnFlip(blockStart_trigger.setData, int(0))
        
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
    blocks.addData('radioactive_block_source.started', radioactive_block_source.tStartRefresh)
    blocks.addData('radioactive_block_source.stopped', radioactive_block_source.tStopRefresh)
    blocks.addData('text_sourceImage.started', text_sourceImage.tStartRefresh)
    blocks.addData('text_sourceImage.stopped', text_sourceImage.tStopRefresh)
    # check responses
    if key_resp_blockStart.keys in ['', [], None]:  # No response was made
        key_resp_blockStart.keys = None
    blocks.addData('key_resp_blockStart.keys',key_resp_blockStart.keys)
    if key_resp_blockStart.keys != None:  # we had a response
        blocks.addData('key_resp_blockStart.rt', key_resp_blockStart.rt)
    blocks.addData('key_resp_blockStart.started', key_resp_blockStart.tStartRefresh)
    blocks.addData('key_resp_blockStart.stopped', key_resp_blockStart.tStopRefresh)
    if blockStart_trigger.status == STARTED:
        win.callOnFlip(blockStart_trigger.setData, int(0))
    blocks.addData('blockStart_trigger.started', blockStart_trigger.tStartRefresh)
    blocks.addData('blockStart_trigger.stopped', blockStart_trigger.tStopRefresh)
    # the Routine "blockStartText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    #initialise variables that will be updated as experiment progresses
    shieldDegrees = 20; #because it needs to be predefined
    
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
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
    
    if wins == 0:
        totalReward = 1;
    else:
        totalReward = 3.5;
    
    unique, counts = np.unique(storedStream_np, return_counts=True);
    laser_on = min(counts);
    laser_frame_ct = 0;
    
    laser.setAutoDraw(False);
    laser_long.setAutoDraw(False);
    
    #progress circle variables
    pc_orientation = 0;
    pc_degrees = 0;
    pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_X = np.concatenate(([0],pc_X));
    pc_Y = np.concatenate(([0],pc_Y));
    pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))
    laser.setPos((0, 0))
    laser.setSize((1, 1))
    laser_long.setPos((0, 0))
    laser_long.setSize((1, 1))
    radioactive.setImage(sourceImageFile)
    # keep track of which components have finished
    trialComponents = [harmless_area, shield, shield_centre, shield_bg_short, laser, laser_long, progress_bar, radioactive, trialTrigger]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #determine whether laser is crossing the shield
        if hit_i:
            hit_i = 0
        else:
            if first_hit:
                laser_long.setAutoDraw(True)
        
        if totalReward <= 0:
            if wins == 0:        
                totalReward = 0.1;
            if wins == 1:
                totalReward = 0;
        
        #do not send a trigger on every frame, only if laser position changes or subject presses a button
        sendTrigger = False
        keyReleaseThisFrame = False
        triggerValue = 0
        win.callOnFlip(trialTrigger.setData, int(0))
        
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=keys_move,clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=True,waitRelease=False)
            triggerValue = 7
            sendTrigger = True
            win.callOnFlip(trialTrigger.setData, int(triggerValue))
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
                win.callOnFlip(trialTrigger.setData, int(triggerValue))
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
            win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
        #set lower boundary on shieldWidth
        if shieldDegrees < minShieldDegrees:
            shieldDegrees = minShieldDegrees;
            
        #set upper boundary on shieldWidth
        if shieldDegrees > maxShieldDegrees:
            shieldDegrees = maxShieldDegrees;
            
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
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
        
                sendTrigger = True
                win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
            if currentHit:
                if wins == 0:
                    if shieldDegrees == 20:
                        totalReward = totalReward;
                    if shieldDegrees == 40:
                        totalReward = totalReward - lossFactor/3;
                    if shieldDegrees == 60:
                        totalReward = totalReward - lossFactor/2;
                if wins == 1:
                    if shieldDegrees == 20:
                        totalReward = totalReward + 2*0.00003;
                    if shieldDegrees == 40:
                        totalReward = totalReward;
                    if shieldDegrees == 60:
                        totalReward = totalReward - 2*0.00003;
                
                hit_i = 1;
                first_hit = 1;
            else:
                if totalReward > 0:
                    totalReward = totalReward - lossFactor;
                else:
                    totalReward = 0;
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
                    win.callOnFlip(trialTrigger.setData, int(triggerValue))
            
                if currentHit:
                    if wins == 0:
                        if shieldDegrees == 20:
                            totalReward = totalReward;
                        if shieldDegrees == 40:
                            totalReward = totalReward - lossFactor/3;
                        if shieldDegrees == 60:
                            totalReward = totalReward - lossFactor/2;
                    if wins == 1:
                        if shieldDegrees == 20:
                            totalReward = totalReward + 2*0.00003;
                        if shieldDegrees == 40:
                            totalReward = totalReward;
                        if shieldDegrees == 60:
                            totalReward = totalReward - 2*0.00003;
                    hit_i = 1
                    first_hit = 1
                else:
                    if totalReward > 0:
                        totalReward = totalReward - lossFactor;
                    else:
                        totalReward = 0;
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            if shieldDegrees == 20:
                laser_long_opacity = 0;
            if shieldDegrees == 40:
                laser_long_opacity = 0.1;
            if shieldDegrees == 60:
                laser_long_opacity = 0.3;
            
            shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
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
            win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
        pc_orientation = pc_orientation + (360/nFrames)/2;
        pc_degrees = pc_degrees + (360/nFrames)/2;
        pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
        pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
        pc_X = np.concatenate(([0],pc_X));
        pc_Y = np.concatenate(([0],pc_Y));
        pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))
        
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
        
        # *shield_bg_short* updates
        if shield_bg_short.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_bg_short.frameNStart = frameN  # exact frame index
            shield_bg_short.tStart = t  # local t and not account for scr refresh
            shield_bg_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_bg_short, 'tStartRefresh')  # time at next scr refresh
            shield_bg_short.setAutoDraw(True)
        if shield_bg_short.status == STARTED:
            if frameN >= (shield_bg_short.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_bg_short.tStop = t  # not accounting for scr refresh
                shield_bg_short.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_bg_short, 'tStopRefresh')  # time at next scr refresh
                shield_bg_short.setAutoDraw(False)
        if shield_bg_short.status == STARTED:  # only update if drawing
            shield_bg_short.setFillColor([0, 0, 0], log=False)
            shield_bg_short.setOri(shieldRotation, log=False)
            shield_bg_short.setVertices(shieldCoords, log=False)
            shield_bg_short.setLineColor([0, 0, 0], log=False)
        
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
            laser_long.setOpacity(laser_long_opacity, log=False)
            laser_long.setOri(laserRotation, log=False)
            laser_long.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
        
        # *progress_bar* updates
        if progress_bar.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            progress_bar.frameNStart = frameN  # exact frame index
            progress_bar.tStart = t  # local t and not account for scr refresh
            progress_bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_bar, 'tStartRefresh')  # time at next scr refresh
            progress_bar.setAutoDraw(True)
        if progress_bar.status == STARTED:
            if frameN >= (progress_bar.frameNStart + nFrames):
                # keep track of stop time/frame for later
                progress_bar.tStop = t  # not accounting for scr refresh
                progress_bar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_bar, 'tStopRefresh')  # time at next scr refresh
                progress_bar.setAutoDraw(False)
        if progress_bar.status == STARTED:  # only update if drawing
            progress_bar.setOri(pc_orientation, log=False)
            progress_bar.setVertices(pc_coords, log=False)
        
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
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    totalReward_tot = totalReward_tot + totalReward;
    totalReward_text = "£%.2f" %(totalReward);
    
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    win.callOnFlip(trialTrigger.setData, int(0))
    triggerValue = 0;
    sendTrigger = False;
    blocks.addData('harmless_area.started', harmless_area.tStartRefresh)
    blocks.addData('harmless_area.stopped', harmless_area.tStopRefresh)
    blocks.addData('shield.started', shield.tStartRefresh)
    blocks.addData('shield.stopped', shield.tStopRefresh)
    blocks.addData('shield_centre.started', shield_centre.tStartRefresh)
    blocks.addData('shield_centre.stopped', shield_centre.tStopRefresh)
    blocks.addData('shield_bg_short.started', shield_bg_short.tStartRefresh)
    blocks.addData('shield_bg_short.stopped', shield_bg_short.tStopRefresh)
    blocks.addData('laser.started', laser.tStartRefresh)
    blocks.addData('laser.stopped', laser.tStopRefresh)
    blocks.addData('laser_long.started', laser_long.tStartRefresh)
    blocks.addData('laser_long.stopped', laser_long.tStopRefresh)
    blocks.addData('progress_bar.started', progress_bar.tStartRefresh)
    blocks.addData('progress_bar.stopped', progress_bar.tStopRefresh)
    blocks.addData('radioactive.started', radioactive.tStartRefresh)
    blocks.addData('radioactive.stopped', radioactive.tStopRefresh)
    if trialTrigger.status == STARTED:
        win.callOnFlip(trialTrigger.setData, int(0))
    blocks.addData('trialTrigger.started', trialTrigger.tStartRefresh)
    blocks.addData('trialTrigger.stopped', trialTrigger.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blockEndText"-------
    continueRoutine = True
    # update component parameters for each repeat
    rewardFeedback = "£%.2f" %(totalReward);
    textReward.setText(rewardFeedback)
    key_resp_blockEnd.keys = []
    key_resp_blockEnd.rt = []
    _key_resp_blockEnd_allKeys = []
    # keep track of which components have finished
    blockEndTextComponents = [textPause, textReward, textContinue, key_resp_blockEnd, blockEnd_reward_trigger]
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
        
        # *textReward* updates
        if textReward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textReward.frameNStart = frameN  # exact frame index
            textReward.tStart = t  # local t and not account for scr refresh
            textReward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textReward, 'tStartRefresh')  # time at next scr refresh
            textReward.setAutoDraw(True)
        if textReward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textReward.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textReward.tStop = t  # not accounting for scr refresh
                textReward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textReward, 'tStopRefresh')  # time at next scr refresh
                textReward.setAutoDraw(False)
        
        # *textContinue* updates
        if textContinue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            textContinue.frameNStart = frameN  # exact frame index
            textContinue.tStart = t  # local t and not account for scr refresh
            textContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinue, 'tStartRefresh')  # time at next scr refresh
            textContinue.setAutoDraw(True)
        
        # *key_resp_blockEnd* updates
        waitOnFlip = False
        if key_resp_blockEnd.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockEnd.frameNStart = frameN  # exact frame index
            key_resp_blockEnd.tStart = t  # local t and not account for scr refresh
            key_resp_blockEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockEnd, 'tStartRefresh')  # time at next scr refresh
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
        # *blockEnd_reward_trigger* updates
        if blockEnd_reward_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blockEnd_reward_trigger.frameNStart = frameN  # exact frame index
            blockEnd_reward_trigger.tStart = t  # local t and not account for scr refresh
            blockEnd_reward_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blockEnd_reward_trigger, 'tStartRefresh')  # time at next scr refresh
            blockEnd_reward_trigger.status = STARTED
            win.callOnFlip(blockEnd_reward_trigger.setData, int(20))
        if blockEnd_reward_trigger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blockEnd_reward_trigger.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                blockEnd_reward_trigger.tStop = t  # not accounting for scr refresh
                blockEnd_reward_trigger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blockEnd_reward_trigger, 'tStopRefresh')  # time at next scr refresh
                blockEnd_reward_trigger.status = FINISHED
                win.callOnFlip(blockEnd_reward_trigger.setData, int(0))
        
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
    blocks.addData('textReward.started', textReward.tStartRefresh)
    blocks.addData('textReward.stopped', textReward.tStopRefresh)
    blocks.addData('textContinue.started', textContinue.tStartRefresh)
    blocks.addData('textContinue.stopped', textContinue.tStopRefresh)
    # check responses
    if key_resp_blockEnd.keys in ['', [], None]:  # No response was made
        key_resp_blockEnd.keys = None
    blocks.addData('key_resp_blockEnd.keys',key_resp_blockEnd.keys)
    if key_resp_blockEnd.keys != None:  # we had a response
        blocks.addData('key_resp_blockEnd.rt', key_resp_blockEnd.rt)
    blocks.addData('key_resp_blockEnd.started', key_resp_blockEnd.tStartRefresh)
    blocks.addData('key_resp_blockEnd.stopped', key_resp_blockEnd.tStopRefresh)
    if blockEnd_reward_trigger.status == STARTED:
        win.callOnFlip(blockEnd_reward_trigger.setData, int(0))
    blocks.addData('blockEnd_reward_trigger.started', blockEnd_reward_trigger.tStartRefresh)
    blocks.addData('blockEnd_reward_trigger.stopped', blockEnd_reward_trigger.tStopRefresh)
    # the Routine "blockEndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# ------Prepare to start Routine "sessionEndText"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
totRew_text = "£%.2f" %(totalReward_tot);
finalReward_text.setText(totRew_text)
# keep track of which components have finished
sessionEndTextComponents = [textEndSession, finalReward_text, end_trigger]
for thisComponent in sessionEndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sessionEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sessionEndText"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sessionEndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sessionEndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndSession* updates
    if textEndSession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndSession.frameNStart = frameN  # exact frame index
        textEndSession.tStart = t  # local t and not account for scr refresh
        textEndSession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndSession, 'tStartRefresh')  # time at next scr refresh
        textEndSession.setAutoDraw(True)
    if textEndSession.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndSession.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndSession.tStop = t  # not accounting for scr refresh
            textEndSession.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndSession, 'tStopRefresh')  # time at next scr refresh
            textEndSession.setAutoDraw(False)
    
    # *finalReward_text* updates
    if finalReward_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalReward_text.frameNStart = frameN  # exact frame index
        finalReward_text.tStart = t  # local t and not account for scr refresh
        finalReward_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalReward_text, 'tStartRefresh')  # time at next scr refresh
        finalReward_text.setAutoDraw(True)
    if finalReward_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finalReward_text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            finalReward_text.tStop = t  # not accounting for scr refresh
            finalReward_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finalReward_text, 'tStopRefresh')  # time at next scr refresh
            finalReward_text.setAutoDraw(False)
    # *end_trigger* updates
    if end_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_trigger.frameNStart = frameN  # exact frame index
        end_trigger.tStart = t  # local t and not account for scr refresh
        end_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_trigger, 'tStartRefresh')  # time at next scr refresh
        end_trigger.status = STARTED
        win.callOnFlip(end_trigger.setData, int(105))
    if end_trigger.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_trigger.tStartRefresh + 0.05-frameTolerance:
            # keep track of stop time/frame for later
            end_trigger.tStop = t  # not accounting for scr refresh
            end_trigger.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_trigger, 'tStopRefresh')  # time at next scr refresh
            end_trigger.status = FINISHED
            win.callOnFlip(end_trigger.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sessionEndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sessionEndText"-------
for thisComponent in sessionEndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEndSession.started', textEndSession.tStartRefresh)
thisExp.addData('textEndSession.stopped', textEndSession.tStopRefresh)
thisExp.addData('finalReward_text.started', finalReward_text.tStartRefresh)
thisExp.addData('finalReward_text.stopped', finalReward_text.tStopRefresh)
if end_trigger.status == STARTED:
    win.callOnFlip(end_trigger.setData, int(0))
thisExp.addData('end_trigger.started', end_trigger.tStartRefresh)
thisExp.addData('end_trigger.stopped', end_trigger.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
