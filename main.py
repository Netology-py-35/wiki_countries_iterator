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

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > len(self.city):
            raise StopIteration
        else:
            try:
                city = self.city[self.count]
                self.count += 1
                return wiki.page(city).url
            except:
                return 'City Not Found'


if __name__ == '__main__':
    for item in CityIterator("countries.json"):
        print(item)
