from spellchecker import SpellChecker


# Get all the text from a list that contains nested lists
def get_text(lst):
    text = []
    for item in lst:
        if isinstance(item, list):
            text.extend(get_text(item))
        else:
            text.append(item)
    return list(set(text))  # Remove duplicate word


def trainTitleTextFile(arr):
    with open('src/resource/title.txt', 'w') as f:
        # เขียนซ้ำๆผ่านarrayเเล้วลงในไฟล์
        for item in arr:
            f.write(str(item) + '\n')


def trainDescriptionTextFile(arr):
    with open('src/resource/description.txt', 'w') as f:
        # เขียนซ้ำๆผ่านarrayเเล้วลงในไฟล์
        for item in arr:
            f.write(str(item) + '\n')


def title_auto_correct(query):
    spell = SpellChecker()
    spell.word_frequency.load_text_file('src/resource/title.txt')
    correctedquery = spell.correction(query)
    return correctedquery


def description_auto_correct(query):
    spell = SpellChecker()
    spell.word_frequency.load_text_file('src/resource/description.txt')
    correctedquery = spell.correction(query)
    return correctedquery
