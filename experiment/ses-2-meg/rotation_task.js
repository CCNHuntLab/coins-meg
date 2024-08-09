/********************** 
 * Rotation_Task Test *
 **********************/

import { core, data, sound, util, visual } from './lib/psychojs-2022.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


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
const move_trainingLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(move_trainingLoopBegin(move_trainingLoopScheduler));
flowScheduler.add(move_trainingLoopScheduler);
flowScheduler.add(move_trainingLoopEnd);
flowScheduler.add(practiceMoveRoutineBegin());
flowScheduler.add(practiceMoveRoutineEachFrame());
flowScheduler.add(practiceMoveRoutineEnd());
flowScheduler.add(sizeExamplesRoutineBegin());
flowScheduler.add(sizeExamplesRoutineEachFrame());
flowScheduler.add(sizeExamplesRoutineEnd());
flowScheduler.add(sizeExamples_1RoutineBegin());
flowScheduler.add(sizeExamples_1RoutineEachFrame());
flowScheduler.add(sizeExamples_1RoutineEnd());
flowScheduler.add(practiceSizeRoutineBegin());
flowScheduler.add(practiceSizeRoutineEachFrame());
flowScheduler.add(practiceSizeRoutineEnd());
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
    {'name': 'images/earth.png', 'path': 'images/earth.png'},
    {'name': 'images/shield_small2.png', 'path': 'images/shield_small2.png'},
    {'name': 'stimgen/blocks.csv', 'path': 'stimgen/blocks.csv'},
    {'name': 'images/shield_miss2.png', 'path': 'images/shield_miss2.png'},
    {'name': 'images/shield_hit2.png', 'path': 'images/shield_hit2.png'},
    {'name': 'images/shield_large2.png', 'path': 'images/shield_large2.png'},
    {'name': 'images/shield_medium2.png', 'path': 'images/shield_medium2.png'},
    {'name': 'images/radioactive1.png', 'path': 'images/radioactive1.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.3';
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
    text: 'A mysterious radioactive substance has just landed on the surface of the Earth, and is emitting radiations harmful for us and our planet. You are tasked with protecting the Earth from these radiations, capturing as many of them as possible with an absorbing shield.\n\nBelow, you can see examples of the shield missing (left) and catching (right) the radiation.\n\n\n\n\n\n\n\n\nPress any button to advance.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  shield_miss = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_miss', units : undefined, 
    image : 'images/shield_miss2.png', mask : undefined,
    ori : 0.0, pos : [(- 0.3), (- 0.12)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  shield_hit = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_hit', units : undefined, 
    image : 'images/shield_hit2.png', mask : undefined,
    ori : 0.0, pos : [0.3, (- 0.12)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "instructed_move"
  instructed_moveClock = new util.Clock();
  kb = new keyboard.Keyboard();
  ROTATION_SPEED = 1;
  CIRCLE_RADIUS = 3;
  shieldDegrees = 45;
  shieldWidth = ((np.sin(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldHeight = ((np.cos(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldX = ((np.sin(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldY = ((np.cos(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldX = np.concatenate([[0], shieldX]);
  shieldY = np.concatenate([[0], shieldY]);
  shieldCoords = np.transpose(np.vstack([shieldX, shieldY]));
  shieldRotation = 0;
  saveData = [["blockID", "currentFrame", "laserRotation", "shieldRotation", "shieldDegrees", "currentHit", "totalReward", "sendTrigger", "triggerValue"]];
  saveFilename = ((("savedData_" + expInfo["participant"].toString()) + expInfo["session"].toString()) + ".csv");
  training_loop_count = (- 1);
  target_orientation = 0;
  
  shield_move_i = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_move_i', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, (- 3)],
    lineWidth: 1.0, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  shield_centre_move_i = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_centre_move_i', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 3.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  shield_bg_short_move_i = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_bg_short_move_i', units : 'height', 
    edges: 4, size:[1, 1],
    ori: 1.0, pos: [0, (- 3)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  target_move_i = new visual.Polygon ({
    win: psychoJS.window, name: 'target_move_i', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 3.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  radioactive_move_i = new visual.ImageStim({
    win : psychoJS.window,
    name : 'radioactive_move_i', units : 'cm', 
    image : 'images/radioactive1.png', mask : undefined,
    ori : 0.0, pos : [0, (- 3)], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_move_i = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_move_i',
    text: 'You must manoeuvre the shield. The more radiations you catch, the lesser the damage to the Earth. You are preparing using a shield around a harmless replication of the radioactive body. \n\nPlease practice by moving the shield using the 1 and 2 buttons. Your goal is to reach the blue line.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  // Initialize components for Routine "practiceMove"
  practiceMoveClock = new util.Clock();
  kb = new keyboard.Keyboard();
  ROTATION_SPEED = 1;
  CIRCLE_RADIUS = 3;
  shieldDegrees = 45;
  shieldWidth = ((np.sin(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldHeight = ((np.cos(np.radians(shieldDegrees)) * CIRCLE_RADIUS) * 1.5);
  shieldX = ((np.sin(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldY = ((np.cos(np.arange(np.radians((- shieldDegrees)), np.radians(shieldDegrees), (np.radians(shieldDegrees) / 20))) * CIRCLE_RADIUS) * 1.1);
  shieldX = np.concatenate([[0], shieldX]);
  shieldY = np.concatenate([[0], shieldY]);
  shieldCoords = np.transpose(np.vstack([shieldX, shieldY]));
  shieldRotation = 0;
  saveData = [["blockID", "currentFrame", "laserRotation", "shieldRotation", "shieldDegrees", "currentHit", "totalReward", "sendTrigger", "triggerValue"]];
  saveFilename = ((("savedData_" + expInfo["participant"].toString()) + expInfo["session"].toString()) + ".csv");
  
  shield_move = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_move', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, (- 3)],
    lineWidth: 1.0, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  shield_centre_move = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_centre_move', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 3.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  shield_bg_short_move = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_bg_short_move', units : 'height', 
    edges: 4, size:[1, 1],
    ori: 1.0, pos: [0, (- 3)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  radioactive_move = new visual.ImageStim({
    win : psychoJS.window,
    name : 'radioactive_move', units : 'cm', 
    image : 'images/radioactive1.png', mask : undefined,
    ori : 0.0, pos : [0, (- 3)], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  text_move = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_move',
    text: 'You can practice as much as you wish to get familiar with the task.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_advance_move = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_advance_move',
    text: 'When you are ready to advance, press button 3.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_move = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sizeExamples"
  sizeExamplesClock = new util.Clock();
  text_size_examples = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_size_examples',
    text: 'You can also control the size of the shield, meaning you can make it bigger or smaller to catch more radiations, but you have to be careful: the larger the shield, the weaker its capturing ability. That means using a smaller shield will be more difficult for capturing radiations, but also that these will do less damage than if a bigger shield captured them. The more red the shield, the less damage the radiation is doing.\n\nBelow, you can see examples of a small (left), medium (centre), and large (right) shield.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.23], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_size_advance = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_size_advance',
    text: 'When you are ready to advance, press any button.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.34)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  shield_small = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_small', units : undefined, 
    image : 'images/shield_small2.png', mask : undefined,
    ori : 0.0, pos : [(- 0.4), (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  shield_medium = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_medium', units : undefined, 
    image : 'images/shield_medium2.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  shield_large = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_large', units : undefined, 
    image : 'images/shield_large2.png', mask : undefined,
    ori : 0.0, pos : [0.4, (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  key_resp_size_examples = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sizeExamples_1"
  sizeExamples_1Clock = new util.Clock();
  text_size_examples_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_size_examples_2',
    text: 'It is not only about catching the laser with the shield: the closer you place the centre of the shield to the laser, the less damage the latter does. The shield will let less and less radiations through, the closer the laser is to its centre, making the laser less and less visible. However, a larger shield lets more radiations through than a small one.\n\nYou can see differences in laser visibility in the examples below.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.23], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_size_advance_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_size_advance_2',
    text: 'When you are ready to advance, press any button.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.34)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  shield_small_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_small_2', units : undefined, 
    image : 'images/shield_small2.png', mask : undefined,
    ori : 0.0, pos : [(- 0.4), (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  shield_medium_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_medium_2', units : undefined, 
    image : 'images/shield_medium2.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  shield_large_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'shield_large_2', units : undefined, 
    image : 'images/shield_large2.png', mask : undefined,
    ori : 0.0, pos : [0.4, (- 0.13)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  key_resp_size_examples_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceSize"
  practiceSizeClock = new util.Clock();
  shield_size = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_size', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: shieldRotation, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  shield_centre_size = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_centre_size', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: shieldRotation, pos: [0, 0],
    lineWidth: 3.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  shield_bg_short_size = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_bg_short_size', units : 'height', 
    edges: 4, size:[1, 1],
    ori: shieldRotation, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  radio_size = new visual.ImageStim({
    win : psychoJS.window,
    name : 'radio_size', units : 'cm', 
    image : 'images/radioactive1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  text_size = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_size',
    text: 'You are preparing to capture the radiations using a shield around a harmless replication of the radioactive body. \n\nPlease practice by changing the shield size using the 3 and 4 buttons.\n\n\n\n\n\n\n\nWhen you are ready to advance, press button 1.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.12], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_resp_size = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  key_resp_blockStart = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  earth_background = new visual.ImageStim({
    win : psychoJS.window,
    name : 'earth_background', units : undefined, 
    image : 'images/earth.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  harmless_area = new visual.Polygon({
    win: psychoJS.window, name: 'harmless_area', units : 'height', 
    edges: 100, size:[6.6, 6.6],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  shield = new visual.Polygon ({
    win: psychoJS.window, name: 'shield', units : 'height', 
    edges: 4, size:[1.1, 1.1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  shield_centre = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_centre', units : 'height', 
    edges: 4, size:[1, 1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 3.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  shield_bg_short = new visual.Polygon ({
    win: psychoJS.window, name: 'shield_bg_short', units : 'height', 
    edges: 4, size:[1, 1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  laser = new visual.Polygon ({
    win: psychoJS.window, name: 'laser', units : 'height', 
    edges: 4, size:[1.0, 1.0],
    ori: 1.0, pos: [0, 0],
    lineWidth: 10.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  laser_long = new visual.Polygon ({
    win: psychoJS.window, name: 'laser_long', units : 'height', 
    edges: 4, size:[1.0, 1.0],
    ori: 1.0, pos: [0, 0],
    lineWidth: 10.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('red'),
    opacity: 1.0, depth: -7, interpolate: true,
  });
  
  radioactive = new visual.ImageStim({
    win : psychoJS.window,
    name : 'radioactive', units : 'cm', 
    image : 'images/radioactive1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  reward_bar = new visual.Rect ({
    win: psychoJS.window, name: 'reward_bar', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, pos: [0.6, (- 0.3)],
    lineWidth: 1.0, lineColor: new util.Color('blue'),
    fillColor: new util.Color('blue'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  reward_text_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'reward_text_top',
    text: top_amount,
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  reward_text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'reward_text_bottom',
    text: bottom_amount,
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -11.0 
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
  
  key_resp_blockEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
    instructionsComponents.push(shield_miss);
    instructionsComponents.push(shield_hit);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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
    
    
    // *shield_miss* updates
    if (t >= 0.0 && shield_miss.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_miss.tStart = t;  // (not accounting for frame time here)
      shield_miss.frameNStart = frameN;  // exact frame index
      
      shield_miss.setAutoDraw(true);
    }

    
    // *shield_hit* updates
    if (t >= 0.0 && shield_hit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_hit.tStart = t;  // (not accounting for frame time here)
      shield_hit.frameNStart = frameN;  // exact frame index
      
      shield_hit.setAutoDraw(true);
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
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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

function move_trainingLoopBegin(move_trainingLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    move_training = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'move_training'
    });
    psychoJS.experiment.addLoop(move_training); // add the loop to the experiment
    currentLoop = move_training;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMove_training of move_training) {
      const snapshot = move_training.getSnapshot();
      move_trainingLoopScheduler.add(importConditions(snapshot));
      move_trainingLoopScheduler.add(instructed_moveRoutineBegin(snapshot));
      move_trainingLoopScheduler.add(instructed_moveRoutineEachFrame());
      move_trainingLoopScheduler.add(instructed_moveRoutineEnd());
      move_trainingLoopScheduler.add(endLoopIteration(move_trainingLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function move_trainingLoopEnd() {
  psychoJS.experiment.removeLoop(move_training);

  return Scheduler.Event.NEXT;
}

function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimgen/blocks.csv',
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock of blocks) {
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
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}

function instructed_moveRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructed_move'-------
    t = 0;
    instructed_moveClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    training_loop_count = (training_loop_count + 1);
    console.log(training_loop_count);
    target_orientations = [163, 356, 271];
    target_orientation = target_orientations[training_loop_count];
    
    target_move_i.setOri(target_orientation);
    // keep track of which components have finished
    instructed_moveComponents = [];
    instructed_moveComponents.push(shield_move_i);
    instructed_moveComponents.push(shield_centre_move_i);
    instructed_moveComponents.push(shield_bg_short_move_i);
    instructed_moveComponents.push(target_move_i);
    instructed_moveComponents.push(radioactive_move_i);
    instructed_moveComponents.push(text_move_i);
    
    for (const thisComponent of instructed_moveComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructed_moveRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructed_move'-------
    // get current time
    t = instructed_moveClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    LRkeys_released = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": true});
    if ((LRkeys_released.length > 0)) {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": false});
    } else {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": false, "waitRelease": false});
    }
    if ((LRkeys_pressed.length > 0)) {
        if ((LRkeys_pressed.slice((- 1))[0] === "1")) {
            shieldRotation += ROTATION_SPEED;
        }
        if ((LRkeys_pressed.slice((- 1))[0] === "2")) {
            shieldRotation -= ROTATION_SPEED;
        }
    }
    if (((shieldRotation % 360) === (target_orientation % 360))) {
        continueRoutine = false;
    }
    
    
    // *shield_move_i* updates
    if (t >= 0 && shield_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_move_i.tStart = t;  // (not accounting for frame time here)
      shield_move_i.frameNStart = frameN;  // exact frame index
      
      shield_move_i.setAutoDraw(true);
    }

    
    if (shield_move_i.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_move_i.setOri(shieldRotation, false);
    }
    
    // *shield_centre_move_i* updates
    if (t >= 0 && shield_centre_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_centre_move_i.tStart = t;  // (not accounting for frame time here)
      shield_centre_move_i.frameNStart = frameN;  // exact frame index
      
      shield_centre_move_i.setAutoDraw(true);
    }

    
    if (shield_centre_move_i.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_centre_move_i.setPos([0, (- 3)], false);
      shield_centre_move_i.setOri(shieldRotation, false);
    }
    
    // *shield_bg_short_move_i* updates
    if (t >= 0 && shield_bg_short_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_bg_short_move_i.tStart = t;  // (not accounting for frame time here)
      shield_bg_short_move_i.frameNStart = frameN;  // exact frame index
      
      shield_bg_short_move_i.setAutoDraw(true);
    }

    
    if (shield_bg_short_move_i.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_bg_short_move_i.setFillColor(new util.Color([0, 0, 0]), false);
      shield_bg_short_move_i.setOri(shieldRotation, false);
      shield_bg_short_move_i.setVertices(shieldCoords, false);
      shield_bg_short_move_i.setLineColor(new util.Color([0, 0, 0]), false);
    }
    
    // *target_move_i* updates
    if (t >= 0 && target_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_move_i.tStart = t;  // (not accounting for frame time here)
      target_move_i.frameNStart = frameN;  // exact frame index
      
      target_move_i.setAutoDraw(true);
    }

    
    if (target_move_i.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target_move_i.setPos([0, (- 3)], false);
    }
    
    // *radioactive_move_i* updates
    if (t >= 0 && radioactive_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      radioactive_move_i.tStart = t;  // (not accounting for frame time here)
      radioactive_move_i.frameNStart = frameN;  // exact frame index
      
      radioactive_move_i.setAutoDraw(true);
    }

    
    // *text_move_i* updates
    if (t >= 0.0 && text_move_i.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_move_i.tStart = t;  // (not accounting for frame time here)
      text_move_i.frameNStart = frameN;  // exact frame index
      
      text_move_i.setAutoDraw(true);
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
    for (const thisComponent of instructed_moveComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructed_moveRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructed_move'-------
    for (const thisComponent of instructed_moveComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instructed_move" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceMoveRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practiceMove'-------
    t = 0;
    practiceMoveClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_move.keys = undefined;
    key_resp_move.rt = undefined;
    _key_resp_move_allKeys = [];
    // keep track of which components have finished
    practiceMoveComponents = [];
    practiceMoveComponents.push(shield_move);
    practiceMoveComponents.push(shield_centre_move);
    practiceMoveComponents.push(shield_bg_short_move);
    practiceMoveComponents.push(radioactive_move);
    practiceMoveComponents.push(text_move);
    practiceMoveComponents.push(text_advance_move);
    practiceMoveComponents.push(key_resp_move);
    
    for (const thisComponent of practiceMoveComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practiceMoveRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practiceMove'-------
    // get current time
    t = practiceMoveClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    LRkeys_released = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": true});
    if ((LRkeys_released.length > 0)) {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": false});
    } else {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": false, "waitRelease": false});
    }
    if ((LRkeys_pressed.length > 0)) {
        if ((LRkeys_pressed.slice((- 1))[0] === "1")) {
            shieldRotation += ROTATION_SPEED;
        }
        if ((LRkeys_pressed.slice((- 1))[0] === "2")) {
            shieldRotation -= ROTATION_SPEED;
        }
    }
    
    
    // *shield_move* updates
    if (t >= 0 && shield_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_move.tStart = t;  // (not accounting for frame time here)
      shield_move.frameNStart = frameN;  // exact frame index
      
      shield_move.setAutoDraw(true);
    }

    
    if (shield_move.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_move.setOri(shieldRotation, false);
    }
    
    // *shield_centre_move* updates
    if (t >= 0 && shield_centre_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_centre_move.tStart = t;  // (not accounting for frame time here)
      shield_centre_move.frameNStart = frameN;  // exact frame index
      
      shield_centre_move.setAutoDraw(true);
    }

    
    if (shield_centre_move.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_centre_move.setPos([0, (- 3)], false);
      shield_centre_move.setOri(shieldRotation, false);
    }
    
    // *shield_bg_short_move* updates
    if (t >= 0 && shield_bg_short_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_bg_short_move.tStart = t;  // (not accounting for frame time here)
      shield_bg_short_move.frameNStart = frameN;  // exact frame index
      
      shield_bg_short_move.setAutoDraw(true);
    }

    
    if (shield_bg_short_move.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_bg_short_move.setFillColor(new util.Color([0, 0, 0]), false);
      shield_bg_short_move.setOri(shieldRotation, false);
      shield_bg_short_move.setVertices(shieldCoords, false);
      shield_bg_short_move.setLineColor(new util.Color([0, 0, 0]), false);
    }
    
    // *radioactive_move* updates
    if (t >= 0 && radioactive_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      radioactive_move.tStart = t;  // (not accounting for frame time here)
      radioactive_move.frameNStart = frameN;  // exact frame index
      
      radioactive_move.setAutoDraw(true);
    }

    
    // *text_move* updates
    if (t >= 0.0 && text_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_move.tStart = t;  // (not accounting for frame time here)
      text_move.frameNStart = frameN;  // exact frame index
      
      text_move.setAutoDraw(true);
    }

    
    // *text_advance_move* updates
    if (t >= 0.0 && text_advance_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_advance_move.tStart = t;  // (not accounting for frame time here)
      text_advance_move.frameNStart = frameN;  // exact frame index
      
      text_advance_move.setAutoDraw(true);
    }

    
    // *key_resp_move* updates
    if (t >= 0.0 && key_resp_move.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_move.tStart = t;  // (not accounting for frame time here)
      key_resp_move.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_move.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_move.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_move.clearEvents(); });
    }

    if (key_resp_move.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_move.getKeys({keyList: ['3'], waitRelease: false});
      _key_resp_move_allKeys = _key_resp_move_allKeys.concat(theseKeys);
      if (_key_resp_move_allKeys.length > 0) {
        key_resp_move.keys = _key_resp_move_allKeys[_key_resp_move_allKeys.length - 1].name;  // just the last key pressed
        key_resp_move.rt = _key_resp_move_allKeys[_key_resp_move_allKeys.length - 1].rt;
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
    for (const thisComponent of practiceMoveComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceMoveRoutineEnd() {
  return async function () {
    //------Ending Routine 'practiceMove'-------
    for (const thisComponent of practiceMoveComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_move.corr, level);
    }
    psychoJS.experiment.addData('key_resp_move.keys', key_resp_move.keys);
    if (typeof key_resp_move.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_move.rt', key_resp_move.rt);
        routineTimer.reset();
        }
    
    key_resp_move.stop();
    // the Routine "practiceMove" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sizeExamplesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'sizeExamples'-------
    t = 0;
    sizeExamplesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_size_examples.keys = undefined;
    key_resp_size_examples.rt = undefined;
    _key_resp_size_examples_allKeys = [];
    // keep track of which components have finished
    sizeExamplesComponents = [];
    sizeExamplesComponents.push(text_size_examples);
    sizeExamplesComponents.push(text_size_advance);
    sizeExamplesComponents.push(shield_small);
    sizeExamplesComponents.push(shield_medium);
    sizeExamplesComponents.push(shield_large);
    sizeExamplesComponents.push(key_resp_size_examples);
    
    for (const thisComponent of sizeExamplesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function sizeExamplesRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'sizeExamples'-------
    // get current time
    t = sizeExamplesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_size_examples* updates
    if (t >= 0.0 && text_size_examples.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_size_examples.tStart = t;  // (not accounting for frame time here)
      text_size_examples.frameNStart = frameN;  // exact frame index
      
      text_size_examples.setAutoDraw(true);
    }

    
    // *text_size_advance* updates
    if (t >= 0.0 && text_size_advance.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_size_advance.tStart = t;  // (not accounting for frame time here)
      text_size_advance.frameNStart = frameN;  // exact frame index
      
      text_size_advance.setAutoDraw(true);
    }

    
    // *shield_small* updates
    if (t >= 0.0 && shield_small.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_small.tStart = t;  // (not accounting for frame time here)
      shield_small.frameNStart = frameN;  // exact frame index
      
      shield_small.setAutoDraw(true);
    }

    
    // *shield_medium* updates
    if (t >= 0.0 && shield_medium.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_medium.tStart = t;  // (not accounting for frame time here)
      shield_medium.frameNStart = frameN;  // exact frame index
      
      shield_medium.setAutoDraw(true);
    }

    
    // *shield_large* updates
    if (t >= 0.0 && shield_large.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_large.tStart = t;  // (not accounting for frame time here)
      shield_large.frameNStart = frameN;  // exact frame index
      
      shield_large.setAutoDraw(true);
    }

    
    // *key_resp_size_examples* updates
    if (t >= 0.0 && key_resp_size_examples.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_size_examples.tStart = t;  // (not accounting for frame time here)
      key_resp_size_examples.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_size_examples.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_examples.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_examples.clearEvents(); });
    }

    if (key_resp_size_examples.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_size_examples.getKeys({keyList: [], waitRelease: false});
      _key_resp_size_examples_allKeys = _key_resp_size_examples_allKeys.concat(theseKeys);
      if (_key_resp_size_examples_allKeys.length > 0) {
        key_resp_size_examples.keys = _key_resp_size_examples_allKeys[_key_resp_size_examples_allKeys.length - 1].name;  // just the last key pressed
        key_resp_size_examples.rt = _key_resp_size_examples_allKeys[_key_resp_size_examples_allKeys.length - 1].rt;
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
    for (const thisComponent of sizeExamplesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sizeExamplesRoutineEnd() {
  return async function () {
    //------Ending Routine 'sizeExamples'-------
    for (const thisComponent of sizeExamplesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_size_examples.corr, level);
    }
    psychoJS.experiment.addData('key_resp_size_examples.keys', key_resp_size_examples.keys);
    if (typeof key_resp_size_examples.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_size_examples.rt', key_resp_size_examples.rt);
        routineTimer.reset();
        }
    
    key_resp_size_examples.stop();
    // the Routine "sizeExamples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sizeExamples_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'sizeExamples_1'-------
    t = 0;
    sizeExamples_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_size_examples_2.keys = undefined;
    key_resp_size_examples_2.rt = undefined;
    _key_resp_size_examples_2_allKeys = [];
    // keep track of which components have finished
    sizeExamples_1Components = [];
    sizeExamples_1Components.push(text_size_examples_2);
    sizeExamples_1Components.push(text_size_advance_2);
    sizeExamples_1Components.push(shield_small_2);
    sizeExamples_1Components.push(shield_medium_2);
    sizeExamples_1Components.push(shield_large_2);
    sizeExamples_1Components.push(key_resp_size_examples_2);
    
    for (const thisComponent of sizeExamples_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function sizeExamples_1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'sizeExamples_1'-------
    // get current time
    t = sizeExamples_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_size_examples_2* updates
    if (t >= 0.0 && text_size_examples_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_size_examples_2.tStart = t;  // (not accounting for frame time here)
      text_size_examples_2.frameNStart = frameN;  // exact frame index
      
      text_size_examples_2.setAutoDraw(true);
    }

    
    // *text_size_advance_2* updates
    if (t >= 0.0 && text_size_advance_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_size_advance_2.tStart = t;  // (not accounting for frame time here)
      text_size_advance_2.frameNStart = frameN;  // exact frame index
      
      text_size_advance_2.setAutoDraw(true);
    }

    
    // *shield_small_2* updates
    if (t >= 0.0 && shield_small_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_small_2.tStart = t;  // (not accounting for frame time here)
      shield_small_2.frameNStart = frameN;  // exact frame index
      
      shield_small_2.setAutoDraw(true);
    }

    
    // *shield_medium_2* updates
    if (t >= 0.0 && shield_medium_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_medium_2.tStart = t;  // (not accounting for frame time here)
      shield_medium_2.frameNStart = frameN;  // exact frame index
      
      shield_medium_2.setAutoDraw(true);
    }

    
    // *shield_large_2* updates
    if (t >= 0.0 && shield_large_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_large_2.tStart = t;  // (not accounting for frame time here)
      shield_large_2.frameNStart = frameN;  // exact frame index
      
      shield_large_2.setAutoDraw(true);
    }

    
    // *key_resp_size_examples_2* updates
    if (t >= 0.0 && key_resp_size_examples_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_size_examples_2.tStart = t;  // (not accounting for frame time here)
      key_resp_size_examples_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_size_examples_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_examples_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_examples_2.clearEvents(); });
    }

    if (key_resp_size_examples_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_size_examples_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_size_examples_2_allKeys = _key_resp_size_examples_2_allKeys.concat(theseKeys);
      if (_key_resp_size_examples_2_allKeys.length > 0) {
        key_resp_size_examples_2.keys = _key_resp_size_examples_2_allKeys[_key_resp_size_examples_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_size_examples_2.rt = _key_resp_size_examples_2_allKeys[_key_resp_size_examples_2_allKeys.length - 1].rt;
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
    for (const thisComponent of sizeExamples_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sizeExamples_1RoutineEnd() {
  return async function () {
    //------Ending Routine 'sizeExamples_1'-------
    for (const thisComponent of sizeExamples_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_size_examples_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_size_examples_2.keys', key_resp_size_examples_2.keys);
    if (typeof key_resp_size_examples_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_size_examples_2.rt', key_resp_size_examples_2.rt);
        routineTimer.reset();
        }
    
    key_resp_size_examples_2.stop();
    // the Routine "sizeExamples_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceSizeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practiceSize'-------
    t = 0;
    practiceSizeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    kb = new keyboard.Keyboard();
    SHIELD_GROWTH_SPEED = 20;
    minShieldDegrees = 25;
    maxShieldDegrees = 65;
    
    key_resp_size.keys = undefined;
    key_resp_size.rt = undefined;
    _key_resp_size_allKeys = [];
    // keep track of which components have finished
    practiceSizeComponents = [];
    practiceSizeComponents.push(shield_size);
    practiceSizeComponents.push(shield_centre_size);
    practiceSizeComponents.push(shield_bg_short_size);
    practiceSizeComponents.push(radio_size);
    practiceSizeComponents.push(text_size);
    practiceSizeComponents.push(key_resp_size);
    
    for (const thisComponent of practiceSizeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practiceSizeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practiceSize'-------
    // get current time
    t = practiceSizeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    UDkeys_pressed = kb.getKeys({"keyList": ["3", "4"], "clear": true, "waitRelease": false});
    if ((UDkeys_pressed.length > 0)) {
        if ((UDkeys_pressed.slice((- 1))[0] === "3")) {
            shieldDegrees += SHIELD_GROWTH_SPEED;
        }
        if ((UDkeys_pressed.slice((- 1))[0] === "4")) {
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
    
    
    // *shield_size* updates
    if (t >= 0 && shield_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_size.tStart = t;  // (not accounting for frame time here)
      shield_size.frameNStart = frameN;  // exact frame index
      
      shield_size.setAutoDraw(true);
    }

    
    if (shield_size.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_size.setVertices(shieldCoords, false);
    }
    
    // *shield_centre_size* updates
    if (t >= 0 && shield_centre_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_centre_size.tStart = t;  // (not accounting for frame time here)
      shield_centre_size.frameNStart = frameN;  // exact frame index
      
      shield_centre_size.setAutoDraw(true);
    }

    
    // *shield_bg_short_size* updates
    if (t >= 0 && shield_bg_short_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_bg_short_size.tStart = t;  // (not accounting for frame time here)
      shield_bg_short_size.frameNStart = frameN;  // exact frame index
      
      shield_bg_short_size.setAutoDraw(true);
    }

    
    if (shield_bg_short_size.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_bg_short_size.setFillColor(new util.Color([0, 0, 0]), false);
      shield_bg_short_size.setVertices(shieldCoords, false);
      shield_bg_short_size.setLineColor(new util.Color([0, 0, 0]), false);
    }
    
    // *radio_size* updates
    if (t >= 0 && radio_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      radio_size.tStart = t;  // (not accounting for frame time here)
      radio_size.frameNStart = frameN;  // exact frame index
      
      radio_size.setAutoDraw(true);
    }

    
    // *text_size* updates
    if (t >= 0.0 && text_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_size.tStart = t;  // (not accounting for frame time here)
      text_size.frameNStart = frameN;  // exact frame index
      
      text_size.setAutoDraw(true);
    }

    
    // *key_resp_size* updates
    if (t >= 0.0 && key_resp_size.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_size.tStart = t;  // (not accounting for frame time here)
      key_resp_size.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_size.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size.clearEvents(); });
    }

    if (key_resp_size.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_size.getKeys({keyList: ['1'], waitRelease: false});
      _key_resp_size_allKeys = _key_resp_size_allKeys.concat(theseKeys);
      if (_key_resp_size_allKeys.length > 0) {
        key_resp_size.keys = _key_resp_size_allKeys[_key_resp_size_allKeys.length - 1].name;  // just the last key pressed
        key_resp_size.rt = _key_resp_size_allKeys[_key_resp_size_allKeys.length - 1].rt;
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
    for (const thisComponent of practiceSizeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceSizeRoutineEnd() {
  return async function () {
    //------Ending Routine 'practiceSize'-------
    for (const thisComponent of practiceSizeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_size.corr, level);
    }
    psychoJS.experiment.addData('key_resp_size.keys', key_resp_size.keys);
    if (typeof key_resp_size.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_size.rt', key_resp_size.rt);
        routineTimer.reset();
        }
    
    key_resp_size.stop();
    // the Routine "practiceSize" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
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
    key_resp_blockStart.keys = undefined;
    key_resp_blockStart.rt = undefined;
    _key_resp_blockStart_allKeys = [];
    // keep track of which components have finished
    blockStartTextComponents = [];
    blockStartTextComponents.push(text_2);
    blockStartTextComponents.push(key_resp_blockStart);
    
    for (const thisComponent of blockStartTextComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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

    
    // *key_resp_blockStart* updates
    if (t >= 0.0 && key_resp_blockStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_blockStart.tStart = t;  // (not accounting for frame time here)
      key_resp_blockStart.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_blockStart.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_blockStart.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_blockStart.clearEvents(); });
    }

    if (key_resp_blockStart.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_blockStart.getKeys({keyList: [], waitRelease: false});
      _key_resp_blockStart_allKeys = _key_resp_blockStart_allKeys.concat(theseKeys);
      if (_key_resp_blockStart_allKeys.length > 0) {
        key_resp_blockStart.keys = _key_resp_blockStart_allKeys[_key_resp_blockStart_allKeys.length - 1].name;  // just the last key pressed
        key_resp_blockStart.rt = _key_resp_blockStart_allKeys[_key_resp_blockStart_allKeys.length - 1].rt;
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
    for (const thisComponent of blockStartTextComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of blockStartTextComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_blockStart.corr, level);
    }
    psychoJS.experiment.addData('key_resp_blockStart.keys', key_resp_blockStart.keys);
    if (typeof key_resp_blockStart.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_blockStart.rt', key_resp_blockStart.rt);
        routineTimer.reset();
        }
    
    key_resp_blockStart.stop();
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
    import * as pd from 'pandas';
    import * as np from 'numpy';
    import * as math from 'math';
    import * as os from 'os';
    var SHIELD_DECAY_RATE, bar_length, bottom_amount, currentFrame, distribution_ex, e, first_hit, hit_i, kb, laserRotation, laserXcoord, laserYcoord, maxShieldDegrees, mean, minShieldDegrees, nFrames, rad_range, rootdir, scaling, sd, sendResponseTriggers, sendTrigger, shieldCoords, shieldDegrees, shieldHeight, shieldRadians, shieldRedness, shieldRotation, shieldWidth, shieldX, shieldY, square_colour, stimStreamPath, storedStream_np, top_amount, totalReward, triggerValue;
    kb = new keyboard.Keyboard();
    rootdir = os.getcwd();
    SHIELD_DECAY_RATE = 0.99;
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
    stimStreamPath = os.path.join(rootdir, "stimgen", blockFileName);
    storedStream_np = np.loadtxt(stimStreamPath, {"delimiter": ","});
    nFrames = (np.shape(storedStream_np)[0] - 1);
    currentFrame = 0;
    laserRotation = storedStream_np[[0, 1]];
    shieldRotation = 360;
    laserXcoord = (CIRCLE_RADIUS * Math.cos(deg2rad(laserRotation)));
    laserYcoord = (CIRCLE_RADIUS * Math.sin(deg2rad(laserRotation)));
    hit_i = 0;
    first_hit = 0;
    shieldRadians = np.radians(25);
    rad_range = [];
    for (var i, _pj_c = 0, _pj_a = util.range(1, ((40 * 2) + 1)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        rad_range.push(((- shieldRadians) + ((shieldRadians / 40) * (i - 1))));
    }
    e = 2.718281828459045;
    mean = 0;
    sd = (pi / 21.6);
    distribution_ex = function () {
        var _pj_a = [], _pj_b = rad_range;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var x = _pj_b[_pj_c];
            _pj_a.push(((1 / (sd * Math.pow((2 * pi), 0.5))) * Math.pow(e, ((- 0.5) * Math.pow(((x - mean) / sd), 2)))));
        }
        return _pj_a;
    }
    .call(this);
    scaling = Math.max(distribution_ex);
    triggerValue = 11;
    sendTrigger = true;
    sendResponseTriggers = true;
    square_colour = "black";
    bar_length = 0.5;
    top_amount = 10;
    bottom_amount = 9;
    
    laser.setPos([0, 0]);
    laser.setSize([1, 1]);
    laser_long.setPos([0, 0]);
    laser_long.setSize([1, 1]);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(earth_background);
    trialComponents.push(harmless_area);
    trialComponents.push(shield);
    trialComponents.push(shield_centre);
    trialComponents.push(shield_bg_short);
    trialComponents.push(laser);
    trialComponents.push(laser_long);
    trialComponents.push(radioactive);
    trialComponents.push(reward_bar);
    trialComponents.push(reward_text_top);
    trialComponents.push(reward_text_bottom);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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
    if (hit_i) {
        hit_i = 0;
    } else {
        if (first_hit) {
            laser_long.setAutoDraw(true);
        }
    }
    if ((bar_length <= 0)) {
        bar_length = 0.5;
        top_amount = (top_amount - 1);
        bottom_amount = (bottom_amount - 1);
    }
    if ((square_colour === "black")) {
        colour_id = 1;
    }
    if ((square_colour === "white")) {
        colour_id = 2;
    }
    sendTrigger = false;
    keyReleaseThisFrame = false;
    LRkeys_released = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": true});
    if ((LRkeys_released.length > 0)) {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": true, "waitRelease": false});
        triggerValue = 7;
        sendTrigger = true;
        keyReleaseThisFrame = true;
    } else {
        LRkeys_pressed = kb.getKeys({"keyList": ["1", "2"], "clear": false, "waitRelease": false});
    }
    UDkeys_pressed = kb.getKeys({"keyList": ["3", "4"], "clear": true, "waitRelease": false});
    if ((LRkeys_pressed.length > 0)) {
        if ((LRkeys_pressed.slice((- 1))[0] === "1")) {
            shieldRotation += ROTATION_SPEED;
            newTriggerValue = 3;
        }
        if ((LRkeys_pressed.slice((- 1))[0] === "2")) {
            shieldRotation -= ROTATION_SPEED;
            newTriggerValue = 4;
        }
        if (sendResponseTriggers) {
            console.log(shieldRotation);
            triggerValue = newTriggerValue;
            sendTrigger = true;
            sendResponseTriggers = false;
        }
    }
    if ((UDkeys_pressed.length > 0)) {
        if ((UDkeys_pressed.slice((- 1))[0] === "3")) {
            shieldDegrees += SHIELD_GROWTH_SPEED;
            triggerValue = 5;
        }
        if ((UDkeys_pressed.slice((- 1))[0] === "4")) {
            shieldDegrees -= SHIELD_GROWTH_SPEED;
            triggerValue = 6;
        }
        sendTrigger = true;
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
    if ((currentFrame > 1)) {
        if ((storedStream_np[[currentFrame, 1]] !== storedStream_np[[(currentFrame - 1), 1]])) {
            if ((! sendTrigger)) {
                if (currentHit) {
                    triggerValue = 1;
                } else {
                    triggerValue = 2;
                }
                if ((colour_id === 1)) {
                    square_colour = "white";
                } else {
                    if ((colour_id === 2)) {
                        square_colour = "black";
                    }
                }
                sendTrigger = true;
            }
        }
    }
    if (currentHit) {
        shieldRedness = (shieldRedness * SHIELD_DECAY_RATE);
        update = ((minShieldDegrees / 50) / shieldDegrees);
        shieldRedness = Math.min((shieldRedness + update), 2);
        shieldColour = [1, (1 - shieldRedness), (1 - shieldRedness)];
        shieldRadians = deg2rad(shieldDegrees);
        e = 2.718281828459045;
        rad_range = [];
        for (var i, _pj_c = 0, _pj_a = util.range(1, ((40 * 2) + 1)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            rad_range.push(((- shieldRadians) + ((shieldRadians / 40) * (i - 1))));
        }
        mean = 0;
        if ((shieldDegrees === 25)) {
            sd = (pi / 21.6);
        }
        if ((shieldDegrees === 45)) {
            sd = (pi / 10);
        }
        if ((shieldDegrees === 65)) {
            sd = (pi / 5.53);
        }
        distribution = function () {
        var _pj_a = [], _pj_b = rad_range;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var x = _pj_b[_pj_c];
            _pj_a.push(((- (1 / (sd * Math.pow((2 * pi), 0.5)))) * Math.pow(e, ((- 0.5) * Math.pow(((x - mean) / sd), 2)))));
        }
        return _pj_a;
    }
    .call(this);
        distribution_scaled = function () {
        var _pj_a = [], _pj_b = distribution;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var p = _pj_b[_pj_c];
            _pj_a.push((p / scaling));
        }
        return _pj_a;
    }
    .call(this);
        distribution_shifted = function () {
        var _pj_a = [], _pj_b = distribution_scaled;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var u = _pj_b[_pj_c];
            _pj_a.push(((u - Math.min(distribution_scaled)) + 0.001));
        }
        return _pj_a;
    }
    .call(this);
        shift = (1 - Math.max(distribution_shifted));
        if (((shieldRotation === 360) || (shieldRotation === 0))) {
            if (((180 < laserRotation) && (laserRotation < 360))) {
                angle_difference = deg2rad(((laserRotation % 360) - 360));
            }
            if (((0 < laserRotation) && (laserRotation < 180))) {
                angle_difference = deg2rad(((laserRotation % 360) - 0));
            }
            if (((laserRotation === 0) || (laserRotation === 360))) {
                angle_difference = deg2rad(((laserRotation % 360) - (shieldRotation % 360)));
            }
        } else {
            angle_difference = deg2rad(((laserRotation % 360) - (shieldRotation % 360)));
        }
        a_diff_distribution = ((- (1 / (sd * Math.pow((2 * pi), 0.5)))) * Math.pow(e, ((- 0.5) * Math.pow(((angle_difference - mean) / sd), 2))));
        a_diff_d_scaled = (a_diff_distribution / scaling);
        a_diff_d_shifted = ((a_diff_d_scaled - Math.min(distribution_scaled)) + 0.001);
        laser_long_opacity = Math.pow(((a_diff_d_shifted + 1) - Math.max(distribution_shifted)), 2);
        shieldColour_1 = [1, (1 - (1 - laser_long_opacity)), (1 - (1 - laser_long_opacity))];
        hit_i = 1;
        first_hit = 1;
    } else {
        shieldRedness = (shieldRedness * SHIELD_DECAY_RATE);
        shieldColour = [1, (1 - shieldRedness), (1 - shieldRedness)];
        laser_long_opacity = 1;
        laser_long.setAutoDraw(true);
        shieldColour_1 = [1, (1 - (1 - laser_long_opacity)), (1 - (1 - laser_long_opacity))];
        bar_length = (bar_length - 0.0005);
    }
    totalReward = (totalReward + (shieldRedness / 100));
    textReward = Math.round(totalReward, 1).toString();
    if (keyReleaseThisFrame) {
        sendResponseTriggers = true;
    }
    if ((currentFrame < nFrames)) {
        saveData.push([blockID, currentFrame, laserRotation, shieldRotation, shieldDegrees, currentHit, totalReward, sendTrigger, triggerValue]);
        currentFrame = (currentFrame + 1);
    } else {
        triggerValue = 99;
        sendTrigger = true;
    }
    
    
    // *earth_background* updates
    if (frameN >= 0 && earth_background.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      earth_background.tStart = t;  // (not accounting for frame time here)
      earth_background.frameNStart = frameN;  // exact frame index
      
      earth_background.setAutoDraw(true);
    }

    if (earth_background.status === PsychoJS.Status.STARTED && frameN >= (earth_background.frameNStart + nFrames)) {
      earth_background.setAutoDraw(false);
    }
    
    // *harmless_area* updates
    if (frameN >= 0 && harmless_area.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      harmless_area.tStart = t;  // (not accounting for frame time here)
      harmless_area.frameNStart = frameN;  // exact frame index
      
      harmless_area.setAutoDraw(true);
    }

    if (harmless_area.status === PsychoJS.Status.STARTED && frameN >= (harmless_area.frameNStart + nFrames)) {
      harmless_area.setAutoDraw(false);
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
      shield.setFillColor(new util.Color(shieldColour_1), false);
      shield.setOri(shieldRotation, false);
      shield.setVertices(shieldCoords, false);
      shield.setLineColor(new util.Color([0, 0, 0]), false);
    }
    
    // *shield_centre* updates
    if (frameN >= 0 && shield_centre.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_centre.tStart = t;  // (not accounting for frame time here)
      shield_centre.frameNStart = frameN;  // exact frame index
      
      shield_centre.setAutoDraw(true);
    }

    if (shield_centre.status === PsychoJS.Status.STARTED && frameN >= (shield_centre.frameNStart + nFrames)) {
      shield_centre.setAutoDraw(false);
    }
    
    if (shield_centre.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_centre.setPos([0, 0], false);
      shield_centre.setOri(shieldRotation, false);
    }
    
    // *shield_bg_short* updates
    if (frameN >= 0 && shield_bg_short.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      shield_bg_short.tStart = t;  // (not accounting for frame time here)
      shield_bg_short.frameNStart = frameN;  // exact frame index
      
      shield_bg_short.setAutoDraw(true);
    }

    if (shield_bg_short.status === PsychoJS.Status.STARTED && frameN >= (shield_bg_short.frameNStart + nFrames)) {
      shield_bg_short.setAutoDraw(false);
    }
    
    if (shield_bg_short.status === PsychoJS.Status.STARTED){ // only update if being drawn
      shield_bg_short.setFillColor(new util.Color([0, 0, 0]), false);
      shield_bg_short.setOri(shieldRotation, false);
      shield_bg_short.setVertices(shieldCoords, false);
      shield_bg_short.setLineColor(new util.Color([0, 0, 0]), false);
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
      laser.setOri(laserRotation, false);
      laser.setVertices([[0, 0], [0, (CIRCLE_RADIUS * 1.1)]], false);
    }
    
    // *laser_long* updates
    if (t >= 0.0 && laser_long.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      laser_long.tStart = t;  // (not accounting for frame time here)
      laser_long.frameNStart = frameN;  // exact frame index
      
      laser_long.setAutoDraw(true);
    }

    if (laser_long.status === PsychoJS.Status.STARTED && frameN >= (laser_long.frameNStart + nFrames)) {
      laser_long.setAutoDraw(false);
    }
    
    if (laser_long.status === PsychoJS.Status.STARTED){ // only update if being drawn
      laser_long.setOpacity(laser_long_opacity, false);
      laser_long.setOri(laserRotation, false);
      laser_long.setVertices([[0, 0], [0, (CIRCLE_RADIUS * 1.4)]], false);
    }
    
    // *radioactive* updates
    if (frameN >= 0 && radioactive.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      radioactive.tStart = t;  // (not accounting for frame time here)
      radioactive.frameNStart = frameN;  // exact frame index
      
      radioactive.setAutoDraw(true);
    }

    if (radioactive.status === PsychoJS.Status.STARTED && frameN >= (radioactive.frameNStart + nFrames)) {
      radioactive.setAutoDraw(false);
    }
    
    // *reward_bar* updates
    if (frameN >= 0 && reward_bar.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reward_bar.tStart = t;  // (not accounting for frame time here)
      reward_bar.frameNStart = frameN;  // exact frame index
      
      reward_bar.setAutoDraw(true);
    }

    if (reward_bar.status === PsychoJS.Status.STARTED && frameN >= (reward_bar.frameNStart + nFrames)) {
      reward_bar.setAutoDraw(false);
    }
    
    if (reward_bar.status === PsychoJS.Status.STARTED){ // only update if being drawn
      reward_bar.setSize([0.05, bar_length], false);
    }
    
    // *reward_text_top* updates
    if (frameN >= 0 && reward_text_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reward_text_top.tStart = t;  // (not accounting for frame time here)
      reward_text_top.frameNStart = frameN;  // exact frame index
      
      reward_text_top.setAutoDraw(true);
    }

    if (reward_text_top.status === PsychoJS.Status.STARTED && frameN >= (reward_text_top.frameNStart + nFrames)) {
      reward_text_top.setAutoDraw(false);
    }
    
    // *reward_text_bottom* updates
    if (frameN >= 0 && reward_text_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reward_text_bottom.tStart = t;  // (not accounting for frame time here)
      reward_text_bottom.frameNStart = frameN;  // exact frame index
      
      reward_text_bottom.setAutoDraw(true);
    }

    if (reward_text_bottom.status === PsychoJS.Status.STARTED && frameN >= (reward_text_bottom.frameNStart + nFrames)) {
      reward_text_bottom.setAutoDraw(false);
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
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
    key_resp_blockEnd.keys = undefined;
    key_resp_blockEnd.rt = undefined;
    _key_resp_blockEnd_allKeys = [];
    // keep track of which components have finished
    blockEndTextComponents = [];
    blockEndTextComponents.push(textPause);
    blockEndTextComponents.push(textContinue);
    blockEndTextComponents.push(key_resp_blockEnd);
    
    for (const thisComponent of blockEndTextComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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

    
    // *key_resp_blockEnd* updates
    if (t >= 5.0 && key_resp_blockEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_blockEnd.tStart = t;  // (not accounting for frame time here)
      key_resp_blockEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_blockEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_blockEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_blockEnd.clearEvents(); });
    }

    if (key_resp_blockEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_blockEnd.getKeys({keyList: [], waitRelease: false});
      _key_resp_blockEnd_allKeys = _key_resp_blockEnd_allKeys.concat(theseKeys);
      if (_key_resp_blockEnd_allKeys.length > 0) {
        key_resp_blockEnd.keys = _key_resp_blockEnd_allKeys[_key_resp_blockEnd_allKeys.length - 1].name;  // just the last key pressed
        key_resp_blockEnd.rt = _key_resp_blockEnd_allKeys[_key_resp_blockEnd_allKeys.length - 1].rt;
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
    for (const thisComponent of blockEndTextComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of blockEndTextComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_blockEnd.corr, level);
    }
    psychoJS.experiment.addData('key_resp_blockEnd.keys', key_resp_blockEnd.keys);
    if (typeof key_resp_blockEnd.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_blockEnd.rt', key_resp_blockEnd.rt);
        routineTimer.reset();
        }
    
    key_resp_blockEnd.stop();
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
    
    for (const thisComponent of expEndTextComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
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
    for (const thisComponent of expEndTextComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of expEndTextComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
