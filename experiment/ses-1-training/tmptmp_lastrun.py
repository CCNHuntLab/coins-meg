#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Thu Mar 31 12:48:22 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
psychopyVersion = '2022.1.1'
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
    originPath='/Users/laurence/Dropbox/Private/python/PsychoPy/experiments/tmp/tmptmp_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=True,
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
import pandas as pd;
import numpy as np;

storedStream = pd.read_csv('/Users/laurence/home/python/PsychoPy/experiments/rotation_task/stimgen/rotation_stream.csv',header=None);
storedStream_np = storedStream.values; #convert from Pandas to NumPy

nFrames = np.shape(storedStream_np)[0] - 1;
currentFrame = 0;

ROTATION_SPEED = 1;
SHIELD_GROWTH_SPEED = 0.04;
CIRCLE_RADIUS = 5;

shieldWidth = 2.5; #because it needs to be predefined

key_resp = keyboard.Keyboard()
shield = visual.ShapeStim(
    win=win, name='shield', vertices=[[0, 0], [shieldWidth, CIRCLE_RADIUS], [-shieldWidth, CIRCLE_RADIUS]],
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
inner_circle = visual.ShapeStim(
    win=win, name='inner_circle',units='cm', 
    size=(CIRCLE_RADIUS*0.9, CIRCLE_RADIUS*0.9), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6549, 0.6549, 0.6549], fillColor=[0.6549, 0.6549, 0.6549],
    opacity=None, depth=-3.0, interpolate=True)
laser = visual.ShapeStim(
    win=win, name='laser', vertices=[[0, 0], [0, CIRCLE_RADIUS]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
aperture = visual.Aperture(
    win=win, name='aperture',
    units='cm', size=[CIRCLE_RADIUS*1.05], pos=(0, 0), ori=0.0,
    shape='circle', anchor='center'
)
aperture.disable()  # disable until its actually used

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
shieldWidth = 2.5;
laserRotation = storedStream_np[0,1];
shieldRotation = storedStream_np[0,1]; #begin aligned to laser

#update variables to draw polygon
laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
#laserRotation_present = 270 - laserRotation; #to make it point centrally

key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
laser.setPos((0, 0))
laser.setSize((1, 1))
# keep track of which components have finished
trialComponents = [key_resp, shield, inner_circle, laser, aperture]
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
    #if key is pressed, rotate cursor
    if 'right' in key_resp.keys:
        shieldRotation -= ROTATION_SPEED;
    
    if 'left' in key_resp.keys:
        shieldRotation += ROTATION_SPEED;
    
    if 'up' in key_resp.keys:
        shieldWidth += SHIELD_GROWTH_SPEED;
    
    if 'down' in key_resp.keys:
        shieldWidth -= SHIELD_GROWTH_SPEED;
    
    #set lower boundary on shieldWidth
    if shieldWidth <= SHIELD_GROWTH_SPEED:
        shieldWidth = SHIELD_GROWTH_SPEED;
    
    laserRotation = storedStream_np[currentFrame,1]
    currentFrame = currentFrame + 1;
    
    
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and frameN >= 0:
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
    if key_resp.status == STARTED:
        if frameN >= (key_resp.frameNStart + nFrames):
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['up','down','left','right','space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
    
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
        shield.setOri(shieldRotation, log=False)
        shield.setVertices([[0, 0], [shieldWidth, CIRCLE_RADIUS], [-shieldWidth, CIRCLE_RADIUS]], log=False)
    
    # *inner_circle* updates
    if inner_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inner_circle.frameNStart = frameN  # exact frame index
        inner_circle.tStart = t  # local t and not account for scr refresh
        inner_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inner_circle, 'tStartRefresh')  # time at next scr refresh
        inner_circle.setAutoDraw(True)
    if inner_circle.status == STARTED:
        if frameN >= (inner_circle.frameNStart + nFrames):
            # keep track of stop time/frame for later
            inner_circle.tStop = t  # not accounting for scr refresh
            inner_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inner_circle, 'tStopRefresh')  # time at next scr refresh
            inner_circle.setAutoDraw(False)
    
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
        laser.setVertices([[0, 0], [0, CIRCLE_RADIUS]], log=False)
    
# *aperture* updates
    if aperture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        aperture.frameNStart = frameN  # exact frame index
        aperture.tStart = t  # local t and not account for scr refresh
        aperture.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(aperture, 'tStartRefresh')  # time at next scr refresh
        aperture.enabled = True
    if aperture.status == STARTED:
        if frameN >= (aperture.frameNStart + nFrames):
            # keep track of stop time/frame for later
            aperture.tStop = t  # not accounting for scr refresh
            aperture.frameNStop = frameN  # exact frame index
            win.timeOnFlip(aperture, 'tStopRefresh')  # time at next scr refresh
            aperture.enabled = False
    
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
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('shield.started', shield.tStartRefresh)
thisExp.addData('shield.stopped', shield.tStopRefresh)
thisExp.addData('inner_circle.started', inner_circle.tStartRefresh)
thisExp.addData('inner_circle.stopped', inner_circle.tStopRefresh)
thisExp.addData('laser.started', laser.tStartRefresh)
thisExp.addData('laser.stopped', laser.tStopRefresh)
aperture.enabled = False  # just in case it was left enabled
thisExp.addData('aperture.started', aperture.tStartRefresh)
thisExp.addData('aperture.stopped', aperture.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
