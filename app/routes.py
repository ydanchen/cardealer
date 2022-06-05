from flask import request, abort

from app import app
from app.controller import get_cars, get_car_by_id, store_car, delete_car, get_dealers, delete_dealer, store_dealer
from app.data.models import Car, Dealer, is_valid
from app.utils import json_response

SC_OK = 200
SC_CREATED = 201
SC_BAD_REQUEST = 400
SC_NOT_FOUND = 404


@app.errorhandler(SC_NOT_FOUND)
def not_found(error):
    return json_response({'error': 'Not found'}, SC_NOT_FOUND)


@app.errorhandler(SC_BAD_REQUEST)
def bad_request(error):
    return json_response({'error': 'Bad request'}, SC_BAD_REQUEST)


@app.route("/dealers", methods=["GET"])
def list_dealers():
    return json_response(get_dealers())


@app.route("/dealers", methods=["POST"])
def add_dealer():
    json = request.get_json()
    if is_valid(Dealer(), json):
        store_dealer(Dealer(**json))
        return json_response({'result': 'Success'}, SC_CREATED)
    else:
        abort(SC_BAD_REQUEST)


@app.route("/dealers/<int:dealer_id>", methods=["DELETE"])
def remove_dealer(dealer_id: int):
    delete_dealer(dealer_id)
    return json_response({'result': 'Success'}, SC_OK)


@app.route("/cars", methods=["GET"])
def list_cars():
    color_filter = request.args.get("color")
    model_filter = request.args.get("model")
    return json_response(get_cars(color_filter, model_filter))


@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id: int):
    car = get_car_by_id(car_id)
    return json_response(car[0]) if len(car) > 0 else abort(SC_NOT_FOUND)


@app.route("/cars", methods=["POST"])
def add_car():
    json = request.get_json()
    if is_valid(Car(), json):
        store_car(Car(**json))
        return json_response({'result': 'Success'}, SC_CREATED)
    else:
        abort(SC_BAD_REQUEST)


@app.route("/cars/<int:car_id>", methods=["DELETE"])
def remove_car(car_id: int):
    delete_car(car_id)
    return json_response({'result': 'Success'}, SC_OK)
