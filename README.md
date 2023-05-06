## Real-Time Monitoring System (Horde)

This project is created by using ESP32 x 4 and Intel Joule x 1.

![image](https://user-images.githubusercontent.com/72278818/233649310-02c203aa-7e83-4df7-8fe6-4082f65205db.png)

Todo:
1. Programy (4 x ESP), które mają zdefiniowane:
- IP urządzenia zdefiniowane,
- Adres IP routera (sieć),
- Adres IP Intel Joula + PORT (REST API Python),
- WYKORZYSTUJEMY CZUJNIKI TEMPERATURY,
2. Backend w Intel Joule w Pythonie (Flask + Influx)
- Flask = REST API, czyli:
- GET = Wszystkie pomiaru,
- PUT = Dodanie pomiaru,
- DELETE = Usunięcie pomiaru,

#Program do komunikacji ESP2688 i DHT11
Opis:
Program pobiera wartości odczytywane z modułu DHT11 wysyła do ESP2688, a  następnie wyświetla te wartości na monitorze szeregowym.
Połącznie
![IMG_20230506_170524](https://user-images.githubusercontent.com/76017554/236632357-702b2291-ba73-4080-b369-053c510cb3af.jpg)

KOD
'''
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

'''
