import json
import requests

API_KEY = "1768cef5014149e19db20150250204"  # Replace with your actual key

def lambda_handler(event, context):
    country_name = event.get('queryStringParameters', {}).get('country')

    if not country_name:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Country name is required'})
        }

    try:
        # Fetch weather data
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={country_name}")
        response.raise_for_status()
        data = response.json()

        weather_condition = data['current']['condition']['text']

        # Fetch activity suggestions from your friend's API
        activity_response = requests.get(
            f"https://65wb2cfcug.execute-api.eu-west-1.amazonaws.com/hproduction/suggest-activities?weather_condition={weather_condition}"
        )
        activity_response.raise_for_status()
        activity_data = activity_response.json()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'weather': {
                    'temperature_celsius': data['current']['temp_c'],
                    'condition': weather_condition
                },
                'activities': activity_data.get('activities', [])
            })
        }

    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
