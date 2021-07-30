import json
import os

def write_json(file_path: str, file_name: str, info: list or dict) -> None:
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    json_str = json.dumps(info, indent=4)
    with open("{0}/{1}".format(file_path, file_name), 'w', encoding='utf-8') as f:
        f.write(json_str)
    f.close()


def read_json(file_path: str) -> list or dict:
    if not os.path.exists(file_path):
        raise RuntimeError('No such file')
    with open(file_path, encoding='utf-8') as f:
        rp_list = json.load(f)
    return rp_list
