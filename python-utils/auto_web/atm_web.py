import webbrowser as wb
import os
import keyboard as kb
import sys
import yaml
import pandas as pd

sys.path.append("..")
from datproc.file_data import read_json, write_json


def open_web(_link: str) -> None:
    """
    Opens one link
    :param _link:
    :return:
    """
    wb.open(_link)


def read_setting() -> dict:
    """
    Reads the setting from the file
    :return: setting dictionary
    """
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(cur_path, "settings.yaml")
    f = open(yaml_path, 'r', encoding='utf-8')
    d = yaml.load(f.read(), Loader=yaml.FullLoader)
    return d


def main() -> None:
    """
    Main program entry
    :return:
    """
    setting = read_setting()
    link_list = []
    try:
        if setting['file']['name'][-5:] == '.json':
            link_list = read_json(str(setting['file']['name']))
        elif setting['file']['name'][-4:] == '.csv':
            # TODO:
            return
        elif setting['file']['name'][-5:] == '.xlsx':
            df = pd.read_excel(setting['file']['name'])
            link_list = list(df[setting['file']['column_name_html']])
        else:
            return
    except RuntimeError:
        print("OOPS")
    except Exception:
        print("OOPS")

    hotkey_1: str = setting['hotkey']['open'] if setting['hotkey']['open'] is not None else 'ctrl+alt+q'
    hotkey_2: str = setting['hotkey']['wait'] if setting['hotkey']['wait'] is not None else 'ctrl+alt+e'
    tmp = None
    try:
        tmp = kb.add_hotkey(hotkey_1, open_web, args=('link',))
    except ValueError as ve:
        hotkey_1 = 'ctrl+alt+q'
        tmp = kb.add_hotkey(hotkey_1, open_web, args=('link',))
        print("hotkey--open is not valid -> hence automatically modified to default value `ctrl+alt+q`")
    finally:
        try:
            kb.remove_hotkey(tmp)
        except ValueError as v:
            hotkey_2 = 'ctrl+alt+e'
            kb.remove_hotkey(tmp)
            print("hotkey--wait is not valid -> hence automatically modified to default value `ctrl+alt+e`")
    start_index = 0 if setting['file']['start_index'] is None or type(setting['file']['start_index']) is not int or \
                       setting['file']['start_index'] < 0 else setting['file']['start_index']
    end_index = len(link_list) if setting['file']['end_index'] is None or type(
        setting['file']['end_index']) is not int or \
                                  setting['file']['end_index'] <= start_index or setting['file']['end_index'] > len(
        link_list) else setting['file']['end_index']
    for ind in range(start_index, end_index):
        var = kb.add_hotkey(hotkey_1, open_web, args=(link_list[ind],))
        kb.wait(hotkey_2)
        kb.remove_hotkey(var)


if __name__ == '__main__':
    main()
