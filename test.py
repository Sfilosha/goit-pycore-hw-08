from prompt_toolkit import prompt


print(generateId())

# Ваша нотатка
note = {
    "id": 1,
    "value": "Це початковий текст нотатки"
}

print(f"--- Редагування нотатки #{note['id']} ---")
print("Підказка: Ви можете редагувати текст прямо зараз і натиснути Enter.")

# Функція prompt дозволяє передати default значення
updated_value = prompt("> ", default=note["value"])

# Оновлюємо значення в об'єкті
note["value"] = updated_value

print("\n--- Оновлено! ---")
print(f"Нове значення: {note['value']}")