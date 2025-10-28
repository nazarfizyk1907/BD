def show_main_menu():
    print("\n--- Головне Меню: Довідник Медичних Препаратів ---")
    print("--- Керування Виробниками (CRUD) ---")
    print("1. Показати | 2. Додати | 3. Редагувати | 4. Видалити")
    print("--- Керування Речовинами (CRUD) ---")
    print("5. Показати | 6. Додати | 7. Редагувати | 8. Видалити")
    print("--- Керування Препаратами (CRUD) ---")
    print("9. Показати | 10. Додати | 11. Редагувати | 12. Видалити")
    print("--- Керування Складом (CRUD) ---")
    print("13. Показати | 14. Додати | 15. Редагувати | 16. Видалити")
    print("--------------------------------------------------")
    print("--- Завдання РГР ---")
    print("17. Автоматична генерація даних")
    print("18. Меню пошуку")
    print("19. ОЧИСТИТИ ВСІ ДАНІ (TRUNCATE)")
    print("--------------------------------------------------")
    print("0. Вихід")
    return input("Оберіть опцію [0-19]: ")

def show_all_manufacturers(manufacturers_list):
    if not manufacturers_list:
        print("\nСписок виробників порожній.")
        return
    
    print("\n--- Список Виробників ---")
    print(f"{'ID':<5} | {'Назва компанії':<30} | {'Країна':<20}")
    print("-" * 57)
    
    for row in manufacturers_list:
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<20}")

def get_new_manufacturer_data():
    print("\n--- Додавання Нового Виробника ---")
    company_name = input("Введіть назву компанії: ").strip()
    country = input("Введіть країну: ").strip()
    return company_name, country

def get_id_input(prompt_message):
    print(f"\n--- {prompt_message} ---")
    try:
        item_id = int(input("Введіть ID: "))
        return item_id
    except ValueError:
        return None

def get_updated_manufacturer_data(manufacturer_data):
    print("\n--- Редагування Виробника ---")
    print(f"Поточна назва: {manufacturer_data[1]}")
    new_company_name = input(f"Введіть нову назву (або Enter, щоб лишити поточну): ").strip()
    
    print(f"Поточна країна: {manufacturer_data[2]}")
    new_country = input(f"Введіть нову країну (або Enter, щоб лишити поточну): ").strip()

    if not new_company_name:
        new_company_name = manufacturer_data[1]
    if not new_country:
        new_country = manufacturer_data[2]
        
    return new_company_name, new_country

def show_message(message):
    print(f"\n[ПОВІДОМЛЕННЯ] {message}")

# --- Active Substances Views ---

def show_all_active_substances(substances_list):
    if not substances_list:
        print("\nСписок діючих речовин порожній.")
        return
    
    print("\n--- Список Діючих Речовин ---")
    print(f"{'ID':<5} | {'Назва речовини':<30} | {'Опис':<40}")
    print("-" * 77)
    
    for row in substances_list:
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<40}")

def get_new_active_substance_data():
    print("\n--- Додавання Нової Діючої Речовини ---")
    substance_name = input("Введіть назву речовини: ").strip()
    description = input("Введіть опис: ").strip()
    return substance_name, description

def get_updated_active_substance_data(substance_data):
    print("\n--- Редагування Діючої Речовини ---")
    print(f"Поточна назва: {substance_data[1]}")
    new_name = input(f"Введіть нову назву (або Enter, щоб лишити поточну): ").strip()
    
    print(f"Поточний опис: {substance_data[2]}")
    new_description = input(f"Введіть новий опис (або Enter, щоб лишити поточний): ").strip()

    if not new_name:
        new_name = substance_data[1]
    if not new_description:
        new_description = substance_data[2]
        
    return new_name, new_description

# --- Preparations Views ---

def show_all_preparations(preparations_list):
    if not preparations_list:
        print("\nСписок препаратів порожній.")
        return
    
    print("\n--- Список Препаратів ---")
    print(f"{'ID':<5} | {'Торгова назва':<25} | {'Форма':<15} | {'Виробник':<30}")
    print("-" * 77)
    
    for row in preparations_list:
        print(f"{row[0]:<5} | {row[1]:<25} | {row[2]:<15} | {row[4]:<30}")

def get_new_preparation_data(manufacturers_list):
    print("\n--- Додавання Нового Препарату ---")
    trade_name = input("Введіть торгову назву: ").strip()
    form = input("Введіть форму (таблетки, сироп...): ").strip()
    storage_conditions = input("Введіть умови зберігання: ").strip()
    
    print("\nОберіть ID виробника з списку:")
    show_all_manufacturers(manufacturers_list)
    try:
        manufacturer_id = int(input("Введіть ID виробника: "))
    except ValueError:
        return None
    
    return trade_name, form, storage_conditions, manufacturer_id

def get_updated_preparation_data(preparation_data, manufacturers_list):
    print("\n--- Редагування Препарату ---")
    
    print(f"Поточна назва: {preparation_data[1]}")
    new_trade_name = input("Введіть нову назву (або Enter): ").strip() or preparation_data[1]
    
    print(f"Поточна форма: {preparation_data[2]}")
    new_form = input("Введіть нову форму (або Enter): ").strip() or preparation_data[2]

    print(f"Поточні умови зберігання: {preparation_data[3]}")
    new_storage_conditions = input("Введіть нові умови (або Enter): ").strip() or preparation_data[3]
    
    print(f"\nПоточний виробник: {preparation_data[5]} (ID: {preparation_data[4]})")
    print("Оберіть нового ID виробника з списку (або Enter, щоб лишити поточного):")
    show_all_manufacturers(manufacturers_list)
    
    try:
        manufacturer_id_input = input("Введіть ID виробника: ")
        new_manufacturer_id = int(manufacturer_id_input) if manufacturer_id_input else preparation_data[4]
    except ValueError:
        return None
        
    return new_trade_name, new_form, new_storage_conditions, new_manufacturer_id

