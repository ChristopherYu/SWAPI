from datetime import datetime
import requests
import json


class Result:
    def __init__(self, film_info):
        self.episode_id = film_info["episode_id"]
        self.title = film_info["title"]
        self.release_date = film_info["release_date"]


def q1_1(url: str) -> list:
    response = requests.get(url)
    data = json.loads(response.text)
    films = data["results"]
    result = [Result(film_info) for film_info in films]
    result.sort(key=lambda d: datetime.strptime(d.release_date, "%Y-%m-%d"))
    return result


def q1_2(url: str) -> list:
    response = requests.get(url)
    data = json.loads(response.text)
    vehicles = data["results"]
    result = [vehicle_info for vehicle_info in vehicles if int(vehicle_info["passengers"]) == 0]
    return result
