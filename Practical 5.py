import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng') 

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform POS Tagging
pos_tags = pos_tag(words)

# Display result
print("Input Sentence:\n", sentence)
print("\nPOS Tagging Result:\n", pos_tags)

# Display with explanations
print("\nPOS Tags with Explanations:")
for word, tag in pos_tags:
    tag_meaning = {
        'DT': 'Determiner',
        'JJ': 'Adjective',
        'NN': 'Noun',
        'VBZ': 'Verb (3rd person singular present)',
        'IN': 'Preposition',
        '.': 'Punctuation mark'
    }.get(tag, tag)
    print(f"{word:8} -> {tag:4} ({tag_meaning})")
