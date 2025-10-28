import psycopg
from psycopg import errors
import time

DB_CONFIG = {
    "dbname": "ptaha",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            return conn
    except psycopg.Error as e:
        print(f"Помилка підключення до бази даних: {e}")
        return None

# --- Manufacturers ---
def get_all_manufacturers():
    query = "SELECT manufacturer_id, company_name, country FROM manufacturers ORDER BY company_name"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
    except psycopg.Error as e:
        print(f"Помилка при отриманні виробників: {e}")
        return []

def add_manufacturer(company_name, country):
    query = "INSERT INTO manufacturers (company_name, country) VALUES (%s, %s)"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (company_name, country))
                conn.commit()
                return True
    except psycopg.Error as e:
        print(f"Помилка при доданні виробника: {e}")
        return False

def get_manufacturer_by_id(manufacturer_id):
    query = "SELECT manufacturer_id, company_name, country FROM manufacturers WHERE manufacturer_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (manufacturer_id,))
                return cur.fetchone()
    except psycopg.Error as e:
        print(f"Помилка при отриманні виробника: {e}")
        return None

def update_manufacturer(manufacturer_id, company_name, country):
    query = "UPDATE manufacturers SET company_name = %s, country = %s WHERE manufacturer_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (company_name, country, manufacturer_id))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Виробника з таким ID не знайдено для оновлення.")
                return (True, "Дані виробника успішно оновлено.")
    except psycopg.Error as e:
        print(f"Помилка при оновленні виробника: {e}")
        return (False, f"Виникла помилка: {e}")

def delete_manufacturer(manufacturer_id):
    query = "DELETE FROM manufacturers WHERE manufacturer_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (manufacturer_id,))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Виробника з таким ID не знайдено.")
                return (True, "Виробника успішно видалено.")
    except errors.ForeignKeyViolation:
        return (False, "Неможливо видалити виробника, оскільки за ним закріплені препарати.")
    except psycopg.Error as e:
        print(f"Помилка при видаленні виробника: {e}")
        return (False, f"Виникла помилка: {e}")

# --- Active Substances ---
def get_all_active_substances():
    query = "SELECT substance_id, substance_name, description FROM active_substances ORDER BY substance_name"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
    except psycopg.Error as e:
        print(f"Помилка при отриманні діючих речовин: {e}")
        return []

def add_active_substance(substance_name, description):
    query = "INSERT INTO active_substances (substance_name, description) VALUES (%s, %s)"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (substance_name, description))
                conn.commit()
                return True
    except psycopg.Error as e:
        print(f"Помилка при доданні діючої речовини: {e}")
        return False

def get_active_substance_by_id(substance_id):
    query = "SELECT substance_id, substance_name, description FROM active_substances WHERE substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (substance_id,))
                return cur.fetchone()
    except psycopg.Error as e:
        print(f"Помилка при отриманні діючої речовини: {e}")
        return None

def update_active_substance(substance_id, substance_name, description):
    query = "UPDATE active_substances SET substance_name = %s, description = %s WHERE substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (substance_name, description, substance_id))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Речовину з таким ID не знайдено для оновлення.")
                return (True, "Дані речовини успішно оновлено.")
    except psycopg.Error as e:
        print(f"Помилка при оновленні речовини: {e}")
        return (False, f"Виникла помилка: {e}")

def delete_active_substance(substance_id):
    query = "DELETE FROM active_substances WHERE substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (substance_id,))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Речовину з таким ID не знайдено.")
                return (True, "Речовину успішно видалено.")
    except errors.ForeignKeyViolation:
        return (False, "Неможливо видалити речовину, оскільки вона входить до складу препаратів.")
    except psycopg.Error as e:
        print(f"Помилка при видаленні речовини: {e}")
        return (False, f"Виникла помилка: {e}")

