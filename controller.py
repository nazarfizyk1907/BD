import model
import view
import time

class Controller:
    def __init__(self):
        pass

    def run(self):
        while True:
            choice = view.show_main_menu()

            if choice == '1':
                self.list_manufacturers()
            elif choice == '2':
                self.add_new_manufacturer()
            elif choice == '3':
                self.edit_manufacturer()
            elif choice == '4':
                self.remove_manufacturer()
            elif choice == '5':
                self.list_active_substances()
            elif choice == '6':
                self.add_new_active_substance()
            elif choice == '7':
                self.edit_active_substance()
            elif choice == '8':
                self.remove_active_substance()
            elif choice == '9':
                self.list_preparations()
            elif choice == '10':
                self.add_new_preparation()
            elif choice == '11':
                self.edit_preparation()
            elif choice == '12':
                self.remove_preparation()
            elif choice == '13':
                self.list_compositions()
            elif choice == '14':
                self.add_new_composition()
            elif choice == '15':
                self.edit_composition()
            elif choice == '16':
                self.remove_composition()
            elif choice == '17':
                self.generate_data()
            elif choice == '18':
                self.run_search_menu()
            elif choice == '19':
                self.clear_data()
            elif choice == '0':
                view.show_message("Дякуємо за використання! Вихід...")
                break
            else:
                view.show_message("Невірна опція. Будь ласка, спробуйте ще раз.")

    # --- Manufacturers Controllers ---

    def list_manufacturers(self):
        manufacturers = model.get_all_manufacturers()
        view.show_all_manufacturers(manufacturers)

    def add_new_manufacturer(self):
        company_name, country = view.get_new_manufacturer_data()
        
        if not company_name or not country:
            view.show_message("Назва компанії та країна не можуть бути порожніми.")
            return

        success = model.add_manufacturer(company_name, country)
        
        if success:
            view.show_message("Виробника успішно додано!")
        else:
            view.show_message("Помилка! Не вдалося додати виробника.")

    def edit_manufacturer(self):
        manufacturer_id = view.get_id_input("Редагування Виробника")
        if manufacturer_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        manufacturer = model.get_manufacturer_by_id(manufacturer_id)
        if not manufacturer:
            view.show_message(f"Виробника з ID {manufacturer_id} не знайдено.")
            return
        
        new_name, new_country = view.get_updated_manufacturer_data(manufacturer)
        
        success, message = model.update_manufacturer(manufacturer_id, new_name, new_country)
        view.show_message(message)

    def remove_manufacturer(self):
        manufacturer_id = view.get_id_input("Видалення Виробника")
        if manufacturer_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        success, message = model.delete_manufacturer(manufacturer_id)
        view.show_message(message)

    # --- Active Substances Controllers ---

    def list_active_substances(self):
        substances = model.get_all_active_substances()
        view.show_all_active_substances(substances)

    def add_new_active_substance(self):
        substance_name, description = view.get_new_active_substance_data()
        
        if not substance_name:
            view.show_message("Назва речовини не може бути порожньою.")
            return

        success = model.add_active_substance(substance_name, description)
        
        if success:
            view.show_message("Діючу речовину успішно додано!")
        else:
            view.show_message("Помилка! Не вдалося додати речовину.")

    def edit_active_substance(self):
        substance_id = view.get_id_input("Редагування Діючої Речовини")
        if substance_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        substance = model.get_active_substance_by_id(substance_id)
        if not substance:
            view.show_message(f"Речовину з ID {substance_id} не знайдено.")
            return
        
        new_name, new_description = view.get_updated_active_substance_data(substance)
        
        success, message = model.update_active_substance(substance_id, new_name, new_description)
        view.show_message(message)

    def remove_active_substance(self):
        substance_id = view.get_id_input("Видалення Діючої Речовини")
        if substance_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        success, message = model.delete_active_substance(substance_id)
        view.show_message(message)
    
    # --- Preparations Controllers ---

    def list_preparations(self):
        preparations = model.get_all_preparations()
        view.show_all_preparations(preparations)
    
    def add_new_preparation(self):
        manufacturers = model.get_all_manufacturers()
        if not manufacturers:
            view.show_message("Неможливо додати препарат. Спочатку додайте хоча б одного виробника.")
            return
            
        data = view.get_new_preparation_data(manufacturers)
        if data is None:
            view.show_message("Некоректний ID виробника. Додавання скасовано.")
            return
            
        trade_name, form, storage, manuf_id = data
        if not trade_name:
            view.show_message("Торгова назва не може бути порожньою.")
            return
            
        success, message = model.add_preparation(trade_name, form, storage, manuf_id)
        view.show_message(message)

    def edit_preparation(self):
        preparation_id = view.get_id_input("Редагування Препарату")
        if preparation_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        preparation = model.get_preparation_by_id(preparation_id)
        if not preparation:
            view.show_message(f"Препарат з ID {preparation_id} не знайдено.")
            return
        
        manufacturers = model.get_all_manufacturers()
        data = view.get_updated_preparation_data(preparation, manufacturers)
        
        if data is None:
            view.show_message("Некоректний ID виробника. Оновлення скасовано.")
            return
            
        new_name, new_form, new_storage, new_manuf_id = data
        success, message = model.update_preparation(preparation_id, new_name, new_form, new_storage, new_manuf_id)
        view.show_message(message)

    def remove_preparation(self):
        preparation_id = view.get_id_input("Видалення Препарату")
        if preparation_id is None:
            view.show_message("Некоректний ID. Введіть число.")
            return

        success, message = model.delete_preparation(preparation_id)
        view.show_message(message)

    # --- Composition Controllers ---

    def list_compositions(self):
        compositions = model.get_all_compositions()
        view.show_all_compositions(compositions)

    def add_new_composition(self):
        preparations = model.get_all_preparations()
        substances = model.get_all_active_substances()
        
        if not preparations or not substances:
            view.show_message("Помилка! Для додавання у склад потрібен хоча б один препарат і одна речовина.")
            return

        data = view.get_new_composition_data(preparations, substances)
        if data is None:
            view.show_message("Некоректні ID. Додавання скасовано.")
            return

        prep_id, sub_id, dosage = data
        if not dosage:
            view.show_message("Дозування не може бути порожнім.")
            return
            
        success, message = model.add_composition(prep_id, sub_id, dosage)
        view.show_message(message)

    def edit_composition(self):
        ids = view.get_composition_ids("Редагування Складу")
        if ids is None:
            view.show_message("Некоректні ID. Введіть числа.")
            return
        
        prep_id, sub_id = ids
        composition = model.get_composition_by_id(prep_id, sub_id)
        
        if not composition:
            view.show_message(f"Запис з ID препарату {prep_id} та ID речовини {sub_id} не знайдено.")
            return
            
        new_dosage = view.get_updated_composition_data(composition)
        if not new_dosage:
            view.show_message("Дозування не може бути порожнім.")
            return
            
        success, message = model.update_composition(prep_id, sub_id, new_dosage)
        view.show_message(message)

    def remove_composition(self):
        ids = view.get_composition_ids("Видалення зі Складу")
        if ids is None:
            view.show_message("Некоректні ID. Введіть числа.")
            return

        prep_id, sub_id = ids
        success, message = model.delete_composition(prep_id, sub_id)
        view.show_message(message)

    # --- RGR Task Controllers ---
    
    def generate_data(self):
        counts = view.get_generation_counts()
        if counts is None:
            view.show_message("Некоректний ввід. Введіть числа.")
            return

        count_m, count_as, count_p, count_pc = counts
        
        if count_m > 0:
            success, message = model.generate_manufacturers(count_m)
            view.show_message(message)
        
        if count_as > 0:
            success, message = model.generate_active_substances(count_as)
            view.show_message(message)
            
        if count_p > 0:
            success, message = model.generate_preparations(count_p)
            view.show_message(message)

        if count_pc > 0:
            success, message = model.generate_compositions(count_pc)
            view.show_message(message)

        if all(c == 0 for c in counts):
            view.show_message("Генерацію скасовано (введено 0).")
    
    def clear_data(self):
        if not view.get_clear_confirmation():
            view.show_message("Очищення скасовано.")
            return
            
        success, message = model.clear_all_data()
        view.show_message(message)

    # --- RGR Search Controllers ---

    def run_search_menu(self):
        while True:
            choice = view.show_search_menu()
            if choice == '1':
                self.handle_search_query_1()
            elif choice == '2':
                self.handle_search_query_2()
            elif choice == '3':
                self.handle_search_query_3()
            elif choice == '0':
                break
            else:
                view.show_message("Невірна опція. Будь ласка, спробуйте ще раз.")

    def handle_search_query_1(self):
        inputs = view.get_search_query_1_input()
        if inputs is None:
            view.show_message("Некоректний ввід. Введіть числа.")
            return
        
        country, form, min_count = inputs
        results, cols, duration, error = model.search_manufacturers_by_prep_count(country, form, min_count)
        
        if error:
            view.show_message(f"Помилка пошуку: {error}")
        else:
            view.show_search_results(results, cols, duration)

    def handle_search_query_2(self):
        inputs = view.get_search_query_2_input()
        if inputs is None:
            view.show_message("Некоректний ввід. Введіть числа.")
            return
            
        subst, min_t, max_t = inputs
        results, cols, duration, error = model.search_substances_by_storage_temp(subst, min_t, max_t)
        
        if error:
            view.show_message(f"Помилка пошуку: {error}")
        else:
            view.show_search_results(results, cols, duration)

    def handle_search_query_3(self):
        inputs = view.get_search_query_3_input()
        prep, form, subst_desc = inputs
        results, cols, duration, error = model.search_preparations_by_composition(prep, form, subst_desc)
        
        if error:
            view.show_message(f"Помилка пошуку: {error}")
        else:
            view.show_search_results(results, cols, duration)
