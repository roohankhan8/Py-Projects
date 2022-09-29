# print('Enter one of these words: ')
print('noun')
print('pronoun')
print('verb')
print('adjective')

word = input('Enter one of these word: ')
dictionary = {
    'noun': 'a word (other than a pronoun) used to identify any of a class of people, places, or things ( common noun ), or to name a particular one of these ( proper noun ).',
    'pronoun': 'a word that can function as a noun phrase used by itself and that refers either to the participants in the discourse (e.g. I, you ) or to someone or something mentioned elsewhere in the discourse (e.g. she, it, this ).',
    'verb': 'a word used to describe an action, state, or occurrence, and forming the main part of the predicate of a sentence, such as hear, become, happen.',
    'adjective': 'a word naming an attribute of a noun, such as sweet, red, or technical'
}
# print(dictionary['noun'])
print(dictionary[word])
# print(word)