# --- Preparations ---
def get_all_preparations():
    query = """
        SELECT p.preparation_id, p.trade_name, p.form, p.storage_conditions, m.company_name
        FROM preparations p
        JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id
        ORDER BY p.trade_name
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
    except psycopg.Error as e:
        print(f"Помилка при отриманні препаратів: {e}")
        return []

def add_preparation(trade_name, form, storage_conditions, manufacturer_id):
    query = "INSERT INTO preparations (trade_name, form, storage_conditions, manufacturer_id) VALUES (%s, %s, %s, %s)"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (trade_name, form, storage_conditions, manufacturer_id))
                conn.commit()
                return (True, "Препарат успішно додано.")
    except errors.ForeignKeyViolation:
        return (False, "Помилка! Виробника з таким ID не існує.")
    except psycopg.Error as e:
        print(f"Помилка при доданні препарату: {e}")
        return (False, f"Виникла помилка: {e}")

def get_preparation_by_id(preparation_id):
    query = """
        SELECT p.preparation_id, p.trade_name, p.form, p.storage_conditions, p.manufacturer_id, m.company_name
        FROM preparations p
        JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id
        WHERE p.preparation_id = %s
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (preparation_id,))
                return cur.fetchone()
    except psycopg.Error as e:
        print(f"Помилка при отриманні препарату: {e}")
        return None

def update_preparation(preparation_id, trade_name, form, storage_conditions, manufacturer_id):
    query = """
        UPDATE preparations 
        SET trade_name = %s, form = %s, storage_conditions = %s, manufacturer_id = %s 
        WHERE preparation_id = %s
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (trade_name, form, storage_conditions, manufacturer_id, preparation_id))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Препарат з таким ID не знайдено для оновлення.")
                return (True, "Дані препарату успішно оновлено.")
    except errors.ForeignKeyViolation:
        return (False, "Помилка! Виробника з таким ID не існує.")
    except psycopg.Error as e:
        print(f"Помилка при оновленні препарату: {e}")
        return (False, f"Виникла помилка: {e}")

def delete_preparation(preparation_id):
    query = "DELETE FROM preparations WHERE preparation_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (preparation_id,))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Препарат з таким ID не знайдено.")
                return (True, "Препарат успішно видалено.")
    except errors.ForeignKeyViolation:
        return (False, "Неможливо видалити препарат, оскільки він має зв'язані дані (склад).")
    except psycopg.Error as e:
        print(f"Помилка при видаленні препарату: {e}")
        return (False, f"Виникла помилка: {e}")

# --- Preparation Composition (N:M Table) ---

def get_all_compositions():
    query = """
        SELECT 
            p.preparation_id, p.trade_name, 
            s.substance_id, s.substance_name, 
            pc.dosage
        FROM preparation_composition pc
        JOIN preparations p ON pc.preparation_id = p.preparation_id
        JOIN active_substances s ON pc.substance_id = s.substance_id
        ORDER BY p.trade_name, s.substance_name
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
    except psycopg.Error as e:
        print(f"Помилка при отриманні складу препаратів: {e}")
        return []

def get_composition_by_id(preparation_id, substance_id):
    query = "SELECT preparation_id, substance_id, dosage FROM preparation_composition WHERE preparation_id = %s AND substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (preparation_id, substance_id))
                return cur.fetchone()
    except psycopg.Error as e:
        print(f"Помилка при отриманні запису зі складу: {e}")
        return None

def add_composition(preparation_id, substance_id, dosage):
    query = "INSERT INTO preparation_composition (preparation_id, substance_id, dosage) VALUES (%s, %s, %s)"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (preparation_id, substance_id, dosage))
                conn.commit()
                return (True, "Запис до складу успішно додано.")
    except errors.UniqueViolation:
        return (False, "Помилка! Ця речовина вже є у складі цього препарату.")
    except errors.ForeignKeyViolation:
        return (False, "Помилка! Вказано неіснуючий ID препарату або речовини.")
    except psycopg.Error as e:
        print(f"Помилка при доданні до складу: {e}")
        return (False, f"Виникла помилка: {e}")

def update_composition(preparation_id, substance_id, new_dosage):
    query = "UPDATE preparation_composition SET dosage = %s WHERE preparation_id = %s AND substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (new_dosage, preparation_id, substance_id))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Запис з такими ID не знайдено для оновлення.")
                return (True, "Дозування успішно оновлено.")
    except psycopg.Error as e:
        print(f"Помилка при оновленні складу: {e}")
        return (False, f"Виникла помилка: {e}")

