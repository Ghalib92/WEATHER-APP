import requests

api_key = '0aa329f750d27fa0233822cb30e7e2e3'

while True:
    user_input = input("Enter city: ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&unitsimperial&APPID={api_key}"
    )

    if weather_data.json()['cod']=='404': #status code that the API returns
        print("City not found.")
    
    
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp =round(weather_data.json()['main']['temp'])
        temp_degrees = round(temp - 273.15)
        print(f"The weather in {user_input} is {weather}")
        print(f"The temperature in {user_input} is {temp_degrees} degrees")

    
        choice = input("Do you want to check another city? (yes/no): ")
        if choice.lower() != 'yes':
            break 