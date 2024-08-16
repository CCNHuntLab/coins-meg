/********************** 
 * Rotation_Task Test *
 **********************/


// store info about the experiment session:
let expName = 'rotation_task';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin(blocksLoopScheduler));
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(expEndTextRoutineBegin());
flowScheduler.add(expEndTextRoutineEachFrame());
flowScheduler.add(expEndTextRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimgen/blocks.csv', 'path': 'stimgen/blocks.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.2';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the laser task!\n\nRemember to catch as many lasers as possible by moving the shield.\n\nYou will gain more energy the smaller your shield is.\n\nPress any key to start.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blockStartText"
  blockStartTextClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: "New block ahead.\n\nPress any key if you're ready to start.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  import * as pd from 'pandas';
  import * as np from 'numpy';
  import * as math from 'math';
  import * as os from 'os';
  var CIRCLE_RADIUS, ROTATION_SPEED, SHIELD_DECAY_RATE, SHIELD_GROWTH_SPEED, kb, maxShieldDegrees, minShieldDegrees, rootdir, saveData, saveFilename, shieldCoords, shieldDegrees, shieldHeight, shieldRedness, shieldWidth, shieldX, shieldY, totalReward;
  kb = new keyboard.Keyboard();
  rootdir = os.getcwd();
  ROTATION_SPEED = 1;
  SHIELD_GROWTH_SPEED = 20;
  SHIELD_DECAY_RATE = 0.99;
  CIRCLE_RADIUS = 3;
  shieldDegrees = 45;
  shieldWidth = ((np.sin(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldHeight = ((np.cos(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldX = ((np.sin(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldY = ((np.cos(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldX = np.concatenate([[0], shieldX]);
  shieldY = np.concatenate([[0], shieldY]);
  shieldCoords = np.transpose(np.vstack([shieldX, shieldY]));
  shieldRedness = 0;
  minShieldDegrees = 25;
  maxShieldDegrees = 65;
  totalReward = 0;
  saveData = [["currentFrame", "laserRotation", "shieldRotation", "shieldDegrees", "currentHit", "totalReward"]];
  saveFilename = "savedData.csv";
  
  shield = new visual.Polygon ({
    win: psychoJS.window, name: 'shield', units : 'height', 
    edges: 4, size:[1, 1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  inner_circle = new visual.Polygon({
    win: psychoJS.window, name: 'inner_circle', units : 'height', 
    edges: 100, size:[(CIRCLE_RADIUS * 2), (CIRCLE_RADIUS * 2)],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([0.6549, 0.6549, 0.6549]),
    fillColor: new util.Color([0.6549, 0.6549, 0.6549]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  laser = new visual.Polygon ({
    win: psychoJS.window, name: 'laser', units : 'height', 
    edges: 4, size:[1.0, 1.0],
    ori: 1.0, pos: [0, 0],
    lineWidth: 10.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  reward_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'reward_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.02], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "blockEndText"
  blockEndTextClock = new util.Clock();
  textPause = new visual.TextStim({
    win: psychoJS.window,
    name: 'textPause',
    text: 'Well done.\n\nTake a short break.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'textContinue',
    text: 'Press any key to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "expEndText"
  expEndTextClock = new util.Clock();
  textEndExp = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEndExp',
    text: 'Well done. You completed all blocks.\n\nThank you',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text);
    instructionsComponents.push(key_resp);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructions'-------
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimgen/blocks.csv',
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    blocks.forEach(function() {
      const snapshot = blocks.getSnapshot();
    
      blocksLoopScheduler.add(importConditions(snapshot));
      blocksLoopScheduler.add(blockStartTextRoutineBegin(snapshot));
      blocksLoopScheduler.add(blockStartTextRoutineEachFrame());
      blocksLoopScheduler.add(blockStartTextRoutineEnd());
      blocksLoopScheduler.add(trialRoutineBegin(snapshot));
      blocksLoopScheduler.add(trialRoutineEachFrame());
      blocksLoopScheduler.add(trialRoutineEnd());
      blocksLoopScheduler.add(blockEndTextRoutineBegin(snapshot));
      blocksLoopScheduler.add(blockEndTextRoutineEachFrame());
      blocksLoopScheduler.add(blockEndTextRoutineEnd());
      blocksLoopScheduler.add(endLoopIteration(blocksLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}

function blockStartTextRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'blockStartText'-------
    t = 0;
    blockStartTextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    blockStartTextComponents = [];
    blockStartTextComponents.push(text_2);
    blockStartTextComponents.push(key_resp_2);
    
    blockStartTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function blockStartTextRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'blockStartText'-------
    // get current time
    t = blockStartTextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    blockStartTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function blockStartTextRoutineEnd() {
  return async function () {
    //------Ending Routine 'blockStartText'-------
    blockStartTextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "blockStartText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stimStreamPath = os.path.join(rootdir, "stimgen", blockFileName);
    storedStream_np = np.loadtxt(stimStreamPath, {"delimiter": ","});
    nFrames = (np.shape(storedStream_np)[0] - 1);
    currentFrame = 0;
    laserRotation = storedStream_np[[0, 1]];
    shieldRotation = 0;
    laserXcoord = (CIRCLE_RADIUS * Math.cos(deg2rad(laserRotation)));
    laserYcoord = (CIRCLE_RADIUS * Math.sin(deg2rad(laserRotation)));
    
    laser.setPos([0, 0]);
    laser.setSize([1, 1]);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(shield);
    trialComponents.push(inner_circle);
    trialComponents.push(laser);
    trialComponents.push(reward_text);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    LRkeys_released = kb.getKeys({"keyList": ["right", "left"], "clear": true, "waitRelease": true});
    if ((LRkeys_released.length > 0)) {
        LRkeys_pressed = kb.getKeys({"keyList": ["right", "left"], "clear": true, "waitRelease": false});
    } else {
        LRkeys_pressed = kb.getKeys({"keyList": ["right", "left"], "clear": false, "waitRelease": false});
    }
    UDkeys_pressed = kb.getKeys({"keyList": ["up", "down"], "clear": true, "waitRelease": false});
    if ((LRkeys_pressed.length > 0)) {
        if ((LRkeys_pressed.slice((- 1))[0] === "right")) {
            shieldRotation += ROTATION_SPEED;
        }
        if ((LRkeys_pressed.slice((- 1))[0] === "left")) {
            shieldRotation -= ROTATION_SPEED;
        }
    }
    if ((UDkeys_pressed.length > 0)) {
        if ((UDkeys_pressed.slice((- 1))[0] === "up")) {
            shieldDegrees += SHIELD_GROWTH_SPEED;
        }
        if ((UDkeys_pressed.slice((- 1))[0] === "down")) {
            shieldDegrees -= SHIELD_GROWTH_SPEED;
        }
    }
    if ((shieldDegrees < minShieldDegrees)) {
        shieldDegrees = minShieldDegrees;
    }
    if ((shieldDegrees > maxShieldDegrees)) {
        shieldDegrees = maxShieldDegrees;
    }
    shieldWidth = ((np.sin(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
    shieldHeight = ((np.cos(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
    shieldX = ((np.sin(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
    shieldY = ((np.cos(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
    shieldX = np.concatenate([[0], shieldX]);
    shieldY = np.concatenate([[0], shieldY]);
    shieldCoords = np.transpose(np.vstack([shieldX, shieldY]));
    if ((currentFrame < nFrames)) {
        laserRotation = storedStream_np[[currentFrame, 1]];
    }
    currentHit = ((((shieldRotation - laserRotation) + shieldDegrees) % 360) <= (2 * shieldDegrees));
    if (currentHit) {
        shieldRedness = (shieldRedness * SHIELD_DECAY_RATE);
        update = ((minShieldDegrees / 50) / shieldDegrees);
        shieldRedness = Math.min((shieldRedness + update), 2);
        shieldColour = [1, (1 - shieldRedness), (1 - shieldRedness)];
        laserColour = [1, (- 1), (- 1)];
    } else {
        shieldRedness = (shieldRedness * SHIELD_DECAY_RATE);
        shieldColour = [1, (1 - shieldRedness), (1 - shieldRedness)];
        laserColour = [1, 1, 1];
    }
    totalReward = (totalReward + (shieldRedness / 100));
    textReward = Math.round(totalReward, 1).toString();
    if ((currentFrame < nFrames)) {
        saveData.push([currentFrame, laserRotation, shieldRotation, shieldDegrees, currentHit, totalReward]);
        currentFrame = (currentFrame + 1);
    }
    
    
    // *shield* updates
    if (frameN >= 0 && shield.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield.tStart = t;  // (not accounting for frame time here)
      shield.frameNStart = frameN;  // exact frame index
      
      shield.setAutoDraw(true);
    }

    if (shield.status === PsychoJS.Status.STARTED && frameN >= (shield.frameNStart + nFrames)) {
      shield.setAutoDraw(false);
    }
    
    if (shield.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield.setFillColor(new util.Color(shieldColour), false);
      shield.setOri(shieldRotation, false);
      shield.setVertices(shieldCoords, false);
      shield.setLineColor(new util.Color(shieldColour), false);
    }
    
    // *inner_circle* updates
    if (t >= 0.0 && inner_circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inner_circle.tStart = t;  // (not accounting for frame time here)
      inner_circle.frameNStart = frameN;  // exact frame index
      
      inner_circle.setAutoDraw(true);
    }

    if (inner_circle.status === PsychoJS.Status.STARTED && frameN >= (inner_circle.frameNStart + nFrames)) {
      inner_circle.setAutoDraw(false);
    }
    
    // *laser* updates
    if (t >= 0.0 && laser.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      laser.tStart = t;  // (not accounting for frame time here)
      laser.frameNStart = frameN;  // exact frame index
      
      laser.setAutoDraw(true);
    }

    if (laser.status === PsychoJS.Status.STARTED && frameN >= (laser.frameNStart + nFrames)) {
      laser.setAutoDraw(false);
    }
    
    if (laser.status === PsychoJS.Status.STARTED){ // only update if being drawn
      laser.setFillColor(new util.Color(laserColour), false);
      laser.setOri(laserRotation, false);
      laser.setVertices([[0, 0], [0, (CIRCLE_RADIUS * 1.1)]], false);
      laser.setLineColor(new util.Color(laserColour), false);
    }
    
    // *reward_text* updates
    if (t >= 0.0 && reward_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reward_text.tStart = t;  // (not accounting for frame time here)
      reward_text.frameNStart = frameN;  // exact frame index
      
      reward_text.setAutoDraw(true);
    }

    if (reward_text.status === PsychoJS.Status.STARTED && frameN >= (reward_text.frameNStart + nFrames)) {
      reward_text.setAutoDraw(false);
    }
    
    if (reward_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      reward_text.setText(textReward, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    np.savetxt(saveFilename, saveData, {"delimiter": ",", "fmt": "%s"});
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function blockEndTextRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'blockEndText'-------
    t = 0;
    blockEndTextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    blockEndTextComponents = [];
    blockEndTextComponents.push(textPause);
    blockEndTextComponents.push(textContinue);
    blockEndTextComponents.push(key_resp_3);
    
    blockEndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function blockEndTextRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'blockEndText'-------
    // get current time
    t = blockEndTextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textPause* updates
    if (t >= 0.0 && textPause.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textPause.tStart = t;  // (not accounting for frame time here)
      textPause.frameNStart = frameN;  // exact frame index
      
      textPause.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textPause.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textPause.setAutoDraw(false);
    }
    
    // *textContinue* updates
    if (t >= 5.0 && textContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textContinue.tStart = t;  // (not accounting for frame time here)
      textContinue.frameNStart = frameN;  // exact frame index
      
      textContinue.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 5.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    blockEndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function blockEndTextRoutineEnd() {
  return async function () {
    //------Ending Routine 'blockEndText'-------
    blockEndTextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "blockEndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function expEndTextRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'expEndText'-------
    t = 0;
    expEndTextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    expEndTextComponents = [];
    expEndTextComponents.push(textEndExp);
    
    expEndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function expEndTextRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'expEndText'-------
    // get current time
    t = expEndTextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEndExp* updates
    if (t >= 0.0 && textEndExp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEndExp.tStart = t;  // (not accounting for frame time here)
      textEndExp.frameNStart = frameN;  // exact frame index
      
      textEndExp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textEndExp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textEndExp.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    expEndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function expEndTextRoutineEnd() {
  return async function () {
    //------Ending Routine 'expEndText'-------
    expEndTextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
