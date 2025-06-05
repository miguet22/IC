import os
import requests

api_key = "c1db904abfa232beccd163727bb2722d"
token = os.getenv("ATTA6b793b298c4ef774ab2bec8215db70c795be58af8e9909921274eff60ed0f4e5672FB92E")
doing_list_id = os.getenv("TRELLO_DOING_LIST_ID")
done_list_id = os.getenv("TRELLO_DONE_LIST_ID")

# Buscar tarjeta "Task 1" en la lista Doing
response = requests.get(
    f"https://api.trello.com/1/lists/{doing_list_id}/cards",
    params={"key": api_key, "token": token}
)

if response.status_code != 200:
    print("Error al obtener las tarjetas:", response.text)
    exit(1)

cards = response.json()
card = next((c for c in cards if c["name"].strip().lower() == "task 1"), None)

if not card:
    print("❌ No se encontró la tarjeta 'Task 1'")
    exit(0)

card_id = card["id"]
print(f"✔️ Tarjeta encontrada: {card['name']}. Moviendo a 'Done'...")

move = requests.put(
    f"https://api.trello.com/1/cards/{card_id}",
    params={"idList": done_list_id, "key": api_key, "token": token}
)

if move.status_code == 200:
    print("✅ Tarjeta movida correctamente.")
else:
    print("❌ Falló el movimiento:", move.text)
