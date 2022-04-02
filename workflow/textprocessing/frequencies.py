def calculate_frequencies(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))

    return result
