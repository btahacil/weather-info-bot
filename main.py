import requests

API_KEY = "BURAYA_API_ANAHTARINI_YAPIŞTIR"
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
    print(f"\n{city} için hava durumu:")
    print(f"Açıklama: {data['weather'][0]['description']}")
    print(f"Sıcaklık: {data['main']['temp']}°C")
    print(f"Nem: %{data['main']['humidity']}")
    print(f"Rüzgar Hızı: {data['wind']['speed']} m/s")
else:
    print("Şehir bulunamadı veya API hatası oluştu.")
