def get_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    character_dict = {}
    character_list = []
    def sort_on(dict): return dict["num"]
    
    for letter in file_contents:
        letter = letter.lower()
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1

    for key, value in character_dict.items():  
        character_list.append({"char": key, "num": value})
        
    character_list.sort(reverse=True, key=sort_on)
      

    return character_list


