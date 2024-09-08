import json


def json_dumping(cur_dict) -> str:
    return json.dumps(cur_dict, indent=4, ensure_ascii=True)
