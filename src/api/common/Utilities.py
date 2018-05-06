import json


def validate_payload(payload_to_validate):
    if payload_to_validate is [None, '', 'null']:
        return False
    else:
        return True


def validate_required_fields(fields_to_validate, payload):
    dict_payload = payload if payload is dict else json.loads(payload)
    if all(key in dict_payload for key in fields_to_validate):
        return True
    else:
        return False