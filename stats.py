def count_words(text):
    count = 0
    for i in text.split():
        count += 1    
    
    return f"Found {count} total words"

def count_characters(text):
    count = {}
    lower_case_text = text.lower()
    
    for char in lower_case_text:
        if not char.isalpha():
            continue
        elif char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return count

def convert_dict_to_list(count_char):
    my_list = []
    for char, value in count_char.items():
        #create a new dict to sort as a list
        my_dict = {"char" : char, "value" : value }
        my_list.append(my_dict)
    return my_list

def sort_on(dict):
    return dict["value"]

def sorted_list(list_of_dict):
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def chars_to_sorted_list(char_dict):
    list_of_dict = convert_dict_to_list(char_dict)
    sorted_result = sorted_list(list_of_dict)
    return sorted_result