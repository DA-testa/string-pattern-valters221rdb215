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

    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = sum([ord(c) for c in pattern])
    text_hash = sum([ord(c) for c in text[:pattern_len]])

    for i in range(0, text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_len]:
            yield i

        if i < text_len - pattern_len:
            text_hash -= ord(text[i])
            text_hash += ord(text[i+pattern_len])

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
