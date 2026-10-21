import random

input = None  
def noise_maker (input, k_case : int | None):
    base_case = str(input)
    if not k_case:
        k_case = 50
    
    stripped_input = base_case.strip(" ")
    
    list_choices = ["normal", _typo, "swap", "nospace"]
    weights = [40,20,20,20]
    
    for i in range(k_case):
        random.choices(list_choices,
                       weights = weights,
                    #    k = num_cases
        )
        
        if list_choices == "normal":
            yield base_case
        elif list_choices == _typo:
            yield None
        elif list_choices == "swap":
            yield None
        elif list_choices == "nospace":
            yield None


LAYOUT  = {
          'q': (0,0), 'w': (0,1), 'e': (0,2), 'r': (0,3), 't': (0,4), 'y': (0,5), 'u': (0,6), 'i': (0,7), 'o': (0,8), 'p': (0,9),
    'a': (1,0), 's': (1,1), 'd': (1,2), 'f': (1,3), 'g': (1,4), 'h': (1,5), 'j': (1,6), 'k': (1,7), 'l': (1,8),
    'z': (2,0), 'x': (2,1), 'c': (2,2), 'v': (2,3), 'b': (2,4), 'n': (2,5), 'm': (2,6)
    }
    
 
def _typo (text):
    #manual map 
    
    valid_indices = []
    for index, char in enumerate(text):
        if char.lower() in LAYOUT:
            valid_indices.append(index)
            
            
    if not valid_indices:
        return text
    
    target_idx = random.choices(valid_indices)[0]
    
    original_char = text[target_idx]
    
    neighbors, weights = get_typo_char(original_char.lower())
    
    if not neighbors:
        return text
    
    
    new_char = random.choices(neighbors, weights = weights, k=1)[0]
    
    if original_char.isupper():
        new_char = new_char.upper()
        
    return text[:target_idx] + new_char + text[target_idx + 1:]


def get_typo_char(char): 
    
    r1, c1 = LAYOUT[char]
    neighbors = []
    weights = []
    
    for key, (r2, c2) in LAYOUT.items():
        if key == char:
            continue
        
        dr = abs(r1-r2)
        dc = abs(c1-c2)
        if dr <= 1 and dc <= 1:
            neighbors.append(key)
            
            if dr == 0:
                weights.append(3)
            else:
                weights.append(1)
        
    return neighbors, weights


result = _typo("what are you doing")
print(result)


