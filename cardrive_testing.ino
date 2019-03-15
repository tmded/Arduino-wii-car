#define ENB 5
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
#define ENA 6

unsigned char ENB_speed = 230;
unsigned char ENA_speed = 230;
unsigned char carSpeed = 255;
char getstr;

void forward(int CarLeftSpeed,int CarRightSpeed){
    analogWrite(ENA, CarRightSpeed);
    analogWrite(ENB, CarLeftSpeed);
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void back(int CarLeftSpeed,int CarRightSpeed){
    analogWrite(ENA, CarRightSpeed);
    analogWrite(ENB, CarLeftSpeed);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
}

void left(){
    analogWrite(ENA, carSpeed);
    analogWrite(ENB, carSpeed);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void right(){
    analogWrite(ENA, carSpeed);
    analogWrite(ENB, carSpeed);
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
}

void stop(){
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
}

void setup() {
    Serial.begin(9600);
    
    pinMode(IN1,OUTPUT);
    pinMode(IN2,OUTPUT);
    pinMode(IN3,OUTPUT);
    pinMode(IN4,OUTPUT);
    pinMode(ENA,OUTPUT);
    pinMode(ENB,OUTPUT);
    stop();
}

void loop() {
    getstr = Serial.read();
      switch(getstr){
      case 'f': forward(ENA_speed,ENB_speed);  break;
      case 'b': back(ENA_speed,ENB_speed);     break;
      case 'm': Serial.end();Serial.begin(9600); while (!Serial.available()){}; ENA_speed = Serial.parseInt();break;
      case 'n': Serial.end();Serial.begin(9600);while (!Serial.available()){};ENB_speed = Serial.parseInt();break;
      case 's': stop();     break;
      case 'l': left();     break;
      case 'r': right();    break;
      default:              break;
      };
}
