import json


def json_dumping(cur_dict) -> str:
    return json.dumps(cur_dict, indent=4, ensure_ascii=True)


def bytes_to_dict(byte_str) -> str:
    return json.loads(str(byte_str)[2:-1])


def pretty_html(html_text):
    return '\n'.join(list(filter(lambda x: bool(x.split()), html_text.split('\n'))))


def pretty_headers(headers):
    if headers:
        return json_dumping(dict(headers))
    else:
        return 'None'


def pretty_body(body: str):
    if body:
        if isinstance(body, bytes):
            return json_dumping(bytes_to_dict(body))
        else:
            try:
                return json_dumping(json.loads(body))
            except:
                return pretty_html(body)
    else:
        return 'None'
