# planet = 'pluto'
# pluto_mass = 1.303 * 10**22
# earth_mass = 5.9722 * 10**24
# population = 52910390
# #         2 decimal points   3 decimal points, format as percent     separate with commas
# print("{} weighs about {:.2} kilograms ({:.4%} of Earth's mass). It is home to {:,} Plutonians.".format(
#     planet, pluto_mass, pluto_mass / earth_mass, population,
# ))
#
#
#
# s = """Pluto's a {0}.
# No, it's a {1}.
# {0}!
# {1}!""".format('planet', 'dwarf planet')
# print(s)
#
#
# dic = {i:i*i for i in range(100) if i*i > 1000}
# print(dic)
# print(len(dic))
#
# strss = '123e10'
# print(strss.isnumeric())




def word_search(documents, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = []
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(documents, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0], 'they': [1]}
    """
    return {keyword:word_search(documents,keyword) for keyword in keywords }

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print(word_search(doc_list,'casino'))

keywords = ['casino', 'they']
print(multi_word_search(doc_list,keywords))