def delete_composition(preparation_id, substance_id):
    query = "DELETE FROM preparation_composition WHERE preparation_id = %s AND substance_id = %s"
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (preparation_id, substance_id))
                conn.commit()
                if cur.rowcount == 0:
                    return (False, "Запис з такими ID не знайдено.")
                return (True, "Запис зі складу успішно видалено.")
    except psycopg.Error as e:
        print(f"Помилка при видаленні зі складу: {e}")
        return (False, f"Виникла помилка: {e}")

# --- Data Generation & Clearing ---

def clear_all_data():
    query = """
        TRUNCATE 
            manufacturers, 
            active_substances, 
            preparations, 
            preparation_composition 
        RESTART IDENTITY CASCADE;
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
                return (True, "Всі дані з таблиць було успішно видалено, лічильники скинуто.")
    except psycopg.Error as e:
        print(f"Помилка при очищенні таблиць: {e}")
        return (False, f"Виникла помилка: {e}")

def generate_manufacturers(count):
    query = """
        INSERT INTO manufacturers (company_name, country)
        SELECT 
            (ARRAY['Astra', 'Bio', 'Medi', 'Pharma', 'Gene', 'Nova', 'Hemo', 'Zene'])[trunc(random()*8+1)] || 
            (ARRAY['Core', 'Tech', 'Labs', 'Solutions', 'Genics', 'Life', 'Farm'])[trunc(random()*7+1)] || ' ' || 
            (ARRAY['Inc.', 'AG', 'LLC', 'Group'])[trunc(random()*4+1)],
            
            (ARRAY['USA', 'Germany', 'Ukraine', 'India', 'Poland', 'Switzerland', 'Japan'])[trunc(random()*7 + 1)]
        FROM generate_series(1, %s) AS s(id);
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (count,))
                conn.commit()
                return (True, f"Успішно згенеровано {count} виробників.")
    except psycopg.Error as e:
        print(f"Помилка генерації виробників: {e}")
        return (False, f"Помилка: {e}")

def generate_active_substances(count):
    query = """
        INSERT INTO active_substances (substance_name, description)
        SELECT 
            (ARRAY['Aceta', 'Ibu', 'Levo', 'Dextra', 'Meto', 'Serta', 'Amlo', 'Ome', 'Lisi', 'Atorva'])[trunc(random()*10+1)] ||
            (ARRAY['profen', 'minophen', 'cetin', 'line', 'dipine', 'prazole', 'nacin', 'xetil', 'pril', 'statin'])[trunc(random()*10+1)],
            
            (ARRAY[
                'Non-steroidal anti-inflammatory drug (NSAID)', 
                'Beta-blocker for hypertension', 
                'Proton pump inhibitor (PPI)', 
                'SSRI antidepressant', 
                'Analgesic and antipyretic', 
                'Calcium channel blocker',
                'ACE inhibitor'
            ])[trunc(random()*7+1)] || ' (Gen ' || s.id || ')'
        FROM generate_series(1, %s) AS s(id);
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (count,))
                conn.commit()
                return (True, f"Успішно згенеровано {count} діючих речовин.")
    except psycopg.Error as e:
        print(f"Помилка генерації речовин: {e}")
        return (False, f"Помилка: {e}")

def generate_preparations(count):
    query = """
        INSERT INTO preparations (trade_name, form, storage_conditions, manufacturer_id)
        SELECT 
            (ARRAY['Nuro', 'Pana', 'Aspi', 'Vibro', 'Strepto', 'Tera', 'Amoxi', 'Mezy'])[trunc(random()*8+1)] ||
            (ARRAY['fen', 'dol', 'rin', 'cil', 'flu', 'sil', 'clav', 'form'])[trunc(random()*8+1)] || '-' ||
            (ARRAY['D', 'Forte', 'Max', 'Eco'])[trunc(random()*4+1)],

            (ARRAY['Tablets', 'Syrup', 'Capsules', 'Ointment', 'Injection'])[trunc(random()*5 + 1)],
            'Store at ' || trunc(random()*20 + 5) || 'C',
            
            (SELECT manufacturer_id FROM manufacturers WHERE manufacturer_id > 0 OR g.id > 0 ORDER BY random() LIMIT 1)
        FROM generate_series(1, %s) AS g(id);
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (count,))
                conn.commit()
                return (True, f"Успішно згенеровано {count} препаратів.")
    except psycopg.Error as e:
        print(f"Помилка генерації препаратів: {e}")
        if "null value in column \"manufacturer_id\"" in str(e) or "is not present in table \"manufacturers\"" in str(e):
            return (False, "Помилка: Неможливо згенерувати препарати. Таблиця виробників порожня.")
        return (False, f"Помилка: {e}")

