# python3
def read_input():
    mode = input().strip()

    if mode not in ['F', 'I']:
        raise ValueError("Invalid input. Press I or F")

    if mode == "I":
        pattern = input().strip()
        text = input().strip()
    else:
        try:
            with open("./tests/06") as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        except FileNotFoundError:
            print("File not found.")
            exit()

    return pattern, text




def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    
     
        
        
def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = sum([ord(c) for c in pattern])
    text_hash = sum([ord(c) for c in text[:pattern_len]])

    for i in range(1, text_len - pattern_len + 2):
        if pattern_hash == text_hash and pattern == text[i-1:i-1+pattern_len]:
            yield i-1

        if i < text_len - pattern_len + 1:
            text_hash -= ord(text[i-1])
            text_hash += ord(text[i+pattern_len-1])

    return list(get_occurrences(pattern, text))



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
