import json

import wikipedia as wiki


class Cities:
    def __init__(self, file):
        self.file = file

    def cities_list(self):
        cities_list = []
        with open(self.file, 'r') as f:
            cities = json.loads(f.read())
            for i in range(len(cities)):
                cities_list.append(cities[i]['name']['common'])
        return cities_list


class CityIterator:
    def __init__(self, file_name):
        c = Cities(file_name)
        self.city = c.cities_list()
        self.count = 0

    def __next__(self):
        if self.count < len(self.city):
            city = self.city[self.count]
            try:
                self.count += 1
                return wiki.page(city).url
            except Exception:
                print("City Not Found")
        else:
            raise StopIteration


if __name__ == '__main__':
    city_iterator = CityIterator("countries.json")
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
