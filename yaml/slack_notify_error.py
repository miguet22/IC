# slack_notify_error.py

import requests
import json
import os

def send_error_slack_message():
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')  # Asegúrate de que este secret esté configurado en GitHub
    message = {
        "text": f"🚨 *El workflow falló.*\nRepositorio: {os.getenv('GITHUB_REPOSITORY')}\nCommit: {os.getenv('GITHUB_SHA')}\nAutor: {os.getenv('GITHUB_ACTOR')}",
        
    }

    response = requests.post(slack_webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
    
    if response.status_code == 200:
        print("Mensaje de error enviado correctamente a Slack")
    else:
        print(f"Error al enviar mensaje: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_error_slack_message()
