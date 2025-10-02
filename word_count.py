from collections import Counter

def count_words(text):
    words = text.lower().split()
    return Counter(words)

# Example usage
sample = "Hello world hello hacker world"
print(count_words(sample))from collections import Counter

def count_words(text):
    words = text.lower().split()
    return Counter(words)

# Example usage
sample = "Hello world hello hacker world"
print(count_words(sample))
