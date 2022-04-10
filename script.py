import json

old_bible = []
new_bible = []
merged_bible = []

with open('ro-bible-old.json', encoding='utf-8-sig') as json_file:
    old_bible = json.load(json_file)
    # print(old_bible)
    print("Loaded old Bible.")

with open('ro-bible-new.json', encoding='utf-8-sig') as json_file:
    new_bible = json.load(json_file)
    # print(new_bible)
    print("Loaded new Bible.")

merged_bible = old_bible

translated_books = {
    'Genesis': 'Geneza',
    'Exodus': 'Exodul',
    'Leviticus': 'Leviticul',
    'Numbers': 'Numeri',
    'Deuteronomy': 'Deuteronomul',
    'Joshua': 'Iosua',
    'Judges': 'Judecători',
    'Ruth': 'Rut',
    '1 Samuel': '1 Samuel',
    '2 Samuel': '2 Samuel',
    '1 Kings': '1 Împăraţi',
    '2 Kings': '2 Împăraţi',
    '1 Chronicles': '1 Cronici',
    '2 Chronicles': '2 Cronici',
    'Ezra': 'Ezra',
    'Nehemiah': 'Neemia',
    'Esther': 'Estera',
    'Job': 'Iov',
    'Psalms': 'Psalmii',
    'Proverbs': 'Proverbe',
    'Ecclesiastes': 'Eclesiastul',
    'Song of Solomon': 'Cântarea cântărilor',
    'Isaiah': 'Isaia',
    'Jeremiah': 'Ieremia',
    'Lamentations': 'Plângerile lui Ieremia',
    'Ezekiel': 'Ezechiel',
    'Daniel': 'Daniel',
    'Hosea': 'Osea',
    'Joel': 'Ioel',
    'Amos': 'Amos',
    'Obadiah': 'Obadia',
    'Jonah': 'Iona',
    'Micah': 'Mica',
    'Nahum': 'Naum',
    'Habakkuk': 'Habacuc',
    'Zephaniah': 'Ţefania',
    'Haggai': 'Hagai',
    'Zechariah': 'Zaharia',
    'Malachi': 'Maleahi',
    'Matthew': 'Matei',
    'Mark': 'Marcu',
    'Luke': 'Luca',
    'John': 'Ioan',
    'Acts': 'Faptele apostolilor',
    'Romans': 'Romani',
    '1 Corinthians': '1 Corinteni',
    '2 Corinthians': '2 Corinteni',
    'Galatians': 'Galateni',
    'Ephesians': 'Efeseni',
    'Philippians': 'Filipeni',
    'Colossians': 'Coloseni',
    '1 Thessalonians': '1 Tesaloniceni',
    '2 Thessalonians': '2 Tesaloniceni',
    '1 Timothy': '1 Timotei',
    '2 Timothy': '2 Timotei',
    'Titus': 'Tit',
    'Philemon': 'Filimon',
    'Hebrews': 'Evrei',
    'James': 'Iacov',
    '1 Peter': '1 Petru',
    '2 Peter': '2 Petru',
    '1 John': '1 Ioan',
    '2 John': '2 Ioan',
    '3 John': '3 Ioan',
    'Jude': 'Iuda',
    'Revelation': 'Apocalipsa',
}


def get_text(b, c, v):
    c = str(c)
    v = str(v)
    for x in new_bible:
        if x['bookname'] == b and x['chapter'] == c and x['verse'] == v:
            return x['text']

    return "ERROR"


book_index = 1
for book in old_bible:
    book_name = book['name']
    # print(book_name)
    book_name_ro = translated_books[book_name]
    # print(book_name_ro)

    chapters = book['chapters']

    chapter_index = 1
    chapters_list = []
    for chapter in chapters:

        verse_index = 1
        verses_list = []
        for verse in chapter:
            new_text = get_text(book_name_ro, chapter_index, verse_index)

            if new_text == "ERROR":
                import pdb; pdb.set_trace()
            print(new_text)

            verses_list.append(new_text)
            verse_index += 1

        chapters_list.append(verses_list)
        chapter_index += 1

    merged_bible[book_index - 1]['chapters'] = chapters_list
    book_index += 1

with open('ro-bible-new-merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged_bible, f)
