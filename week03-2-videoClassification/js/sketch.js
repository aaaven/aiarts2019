// Aven Le Zhou https://www.aven.cc
// IMA, NYU Shanghai
// Artificial Intelligence Arts Fall 2019 https://wp.nyu.edu/shanghai-ima-aiarts/

let classifier;
let video;

let name = "";
let probability = 0;


function setup() {
  createCanvas(640, 480);

  video = createCapture(VIDEO);
  classifier = ml5.imageClassifier('MobileNet', video, modelReady);
}


function draw() {
  background(0);
  fill(255);
  textSize(20);
  text(name , width/2, height/2);
  text(probability, width/2, height/2 + 30);
}


function modelReady() {
  console.log("Model Loaded");
  classifyVideo();
}


function classifyVideo() {
  classifier.predict(gotResult);
}


function gotResult(err, results) {
  name = results[0].className;
  probability = nf(results[0].probability, 0, 2);
  classifyVideo();
}
