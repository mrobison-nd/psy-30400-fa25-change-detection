/************************ 
 * Changedetection *
 ************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'ChangeDetection';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'name': '',
};

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
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
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
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(instruction1RoutineBegin());
flowScheduler.add(instruction1RoutineEachFrame());
flowScheduler.add(instruction1RoutineEnd());
flowScheduler.add(start_practiceRoutineBegin());
flowScheduler.add(start_practiceRoutineEachFrame());
flowScheduler.add(start_practiceRoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin(practice_trialsLoopScheduler));
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);






flowScheduler.add(end_practiceRoutineBegin());
flowScheduler.add(end_practiceRoutineEachFrame());
flowScheduler.add(end_practiceRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);





flowScheduler.add(end_expRoutineBegin());
flowScheduler.add(end_expRoutineEachFrame());
flowScheduler.add(end_expRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'practice_trials.csv', 'path': 'practice_trials.csv'},
    {'name': 'trials.csv', 'path': 'trials.csv'},
    {'name': 'examples.png', 'path': 'examples.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var welcome_text;
var key_resp;
var instruction1Clock;
var instruct1_text;
var key_resp_2;
var image;
var start_practiceClock;
var welcome_text_2;
var key_resp_5;
var fixClock;
var text_2;
var encodingClock;
var item1;
var item2;
var item3;
var item4;
var item5;
var item6;
var item7;
var item8;
var delay_intervalClock;
var text;
var timer;
var testClock;
var test_indicator;
var item1_2;
var item2_2;
var item3_2;
var item4_2;
var item5_2;
var item6_2;
var item7_2;
var item8_2;
var key_resp_3;
var feedbackClock;
var fb_text;
var end_practiceClock;
var instruct1_text_2;
var key_resp_4;
var end_expClock;
var end_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Welcome!\n\nThis task is a version of the Luck & Vogel (1997) "change-detection" task.\n\nPress the spacebar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction1"
  instruction1Clock = new util.Clock();
  instruct1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct1_text',
    text: "On each trial, you will see a pattern of colored squares. There will be anywhere from 2 to 8 squares in the display.\n\nThe display will appear only briefly, followed by a short delay. Then, the display will reappear, and one of the squares will be outlined by a black circle.\n\nYour task is to indicate whether this square is the same color or a different color than its initial presentation. Press the 'F' key for same, and the 'J' key for different.\n\nBelow are example trials. Press the right arrow key to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'examples.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.6, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "start_practice"
  start_practiceClock = new util.Clock();
  welcome_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text_2',
    text: 'We will start with some practice trials.\n\nRemember: press F for same, and J for different.\n\nPress the spacebar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "encoding"
  encodingClock = new util.Clock();
  item1 = new visual.Rect ({
    win: psychoJS.window, name: 'item1', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  item2 = new visual.Rect ({
    win: psychoJS.window, name: 'item2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  item3 = new visual.Rect ({
    win: psychoJS.window, name: 'item3', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  item4 = new visual.Rect ({
    win: psychoJS.window, name: 'item4', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  item5 = new visual.Rect ({
    win: psychoJS.window, name: 'item5', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  item6 = new visual.Rect ({
    win: psychoJS.window, name: 'item6', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  item7 = new visual.Rect ({
    win: psychoJS.window, name: 'item7', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  item8 = new visual.Rect ({
    win: psychoJS.window, name: 'item8', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "delay_interval"
  delay_intervalClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from code
  timer = new util.Clock();
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  test_indicator = new visual.Polygon({
    win: psychoJS.window, name: 'test_indicator', 
    edges: 100, size:[0.1, 0.1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('grey'),
    fillColor: 'grey',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  item1_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item1_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  item2_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item2_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  item3_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item3_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  item4_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item4_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  item5_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item5_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  item6_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item6_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  item7_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item7_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  item8_2 = new visual.Rect ({
    win: psychoJS.window, name: 'item8_2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  fb_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fb_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_practice"
  end_practiceClock = new util.Clock();
  instruct1_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct1_text_2',
    text: 'That is the end of the practice trials.\n\nWe will now start the real trials.\n\nPress the right arrow key to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_exp"
  end_expClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'That is the end of the experiment.\n\nPlease wait while we save your data...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcomeMaxDurationReached;
var _key_resp_allKeys;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text);
    welcomeComponents.push(key_resp);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
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
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of welcomeComponents)
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


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instruction1MaxDurationReached;
var _key_resp_2_allKeys;
var instruction1MaxDuration;
var instruction1Components;
function instruction1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction1' ---
    t = 0;
    instruction1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instruction1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('instruction1.started', globalClock.getTime());
    instruction1MaxDuration = null
    // keep track of which components have finished
    instruction1Components = [];
    instruction1Components.push(instruct1_text);
    instruction1Components.push(key_resp_2);
    instruction1Components.push(image);
    
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction1' ---
    // get current time
    t = instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruct1_text* updates
    if (t >= 0.0 && instruct1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct1_text.tStart = t;  // (not accounting for frame time here)
      instruct1_text.frameNStart = frameN;  // exact frame index
      
      instruct1_text.setAutoDraw(true);
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
      let theseKeys = key_resp_2.getKeys({keyList: ['right'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
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
    for (const thisComponent of instruction1Components)
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


function instruction1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction1' ---
    for (const thisComponent of instruction1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var start_practiceMaxDurationReached;
var _key_resp_5_allKeys;
var start_practiceMaxDuration;
var start_practiceComponents;
function start_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_practice' ---
    t = 0;
    start_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    start_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('start_practice.started', globalClock.getTime());
    start_practiceMaxDuration = null
    // keep track of which components have finished
    start_practiceComponents = [];
    start_practiceComponents.push(welcome_text_2);
    start_practiceComponents.push(key_resp_5);
    
    for (const thisComponent of start_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function start_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_practice' ---
    // get current time
    t = start_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text_2* updates
    if (t >= 0.0 && welcome_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text_2.tStart = t;  // (not accounting for frame time here)
      welcome_text_2.frameNStart = frameN;  // exact frame index
      
      welcome_text_2.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
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
    for (const thisComponent of start_practiceComponents)
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


function start_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_practice' ---
    for (const thisComponent of start_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start_practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "start_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'practice_trials.csv',
      seed: undefined, name: 'practice_trials'
    });
    psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
    currentLoop = practice_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_trial of practice_trials) {
      snapshot = practice_trials.getSnapshot();
      practice_trialsLoopScheduler.add(importConditions(snapshot));
      practice_trialsLoopScheduler.add(fixRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(fixRoutineEachFrame());
      practice_trialsLoopScheduler.add(fixRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(encodingRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(encodingRoutineEachFrame());
      practice_trialsLoopScheduler.add(encodingRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(delay_intervalRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(delay_intervalRoutineEachFrame());
      practice_trialsLoopScheduler.add(delay_intervalRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(testRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(testRoutineEachFrame());
      practice_trialsLoopScheduler.add(testRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(feedbackRoutineEachFrame());
      practice_trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialsLoopEndIteration(practice_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEndIteration(scheduler, snapshot) {
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
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trials.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixRoutineEachFrame());
      trialsLoopScheduler.add(fixRoutineEnd(snapshot));
      trialsLoopScheduler.add(encodingRoutineBegin(snapshot));
      trialsLoopScheduler.add(encodingRoutineEachFrame());
      trialsLoopScheduler.add(encodingRoutineEnd(snapshot));
      trialsLoopScheduler.add(delay_intervalRoutineBegin(snapshot));
      trialsLoopScheduler.add(delay_intervalRoutineEachFrame());
      trialsLoopScheduler.add(delay_intervalRoutineEnd(snapshot));
      trialsLoopScheduler.add(testRoutineBegin(snapshot));
      trialsLoopScheduler.add(testRoutineEachFrame());
      trialsLoopScheduler.add(testRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
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
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixMaxDurationReached;
var fixMaxDuration;
var fixComponents;
function fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fix' ---
    t = 0;
    fixClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fixMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fix.started', globalClock.getTime());
    fixMaxDuration = null
    // keep track of which components have finished
    fixComponents = [];
    fixComponents.push(text_2);
    
    for (const thisComponent of fixComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fix' ---
    // get current time
    t = fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from code_4
    if ((t > 1)) {
        continueRoutine = false;
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
    for (const thisComponent of fixComponents)
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


function fixRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fix' ---
    for (const thisComponent of fixComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fix.stopped', globalClock.getTime());
    // the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var encodingMaxDurationReached;
var encodingMaxDuration;
var encodingComponents;
function encodingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'encoding' ---
    t = 0;
    encodingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    encodingMaxDurationReached = false;
    // update component parameters for each repeat
    item1.setFillColor(new util.Color(color1));
    item1.setPos(loc1);
    item1.setLineColor(new util.Color(color1));
    item2.setFillColor(new util.Color(color2));
    item2.setPos(loc2);
    item2.setLineColor(new util.Color(color2));
    item3.setFillColor(new util.Color(color3));
    item3.setPos(loc3);
    item3.setLineColor(new util.Color(color3));
    item4.setFillColor(new util.Color(color4));
    item4.setPos(loc4);
    item4.setLineColor(new util.Color(color4));
    item5.setFillColor(new util.Color(color5));
    item5.setPos(loc5);
    item5.setLineColor(new util.Color(color5));
    item6.setFillColor(new util.Color(color6));
    item6.setPos(loc6);
    item6.setLineColor(new util.Color(color6));
    item7.setFillColor(new util.Color(color7));
    item7.setPos(loc7);
    item7.setLineColor(new util.Color(color7));
    item8.setFillColor(new util.Color(color8));
    item8.setPos(loc8);
    item8.setLineColor(new util.Color(color8));
    psychoJS.experiment.addData('encoding.started', globalClock.getTime());
    encodingMaxDuration = null
    // keep track of which components have finished
    encodingComponents = [];
    encodingComponents.push(item1);
    encodingComponents.push(item2);
    encodingComponents.push(item3);
    encodingComponents.push(item4);
    encodingComponents.push(item5);
    encodingComponents.push(item6);
    encodingComponents.push(item7);
    encodingComponents.push(item8);
    
    for (const thisComponent of encodingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function encodingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'encoding' ---
    // get current time
    t = encodingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *item1* updates
    if (t >= 0 && item1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item1.tStart = t;  // (not accounting for frame time here)
      item1.frameNStart = frameN;  // exact frame index
      
      item1.setAutoDraw(true);
    }
    
    
    // *item2* updates
    if (t >= 0 && item2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item2.tStart = t;  // (not accounting for frame time here)
      item2.frameNStart = frameN;  // exact frame index
      
      item2.setAutoDraw(true);
    }
    
    
    // *item3* updates
    if (t >= 0 && item3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item3.tStart = t;  // (not accounting for frame time here)
      item3.frameNStart = frameN;  // exact frame index
      
      item3.setAutoDraw(true);
    }
    
    
    // *item4* updates
    if (t >= 0 && item4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item4.tStart = t;  // (not accounting for frame time here)
      item4.frameNStart = frameN;  // exact frame index
      
      item4.setAutoDraw(true);
    }
    
    
    // *item5* updates
    if (t >= 0 && item5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item5.tStart = t;  // (not accounting for frame time here)
      item5.frameNStart = frameN;  // exact frame index
      
      item5.setAutoDraw(true);
    }
    
    
    // *item6* updates
    if (t >= 0 && item6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item6.tStart = t;  // (not accounting for frame time here)
      item6.frameNStart = frameN;  // exact frame index
      
      item6.setAutoDraw(true);
    }
    
    
    // *item7* updates
    if (t >= 0 && item7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item7.tStart = t;  // (not accounting for frame time here)
      item7.frameNStart = frameN;  // exact frame index
      
      item7.setAutoDraw(true);
    }
    
    
    // *item8* updates
    if (t >= 0 && item8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item8.tStart = t;  // (not accounting for frame time here)
      item8.frameNStart = frameN;  // exact frame index
      
      item8.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from code_5
    if ((t > 0.25)) {
        continueRoutine = false;
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
    for (const thisComponent of encodingComponents)
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


function encodingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'encoding' ---
    for (const thisComponent of encodingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('encoding.stopped', globalClock.getTime());
    // the Routine "encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var delay_intervalMaxDurationReached;
var startTime;
var delay_intervalMaxDuration;
var delay_intervalComponents;
function delay_intervalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'delay_interval' ---
    t = 0;
    delay_intervalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    delay_intervalMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    startTime = timer.getTime();
    
    psychoJS.experiment.addData('delay_interval.started', globalClock.getTime());
    delay_intervalMaxDuration = null
    // keep track of which components have finished
    delay_intervalComponents = [];
    delay_intervalComponents.push(text);
    
    for (const thisComponent of delay_intervalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var currTime;
function delay_intervalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'delay_interval' ---
    // get current time
    t = delay_intervalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from code
    currTime = timer.getTime();
    if (((currTime - startTime) < 1)) {
        continueRoutine = true;
    }
    if (((currTime - startTime) >= 1)) {
        continueRoutine = false;
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
    for (const thisComponent of delay_intervalComponents)
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


function delay_intervalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'delay_interval' ---
    for (const thisComponent of delay_intervalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('delay_interval.stopped', globalClock.getTime());
    // the Routine "delay_interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var testMaxDurationReached;
var _key_resp_3_allKeys;
var testMaxDuration;
var testComponents;
function testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test' ---
    t = 0;
    testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    testMaxDurationReached = false;
    // update component parameters for each repeat
    test_indicator.setPos(loc1);
    item1_2.setFillColor(new util.Color(testcolor));
    item1_2.setPos(loc1);
    item1_2.setLineColor(new util.Color(testcolor));
    item2_2.setFillColor(new util.Color(color2));
    item2_2.setPos(loc2);
    item2_2.setLineColor(new util.Color(color2));
    item3_2.setFillColor(new util.Color(color3));
    item3_2.setPos(loc3);
    item3_2.setLineColor(new util.Color(color3));
    item4_2.setFillColor(new util.Color(color4));
    item4_2.setPos(loc4);
    item4_2.setLineColor(new util.Color(color4));
    item5_2.setFillColor(new util.Color(color5));
    item5_2.setPos(loc5);
    item5_2.setLineColor(new util.Color(color5));
    item6_2.setFillColor(new util.Color(color6));
    item6_2.setPos(loc6);
    item6_2.setLineColor(new util.Color(color6));
    item7_2.setFillColor(new util.Color(color7));
    item7_2.setPos(loc7);
    item7_2.setLineColor(new util.Color(color7));
    item8_2.setFillColor(new util.Color(color8));
    item8_2.setPos(loc8);
    item8_2.setLineColor(new util.Color(color8));
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('test.started', globalClock.getTime());
    testMaxDuration = null
    // keep track of which components have finished
    testComponents = [];
    testComponents.push(test_indicator);
    testComponents.push(item1_2);
    testComponents.push(item2_2);
    testComponents.push(item3_2);
    testComponents.push(item4_2);
    testComponents.push(item5_2);
    testComponents.push(item6_2);
    testComponents.push(item7_2);
    testComponents.push(item8_2);
    testComponents.push(key_resp_3);
    
    for (const thisComponent of testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test' ---
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *test_indicator* updates
    if (t >= 0.0 && test_indicator.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_indicator.tStart = t;  // (not accounting for frame time here)
      test_indicator.frameNStart = frameN;  // exact frame index
      
      test_indicator.setAutoDraw(true);
    }
    
    
    // *item1_2* updates
    if (t >= 0 && item1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item1_2.tStart = t;  // (not accounting for frame time here)
      item1_2.frameNStart = frameN;  // exact frame index
      
      item1_2.setAutoDraw(true);
    }
    
    
    // *item2_2* updates
    if (t >= 0 && item2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item2_2.tStart = t;  // (not accounting for frame time here)
      item2_2.frameNStart = frameN;  // exact frame index
      
      item2_2.setAutoDraw(true);
    }
    
    
    // *item3_2* updates
    if (t >= 0 && item3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item3_2.tStart = t;  // (not accounting for frame time here)
      item3_2.frameNStart = frameN;  // exact frame index
      
      item3_2.setAutoDraw(true);
    }
    
    
    // *item4_2* updates
    if (t >= 0 && item4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item4_2.tStart = t;  // (not accounting for frame time here)
      item4_2.frameNStart = frameN;  // exact frame index
      
      item4_2.setAutoDraw(true);
    }
    
    
    // *item5_2* updates
    if (t >= 0 && item5_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item5_2.tStart = t;  // (not accounting for frame time here)
      item5_2.frameNStart = frameN;  // exact frame index
      
      item5_2.setAutoDraw(true);
    }
    
    
    // *item6_2* updates
    if (t >= 0 && item6_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item6_2.tStart = t;  // (not accounting for frame time here)
      item6_2.frameNStart = frameN;  // exact frame index
      
      item6_2.setAutoDraw(true);
    }
    
    
    // *item7_2* updates
    if (t >= 0 && item7_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item7_2.tStart = t;  // (not accounting for frame time here)
      item7_2.frameNStart = frameN;  // exact frame index
      
      item7_2.setAutoDraw(true);
    }
    
    
    // *item8_2* updates
    if (t >= 0 && item8_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item8_2.tStart = t;  // (not accounting for frame time here)
      item8_2.frameNStart = frameN;  // exact frame index
      
      item8_2.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_3.keys == correct) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
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
    for (const thisComponent of testComponents)
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


function testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test' ---
    for (const thisComponent of testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackMaxDurationReached;
var feedback_text;
var feedback_color;
var feedbackMaxDuration;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    if ((key_resp_3.corr === 1)) {
        feedback_text = "correct";
        feedback_color = "cyan";
    }
    if ((key_resp_3.corr === 0)) {
        feedback_text = "incorrect";
        feedback_color = "darkred";
    }
    
    fb_text.setColor(new util.Color(feedback_color));
    fb_text.setText(feedback_text);
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    feedbackMaxDuration = null
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(fb_text);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fb_text* updates
    if (t >= 0.0 && fb_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fb_text.tStart = t;  // (not accounting for frame time here)
      fb_text.frameNStart = frameN;  // exact frame index
      
      fb_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fb_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fb_text.setAutoDraw(false);
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
    for (const thisComponent of feedbackComponents)
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


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    if (feedbackMaxDurationReached) {
        routineTimer.add(feedbackMaxDuration);
    } else {
        routineTimer.add(-1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_practiceMaxDurationReached;
var _key_resp_4_allKeys;
var end_practiceMaxDuration;
var end_practiceComponents;
function end_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_practice' ---
    t = 0;
    end_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    end_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('end_practice.started', globalClock.getTime());
    end_practiceMaxDuration = null
    // keep track of which components have finished
    end_practiceComponents = [];
    end_practiceComponents.push(instruct1_text_2);
    end_practiceComponents.push(key_resp_4);
    
    for (const thisComponent of end_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_practice' ---
    // get current time
    t = end_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruct1_text_2* updates
    if (t >= 0.0 && instruct1_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct1_text_2.tStart = t;  // (not accounting for frame time here)
      instruct1_text_2.frameNStart = frameN;  // exact frame index
      
      instruct1_text_2.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['right'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
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
    for (const thisComponent of end_practiceComponents)
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


function end_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_practice' ---
    for (const thisComponent of end_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "end_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_expMaxDurationReached;
var end_expMaxDuration;
var end_expComponents;
function end_expRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_exp' ---
    t = 0;
    end_expClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    end_expMaxDurationReached = false;
    // update component parameters for each repeat
    // Disable downloading results to browser
    psychoJS._saveResults = 0; 
    
    // Generate filename for results
    let filename = psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
    
    // Extract data object from experiment
    let dataObj = psychoJS._experiment._trialsData;
    
    // Convert data object to CSV
    let data = [Object.keys(dataObj[0])].concat(dataObj).map(it => {
        return Object.values(it).toString()
    }).join('\n')
    
    // Send data to OSF via DataPipe
    console.log('Saving data...');
    fetch('https://pipe.jspsych.org/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Accept: '*/*',
        },
        body: JSON.stringify({
            experimentID: 'W1HIqKoOUEoW', // ⭑ UPDATE WITH YOUR DATAPIPE EXPERIMENT ID ⭑
            filename: filename,
            data: data,
        }),
    }).then(response => response.json()).then(data => {
        // Log response and force experiment end
        console.log(data);
        quitPsychoJS();
    })
    psychoJS.experiment.addData('end_exp.started', globalClock.getTime());
    end_expMaxDuration = null
    // keep track of which components have finished
    end_expComponents = [];
    end_expComponents.push(end_text);
    
    for (const thisComponent of end_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_expRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_exp' ---
    // get current time
    t = end_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
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
    for (const thisComponent of end_expComponents)
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


function end_expRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_exp' ---
    for (const thisComponent of end_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_exp.stopped', globalClock.getTime());
    // the Routine "end_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
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