# --- Composition Views ---

def show_all_compositions(composition_list):
    if not composition_list:
        print("\nСписок складу препаратів порожній.")
        return
    
    print("\n--- Склад Препаратів ---")
    print(f"{'ID Преп.':<8} | {'Назва Препарату':<25} | {'ID Реч.':<8} | {'Назва Речовини':<25} | {'Дозування':<15}")
    print("-" * 85)
    
    for row in composition_list:
        print(f"{row[0]:<8} | {row[1]:<25} | {row[2]:<8} | {row[3]:<25} | {row[4]:<15}")

def get_new_composition_data(preparations_list, substances_list):
    print("\n--- Додавання Речовини до Складу Препарату ---")
    
    print("\nОберіть ID препарату з списку:")
    show_all_preparations(preparations_list)
    try:
        preparation_id = int(input("Введіть ID препарату: "))
    except ValueError:
        return None
    
    print("\nОберіть ID діючої речовини з списку:")
    show_all_active_substances(substances_list)
    try:
        substance_id = int(input("Введіть ID речовини: "))
    except ValueError:
        return None

    dosage = input("Введіть дозування (напр. '500 мг'): ").strip()
    
    return preparation_id, substance_id, dosage

def get_composition_ids(prompt_message):
    print(f"\n--- {prompt_message} ---")
    try:
        preparation_id = int(input("Введіть ID препарату: "))
        substance_id = int(input("Введіть ID діючої речовини: "))
        return preparation_id, substance_id
    except ValueError:
        return None

def get_updated_composition_data(composition_data):
    print("\n--- Редагування Дозування ---")
    print(f"Поточне дозування: {composition_data[2]}")
    new_dosage = input("Введіть нове дозування (або Enter): ").strip() or composition_data[2]
    return new_dosage

# --- RGR Task Views ---

def get_generation_counts():
    print("\n--- Автоматична Генерація Даних ---")
    print("Введіть кількість записів для генерації. Введіть 0, щоб пропустити.")
    try:
        count_m = int(input("Кількість Виробників: "))
        count_as = int(input("Кількість Діючих Речовин: "))
        count_p = int(input("Кількість Препаратів: "))
        count_pc = int(input("Кількість Записів у Склад (N:M): "))
        return count_m, count_as, count_p, count_pc
    except ValueError:
        return None

def get_clear_confirmation():
    print("\n--- ОЧИЩЕННЯ БАЗИ ДАНИХ ---")
    print("УВАГА! Ця дія НЕВІДВОРОТНЬО видалить ВСІ дані з УСІХ таблиць.")
    print("Лічильники ID будуть скинуті до 1.")
    confirm = input("Для підтвердження введіть 'yes': ").strip().lower()
    return confirm == 'yes'

# --- RGR Search Views ---

def show_search_menu():
    print("\n--- Меню Пошуку ---")
    print("1. Пошук виробників за кількістю препаратів")
    print("2. Пошук речовин за температурою зберігання препаратів")
    print("3. Пошук препаратів за описом речовин у складі")
    print("--------------------------------------------------")
    print("0. Повернутись до головного меню")
    return input("Оберіть опцію [0-3]: ")

def show_search_results(results, column_names, duration_ms):
    if results is None:
        return 

    if not results:
        print("\n[РЕЗУЛЬТАТ] Нічого не знайдено.")
        print(f"Час виконання: {duration_ms:.2f} мс")
        return

    print("\n--- Результати Пошуку ---")
    
    col_widths = [len(name) for name in column_names]
    for row in results:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))
    
    header = " | ".join([f"{name:<{col_widths[i]}}" for i, name in enumerate(column_names)])
    print(header)
    print("-" * len(header))
    
    for row in results:
        row_str = " | ".join([f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)])
        print(row_str)
        
    print("-" * len(header))
    print(f"Знайдено рядків: {len(results)}. Час виконання: {duration_ms:.2f} мс")

def get_search_query_1_input():
    print("\n--- Пошук виробників за кількістю препаратів ---")
    country_pattern = input("Введіть шаблон країни (напр. 'Ukr%'): ") or "%"
    form_exact = input("Введіть точну форму препарату (напр. 'Tablets'): ") or "Tablets"
    try:
        min_prep_count = int(input("Мінімальна кількість препаратів (напр. 5): ") or "0")
        return country_pattern, form_exact, min_prep_count
    except ValueError:
        return None

def get_search_query_2_input():
    print("\n--- Пошук речовин за температурою зберігання ---")
    substance_pattern = input("Введіть шаблон назви речовини (напр. '%profen%'): ") or "%"
    try:
        min_temp = int(input("Мін. температура зберігання (напр. 5): ") or "0")
        max_temp = int(input("Макс. температура зберігання (напр. 20): ") or "100")
        return substance_pattern, min_temp, max_temp
    except ValueError:
        return None

def get_search_query_3_input():
    print("\n--- Пошук препаратів за описом речовин ---")
    prep_name_pattern = input("Введіть шаблон назви препарату (напр. 'Nuro%'): ") or "%"
    form_exact = input("Введіть точну форму препарату (напр. 'Tablets'): ") or "Tablets"
    substance_desc_pattern = input("Введіть шаблон опису речовини (напр. '%anti-inflammatory%'): ") or "%"
    return prep_name_pattern, form_exact, substance_desc_pattern
