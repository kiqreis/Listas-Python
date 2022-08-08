import json
def is_json(string):
    try:
        json.loads(string)
        return True
    except json.JSONDecodeError:
        return False

if __name__ == '__main__':
    print(is_json())
