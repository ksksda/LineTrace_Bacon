const int motorL_pwm = 3;
const int motorL_fb = 4;
const int motorL_brake = 2;
const int motorR_pwm = 5;
const int motorR_fb = 7;
const int motorR_brake = 8;
const int sensorL = 0;
const int sensorCL = 1;
const int sensorCR = 2;
const int sensorR = 3;
const int psdL = 4;
const int psdR = 5;
float m[2]={1.0,1.0};
char c = -1;
String s = "";

void setup() {
  pinMode(motorL_pwm, OUTPUT);
  pinMode(motorL_fb, OUTPUT);
  pinMode(motorL_brake, OUTPUT);
  pinMode(motorR_pwm, OUTPUT);
  pinMode(motorR_fb, OUTPUT);
  pinMode(motorR_brake, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(true){
  //if(Serial.available() > 0){
    
    c = -1;
    s = "";
    while(c==-1){
      c = Serial.read();
      delay(5); 
    }
    while(c!='e'){
      if(c!=-1)s.concat(String(c));
      c = Serial.read();
    }
    
    for(int i=0;i<2;i++){
      m[i] = split_next().toFloat();
    }
    
    analogWrite(motorL_pwm, int(m[0]*100));
    digitalWrite(motorL_fb, int(m[0]>=0));
    digitalWrite(motorL_brake, int(m[0]==0));
    analogWrite(motorR_pwm, int(m[1]*100));
    digitalWrite(motorR_fb, int(m[1]>=0));
    digitalWrite(motorR_brake, int(m[1]==0));
    
    s = "";
    s.concat(analogRead(sensorL));
    s.concat(" ");
    s.concat(analogRead(sensorCL));
    s.concat(" ");
    s.concat(analogRead(sensorCR));
    s.concat(" ");
    s.concat(analogRead(sensorR));
    s.concat(" ");
    s.concat(analogRead(psdL));
    s.concat(" ");
    s.concat(analogRead(psdR));
    s.concat("\n");
    Serial.print(s);
  }
}
String split_next(){
  int i = s.indexOf(" ");
  String ret = s.substring(0,i);
  s = s.substring(i + 1, s.length());
  return ret;
}
