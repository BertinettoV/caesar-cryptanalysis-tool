import string
from collections import Counter

choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

if choice == 'e':
    message = input("Enter a message (only letters): ")
    shift = int(input("Enter a shift value (1-25): "))

    def prep(message):
        m = message.replace(" ", "")
        return m

    def encrypt(m, shift):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        c = ""
        for i in range(len(m)):
            if m[i].isupper(): 
                c += upper[(upper.index(m[i]) + shift) % 26]
            elif m[i].islower():
                c += lower[(lower.index(m[i]) + shift) % 26]
        return c    

    print(encrypt(prep(message), shift))

elif choice == 'd':
    
    lang = input("Enter language (en/it): ").lower()

    en_freq = {
        'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 13.0, 'F': 2.2, 'G': 2.0,
        'H': 6.1, 'I': 7.0, 'J': 0.2, 'K': 0.8, 'L': 4.0, 'M': 2.4, 'N': 6.7,
        'O': 7.5, 'P': 1.9, 'Q': 0.1, 'R': 6.0, 'S': 6.3, 'T': 9.1, 'U': 2.8,
        'V': 1.0, 'W': 2.4, 'X': 0.2, 'Y': 2.0, 'Z': 0.1
        }

    it_freq = {
        'A': 11.7, 'B': 0.9, 'C': 4.5, 'D': 3.7, 'E': 11.8, 'F': 1.1, 'G': 1.6,
        'H': 0.6, 'I': 11.3, 'J': 0.0, 'K': 0.0, 'L': 6.5, 'M': 2.5, 'N': 7.0,
        'O': 9.8, 'P': 3.0, 'Q': 0.5, 'R': 6.4, 'S': 4.9, 'T': 5.6, 'U': 3.0,
        'V': 2.1, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 1.5
    }


    en_words = ["the", "and", "of", "to", "in", "that", "is", "it", "you"]
    it_words = ["che", "non", "per", "una", "con", "gli", "del", "sono", "come"]

    # Dictionary check
    def score_dictionary(candidate):
        words = en_words if lang == "en" else it_words
        candidate_lower = candidate.lower()
        return sum(word in candidate_lower for word in words)

    # Frequency check
    def letter_frequency(text):
        text = text.upper()
        counts = Counter(ch for ch in text if ch.isalpha())
        total = sum(counts.values())
        return {ch: (counts[ch] / total * 100) for ch in counts} if total > 0 else {}

    def score_frequency(candidate):
        freq_table = en_freq if lang == "en" else it_freq
        candidate_freq = letter_frequency(candidate)
        score = 0
        for ch in freq_table:
            score += (candidate_freq.get(ch, 0) - freq_table[ch]) ** 2
        return score  # lower = closer

    def evaluate_candidate(candidate):
        freq_w=0.5  # weight of frequency check
        dict_w=0.5  # weight of dictionary check
        dict_hits = score_dictionary(candidate)
        freq_score = score_frequency(candidate)

        combined_score = freq_w * freq_score + dict_w * (1 / (1 + dict_hits))
        return combined_score


    ciphertext = input("Enter message: ")

    def prep(ciphertext):
        c = ciphertext.replace(" ", "")
        return c

    def decrypt(c):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase 

        for i in range(1, 26):
            trans = str.maketrans(
            upper + lower,
            upper[-i:] + upper[:-i] +
            lower[-i:] + lower[:-i]
        )

        maintext = c.translate(trans)

        score = evaluate_candidate(maintext)
        print(f"{i}  : {maintext} - {score:.3f}")

    decrypt(prep(ciphertext))










