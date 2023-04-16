# python3

def read_input():
    mode = input().strip()

    if mode == "I":
        pattern = input().strip()
        text = input().strip()
    elif mode == "F":
        with open("./tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        raise ValueError("Invalid input mode")
    
    return pattern, text


def print_occurrences(output):
    for i in output:
        print(i, end=' ')
    print()

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(10, pattern_len - i - 1) for i in range(pattern_len))
    text_hash = sum(ord(text[i]) * pow(10, pattern_len - i - 1) for i in range(pattern_len))
    occurrences = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = text_hash - ord(text[i]) * pow(10, pattern_len - 1)
            text_hash = text_hash * 10 + ord(text[i + pattern_len])

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
