#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int soilPin = 34;
int ldrPin = 35;
int relayPin = 25;

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  int soil = analogRead(soilPin);
  int light = analogRead(ldrPin);

  Serial.println("----- Sensor Data -----");
  Serial.print("Temperature: ");
  Serial.println(temperature);

  Serial.print("Humidity: ");
  Serial.println(humidity);

  Serial.print("Soil Moisture: ");
  Serial.println(soil);

  Serial.print("Light Intensity: ");
  Serial.println(light);

  if (soil < 1500) {
    digitalWrite(relayPin, LOW);
    Serial.println("Pump ON");
  } else {
    digitalWrite(relayPin, HIGH);
    Serial.println("Pump OFF");
  }

  delay(5000);
}