import time


def check(expected, words):
    # all words that have the right length
    expected_dict = char_count(expected)
    max = sum(expected_dict.values())
    local_max = (0, None)
    for word in words:
        # determine the number of times each character appears in the word and in expected word
        word_dict = char_count(word)
        count = match(expected_dict, word_dict)
        if count > local_max[0]:
            local_max = (count, word)
        if count == max:
            return max, word
    return local_max


def match(expected_dict, word_dict):
    count = 0
    for char in expected_dict:
        if word_dict.get(char) is not None and word_dict.get(char) <= expected_dict.get(
            char
        ):
            count += word_dict.get(char)
    return count


def char_count(word):
    word_dict = {}
    for char in word:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    return word_dict


def largest_word(sorted_dict, expected):
    """
    for all words in sorted dictionary, check words with less than or the same number of letters if they contain
    the expected word or a substring of it
    """
    print(sorted_dict.keys())
    max, large_word = 0, None
    for i in sorted_dict:
        words = sorted_dict.get(i)
        num, word = check(expected, words)
        if num > max:
            max, large_word = num, word
    return large_word


def sort_dict(dictionary):
    """
    sort all words in list by number letters in word
    returns a dict with key/value of number of letters/ list of words with that number
    """
    sorted_dict = {}
    for word in dictionary:
        if len(word) in sorted_dict:
            sorted_dict[len(word)].append(word)
        else:
            sorted_dict[len(word)] = [word]
    return sorted_dict


start_time = time.time()

dictionary = [
    "Thasdfadsfasdfsadfsrgvevasdvasvaee",
    "largest",
    "adasfasdfsdvsdenomination",
    "of",
    "United",
    "States",
    "coin",
    "authorized",
    "by",
    "the",
    "The",
    "largest",
    "denomination",
    "of",
    "United",
    "States",
    "coin",
    "authorized",
    "by",
    "the",
    "The",
    "coin",
    "was",
    "immediately",
    "successful",
    "merchants",
    "and",
    "bdfasdfmfvdsanks",
    "used",
    "it",
    "in",
    "trade",
    "It",
    "was",
    "struck",
    "until",
    "replaced",
    "by",
    "the",
    "Saint",
    "Gaudens",
    "double",
    "eagle",
    "in",
    "1907",
    "and",
    "many",
    "were",
    "melted",
    "when",
    "President",
    "Franklin",
    "D",
    "Roosevelt",
    "recalled",
    "gold",
    "coins",
    "from",
    "the",
    "public",
    "in",
    "1933",
    "Millions",
    "of",
    "double",
    "eagles",
    "were",
    "sent",
    "overseas",
    "in",
    "international",
    "transactions",
    "throughout",
    "its",
    "run",
    "to",
    "be",
    "melted",
    "or",
    "placed",
    "in",
    "bank",
    "vaults",
    "Many",
    "of",
    "the",
    "latter",
    "have",
    "now",
    "been",
    "repatriated",
    "to",
    "feed",
    "the",
    "demand",
    "from",
    "collectors",
    "and",
    "those",
    "who",
    "desire",
    "to",
    "hold",
    "gold",
    "The",
    "largest",
    "of",
    "United",
    "Stadsfaates",
    "coin",
    "authorized",
    "by",
    "the",
    "Mint",
    "Act",
    "of",
    "1792",
    "was",
    "the",
    "eaglee",
    "or",
    "ten",
    "dollar",
    "piece",
    "The",
    "large",
    "amount",
    "of",
    "bullion",
    "being",
    "brought",
    "east",
    "after",
    "the",
    "discovery",
    "of",
    "gold",
    "in",
    "California",
    "in",
    "the",
    "1840s",
    "caused",
    "Congress",
    "to",
    "consider",
    "new",
    "denominations",
    "of",
    "gold",
    "coinage",
    "The",
    "gold",
    "dollar",
    "and",
    "double",
    "eagle",
    "were",
    "the",
    "result",
    "After",
    "considerable",
    "infighting",
    "at",
    "the",
    "Philadelphia",
    "Mint",
    "Chief",
    "Engraver",
    "James",
    "B",
    "Longacre",
    "designed",
    "the",
    "double",
    "eagle",
    "and",
    "it",
    "began",
    "to",
    "be",
    "issued",
    "for",
    "commerce",
    "in",
    "1850",
    "Only",
    "one",
    "1849",
    "double",
    "eagle",
    "is",
    "known",
    "to",
    "survive",
    "and",
    "it",
    "rests",
    "in",
    "the",
    "National",
    "Numismatic",
    "Collection",
    "at",
    "the",
    "Smithsonian",
    "",
]
# dogs','cat','dog',
expected = "eaee"
# create a dict key=len, values=words
sorted_dict = sort_dict(dictionary)
print(f"largest word: {largest_word(sorted_dict, 'ee')}")
print(f"largest word: {largest_word(sorted_dict, 'eaee')}")
print("--- %s seconds ---" % (time.time() - start_time))
