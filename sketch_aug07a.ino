const int MotorA = 5;
const int MotorB = 7;
const int MotorC = 9;
const int MotorD = 11;
const int sensorL = 2;
const int sensorC = 3;
const int sensorR = 4;
const int PSD = 0;
float m[2];
char c = -1;
String s = "";

void setup() {
  pinMode(MotorA, OUTPUT);
  pinMode(MotorB, OUTPUT);
  pinMode(MotorC, OUTPUT);
  pinMode(MotorD, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0){
    c = -1;
    while(c==-1){
      c = Serial.read();
      delay(5); 
    }
    while(c!='e'){
      s.concat(String(c));
      c = Serial.read();
    }
    
    for(int i=0;i<2;i++)
      m[i] = split_next().toFloat();
    
    analogWrite(m[0] > 0 ? MotorA : MotorB, int(m[0]*100));
    analogWrite(m[1] > 0 ? MotorC : MotorD, int(m[1]*100));
    
    s = "";
    s.concat(digitalRead(sensorL));
    s.concat(" ");
    s.concat(digitalRead(sensorC));
    s.concat(" ");
    s.concat(digitalRead(sensorR));
    s.concat(" ");
    s.concat(analogRead(PSD));
    Serial.print(s);
  }
}
String split_next(){
  int i = s.indexOf(" ");
  String ret = s.substring(0,i);
  s = s.substring(i + 1, s.length());
  return ret;
}
