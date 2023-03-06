from geopy.geocoders import Nominatim
from geopy import distance
import folium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
Ring = 0
while True:
    #Получение текущего местоположения пользователя
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Мое местоположение")
    user_location = (location.latitude, location.longitude)

    # Создать карту с начальными координатами
    m = folium.Map(location=[55.7558, 37.6173], zoom_start=10)

    # Добавить возможность выбора точки на карте
    folium.LatLngPopup().add_to(m)

    # Сохранить координаты выбранной точки
    coordinates = []

    def on_map_click(event):
        """Обработчик события клика на карте"""
        if event.type == 'click':
            lat = event.latlng[0]
            lon = event.latlng[1]
            coordinates.append((lat, lon))
            flagPoint = 1
            return flagPoint
    
    # Добавить обработчик событий на карту
    m.add_child(folium.ClickForMarker(popup=None, callback=on_map_click))
    flagPoint = callback
    callback = 0
    #отправка уведомления
    if Ring: 
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("notification.html")
        driver.execute_script("showNotification()")
        driver.quit()
        Ring = 0
    destination = coordinates[-1]
    while flagPoint == 1:

        #Рассчитать расстояние между пользователя и целевыми координатами
        dist = distance.distance(user_location, destination).km

        # Вывести результат
        if (dist <= 0.5):
            Ring = 1
            flagPoint = 0
            break