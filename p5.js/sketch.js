function setup() {
  createCanvas(400, 400, WEBGL);
}


function draw() {
  background(200,10);
  my_arc = frameCount *0.1;
  translate(frameCount*0.01, 0, 0);
  normalMaterial();
  push();
  rotateZ(frameCount * 0.01);
  rotateX(my_arc);
  rotateY(frameCount * 0.01);
  box(7, my_arc, 70);
  pop();
}
