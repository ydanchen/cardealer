import json

from app import app


def json_response(data, status=200) -> app.response_class:
    return app.response_class(
        response=json.dumps(data, default=lambda x: x.__dict__, indent=2, sort_keys=True),
        status=status,
        mimetype='application/json')
