import sys

def get_word_count(stri):
    words = stri.split(" ")
    word_count = 0
    for word in words:
        has_alphanum = False
        for ch in word:
            if ch.isalnum():
                has_alphanum = True
                break
        if has_alphanum:
            word_count += 1
    return word_count

response = sys.argv[1]
print(f"That response is {get_word_count(response)} words.")

