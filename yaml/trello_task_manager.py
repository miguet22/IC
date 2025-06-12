# trello_task_manager.py

import os
import requests
import sys

if len(sys.argv) != 3:
    print("❌ Uso: python trello_task_manager.py [start|finish] [nombre_tarea]")
    sys.exit(1)

accion = sys.argv[1]
card_name = sys.argv[2].strip().lower()

api_key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_API_TOKEN")
todo_list_id = os.getenv("TRELLO_TODO_LIST_ID")
doing_list_id = os.getenv("TRELLO_DOING_LIST_ID")
done_list_id = os.getenv("TRELLO_DONE_LIST_ID")

# Si la acción es 'none', no hacer nada
if accion == "none":
    print(f"✔️ La tarea '{card_name}' sigue en progreso. No se realiza ninguna acción.")
    sys.exit(0)

if accion == "start":
    from_list = todo_list_id
    to_list = doing_list_id
elif accion == "finish":
    from_list = doing_list_id
    to_list = done_list_id
else:
    print("❌ Acción no válida.")
    sys.exit(1)

response = requests.get(
    f"https://api.trello.com/1/lists/{from_list}/cards",
    params={"key": api_key, "token": token}
)

if response.status_code != 200:
    print("❌ Error al obtener tarjetas:", response.text)
    sys.exit(1)

cards = response.json()
card = next((c for c in cards if c["name"].strip().lower() == card_name), None)

if not card:
    print(f"❌ No se encontró la tarjeta '{card_name}' en la lista esperada.")
    sys.exit(0)

card_id = card["id"]
print(f"✔️ Tarjeta encontrada: {card_name}. Moviendo...")

move = requests.put(
    f"https://api.trello.com/1/cards/{card_id}",
    params={"idList": to_list, "key": api_key, "token": token}
)

if move.status_code == 200:
    print("✅ Tarjeta movida correctamente.")
else:
    print("❌ Falló el movimiento:", move.text)
