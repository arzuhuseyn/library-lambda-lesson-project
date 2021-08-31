import json


def save_to_db(data, case=1, db_name="db.json"):
    try:
        db = load_from_db(db_name)
        if db is None:
            db = []
        
        if case == 2:
            found = list(filter(lambda x: x['name'] == data['name'], db))
            if found:
                db.remove(found[0])

        db.append(data)

        with open(db_name, 'w') as f:
            json.dump(db, f)
        return True
    except:
        return False

def load_from_db(db_name="db.json"):
    try:
        with open(db_name, 'r') as f:
            data = json.load(f)
        return data
    except:
        return None

def flush_db(db_name="db.json"):
    try:
        with open(db_name, 'w') as f:
            f.write("")
        return True
    except:
        return False