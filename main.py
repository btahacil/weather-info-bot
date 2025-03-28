import requests
import csv

API_KEY = "15782e27364ad0b320b0dfe364eff01b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Hava durumu bilgisini almak istediğiniz şehir: ")

params = {
    'q': city,
    'appid': API_KEY,
    'lang': 'tr',
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n{city} için hava durumu:")
    print(f"Açıklama: {description}")
    print(f"Sıcaklık: {temp}°C")
    print(f"Nem: %{humidity}")
    print(f"Rüzgar Hızı: {wind_speed} m/s")

    # CSV'ye kaydet
    with open('hava_durumu.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([city, description, temp, humidity, wind_speed])

    print("\nVeri başarıyla 'hava_durumu.csv' dosyasına kaydedildi.")
else:
    print("Şehir bulunamadı veya API hatası oluştu.")
