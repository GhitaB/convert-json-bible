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
