from urllib.parse import urljoin
import q1_helper

base_url = "https://swapi.dev/api/"
vehicles_url = "vehicles/"
films_url = "films/"

ans_q1_1 = q1_helper.q1_1(urljoin(base_url, films_url))
ans_q1_2 = q1_helper.q1_2(urljoin(base_url, vehicles_url))
