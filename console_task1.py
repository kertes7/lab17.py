from assistant_task1 import Assistant

assistant = Assistant()

while True:
    command = input("Введіть команду (/add, /list, /search, /exit): ").strip()

    if command == "/add":
        note = input("Введіть нотатку: ")
        assistant.add_note(note)
        print("Нотатку додано.")

    elif command == "/list":
        notes = assistant.list_notes()
        if notes:
            print("\n".join(notes))
        else:
            print("Нотаток немає.")

    elif command == "/search":
        keyword = input("Ключове слово: ")
        results = assistant.search_notes(keyword)
        if results:
            print("\n".join(results))
        else:
            print("Збігів не знайдено.")

    elif command == "/exit":
        print("До побачення!")
        break

    else:
        print("Невідома команда.")
