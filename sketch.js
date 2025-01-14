let currentColor = 0;
let brushSize = 2;

function setup() {
  createCanvas(900, 600);
  background(220);
}

function draw() {
  if (keyIsPressed) {
    if (key == 'r' || key == 'R') {
      currentColor = color(255, 0, 0);
    } else if (key == 'g' || key == 'G') {
      currentColor = color(0, 255, 0);
    } else if (key == 'b' || key == 'B') {
      currentColor = color(0, 0, 255);
    }
  }

    if (keyIsDown(UP_ARROW)) {
        brushSize++;
    }
    if (keyIsDown(DOWN_ARROW) && brushSize > 1) {
        brushSize--;
    }

  if (mouseIsPressed) {
    stroke(currentColor);
    strokeWeight(brushSize);
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}

function keyPressed() {
    if (key == 'c' || key == 'C') {
        background(220);
    }
}