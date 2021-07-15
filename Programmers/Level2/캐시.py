def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    else:
        cache = list()
        time = 0

        for city in cities:
            city = city.lower()

            if city in cache:  # cache hit
                i = cache.index(city)
                cache.append(cache.pop(i))
                time += 1

            else:  # cache miss
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5

        return time
