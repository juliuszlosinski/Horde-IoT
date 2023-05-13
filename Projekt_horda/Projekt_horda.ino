#include <ESP8266WiFi.h>
#include <DHT.h>

// Pin, do którego podłączony jest czujnik DHT11
const int dhtPin = D4; // D4 na większości płytek ESP8266 to GPIO2

// Inicjalizacja instancji DHT
#define DHTTYPE DHT11
DHT dht(dhtPin, DHTTYPE);

void setup() {
  // Rozpoczęcie komunikacji szeregowej
  Serial.begin(115200);
  Serial.println("Uruchomienie czujnika DHT11");

  // Uruchomienie czujnika DHT11
  dht.begin();
}

void loop() {
  // Odczyt wartości temperatury i wilgotności
  float wilgotnosc = dht.readHumidity();
  float temperatura = dht.readTemperature();

  // Sprawdzenie, czy odczyty są poprawne. Funkcja isnan() sprawdza, czy podana wartość jest wartością "Not-a-Number" (NaN).
  if (isnan(wilgotnosc) || isnan(temperatura)) {
    Serial.println("Błąd odczytu z czujnika DHT11");
    return;
  }

  // Wyświetlenie wartości temperatury i wilgotności
  Serial.print("Wilgotnosc: ");
  Serial.print(wilgotnosc);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" *C");

  // Czekaj 2 sekundy przed następnym odczytem
  delay(2000);
}
