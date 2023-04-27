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
