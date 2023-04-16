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
            print("File doesnt exist")
            exit()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    patternLength = len(pattern)
    textLength = len(text)
    patternHash = sum([ord(c) for c in pattern])
    textHash = sum([ord(c) for c in text[:patternLength]])

    for i in range(0, textLength - patternLength + 1):
        if patternHash == textHash and pattern == text[i:i+patternLength]:
            yield i

        if i < textLength - patternLength:
            textHash -= ord(text[i])
            textHash += ord(text[i+patternLength])

            
        
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