def generate_compositions(count):
    query = """
        INSERT INTO preparation_composition (preparation_id, substance_id, dosage)
        SELECT
            (SELECT preparation_id FROM preparations WHERE preparation_id > 0 OR g.id > 0 ORDER BY random() LIMIT 1),
            (SELECT substance_id FROM active_substances WHERE substance_id > 0 OR g.id > 0 ORDER BY random() LIMIT 1),
            trunc(random()*500 + 50)::text || ' mg'
        FROM generate_series(1, %s) g(id)
        ON CONFLICT (preparation_id, substance_id) DO NOTHING;
    """
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (count,))
                conn.commit()
                return (True, f"Успішно згенеровано {count} записів у склад (дублікати проігноровано).")
    except psycopg.Error as e:
        print(f"Помилка генерації складу: {e}")
        if "null value in column" in str(e) or "is not present in table" in str(e):
             return (False, "Помилка: Неможливо згенерувати склад. Таблиці препаратів або речовин порожні.")
        return (False, f"Помилка: {e}")

# --- Search Queries (RGR Task) ---

def execute_search_query(query, params=()):
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                start_time = time.monotonic()
                cur.execute(query, params)
                results = cur.fetchall()
                end_time = time.monotonic()
                
                duration_ms = (end_time - start_time) * 1000
                column_names = [col.name for col in cur.description]
                
                return (results, column_names, duration_ms, None)
    except psycopg.Error as e:
        print(f"Помилка виконання пошукового запиту: {e}")
        return (None, None, 0, str(e))

def search_manufacturers_by_prep_count(country_pattern, form_exact, min_prep_count):
    query = """
        SELECT m.company_name, m.country, COUNT(p.preparation_id) as preparation_count
        FROM manufacturers m
        JOIN preparations p ON m.manufacturer_id = p.manufacturer_id
        WHERE m.country ILIKE %s AND p.form = %s
        GROUP BY m.manufacturer_id, m.company_name, m.country
        HAVING COUNT(p.preparation_id) > %s
        ORDER BY preparation_count DESC;
    """
    return execute_search_query(query, (country_pattern, form_exact, min_prep_count))

def search_substances_by_storage_temp(substance_pattern, min_temp, max_temp):
    query = """
        SELECT s.substance_name, s.description, COUNT(p.preparation_id) as used_in_preparations
        FROM active_substances s
        JOIN preparation_composition pc ON s.substance_id = pc.substance_id
        JOIN preparations p ON pc.preparation_id = p.preparation_id
        WHERE s.substance_name ILIKE %s
          AND CAST(regexp_replace(p.storage_conditions, '[^0-9]', '', 'g') AS INTEGER) BETWEEN %s AND %s
        GROUP BY s.substance_id, s.substance_name, s.description
        ORDER BY used_in_preparations DESC;
    """
    return execute_search_query(query, (substance_pattern, min_temp, max_temp))

def search_preparations_by_composition(prep_name_pattern, form_exact, substance_desc_pattern):
    query = """
        SELECT p.trade_name, p.form, COUNT(s.substance_id) as matching_substances
        FROM preparations p
        JOIN preparation_composition pc ON p.preparation_id = pc.preparation_id
        JOIN active_substances s ON pc.substance_id = s.substance_id
        WHERE p.trade_name ILIKE %s AND p.form = %s AND s.description ILIKE %s
        GROUP BY p.preparation_id, p.trade_name, p.form
        ORDER BY matching_substances DESC;
    """
    return execute_search_query(query, (prep_name_pattern, form_exact, substance_desc_pattern))
