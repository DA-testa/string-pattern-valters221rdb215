# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 10**9+7
    x = 31
    occurrences = []
    p_hash = 0
    t_hash = 0
    x_power = 1

    for i in range(len(pattern)):
        p_hash = (p_hash*x + ord(pattern[i])) % p
        x_power = (x_power*x) % p

    for i in range(len(pattern)):
        t_hash = (t_hash*x + ord(text[i])) % p
        x_power = (x_power*x) % p

    for i in range(len(text)-len(pattern)+1):
        if p_hash == t_hash:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
                
        if i+len(pattern) < len(text):
            t_hash = (t_hash - ord(text[i])*x_power) % p
            t_hash = (t_hash*x + ord(text[i+len(pattern)])) % p
            if t_hash < 0:
                t_hash += p

    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
