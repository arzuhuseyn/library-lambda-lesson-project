import json


def save_to_db(data, db_name="db.json"):
    try:
        with open(db_name, 'w') as f:
            json.dump([data], f)
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