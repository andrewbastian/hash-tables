from collections import defaultdict

def word_count(s):
    ignore = ',":;,.-+=/\\|[]{}()*^&'
    counter = defaultdict(int)

    clean_up = s.translate(str.maketrans('','', ignore))

    for i in clean_up.lower().split():
        counter[i] += 1

    return counter

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))