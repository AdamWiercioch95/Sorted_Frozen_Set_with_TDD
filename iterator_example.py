items = [1, 2, 3]


list_iterator = iter(items)

# print(list_iterator)

# for item in list_iterator:
#     print(item)


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration

        result = self.data[self.idx]
        self.idx += 1
        return result


class MyIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return MyIterator(self.data)


m = MyIterable()
mi = iter(m)

# print(mi)
# print(next(mi))
# print(next(mi))
# print(next(mi))

# for e in MyIterable():
#     print(e)


continents = {
    'asia': {
        'china': 'pekin',
        'japan': 'tokyo',
    },
    'europe': {
        'poland': 'warsaw',
        'spain': 'madrid',
        'hungary': 'budapest',
    }
}


class ContinentsIterator:
    def __init__(self, data):
        self._data = self._parse_data(data)
        self._idx = 0

    @staticmethod
    def _parse_data(data):
        return sorted(city for country in data.values() for city in country.values())

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._data):
            raise StopIteration('No more countries!')

        result = self._data[self._idx]
        self._idx += 1

        return result


# for i in ContinentsIterator(continents):
#     print(i)

# country2 = ContinentsIterator(continents)
# print(country2 == iter(country2))
#
# print(next(country2))
# print(next(country2))
# print(next(country2))
# print(next(country2))
# print(next(country2))
# print(next(country2))




