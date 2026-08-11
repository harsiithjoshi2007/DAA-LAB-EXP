"""Experiment 2: String matching algorithms comparison."""


def naive_string_match(text: str, pattern: str):
    matches = []
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            matches.append(i)
    return matches


def rabin_karp_match(text: str, pattern: str):
    matches = []
    n, m = len(text), len(pattern)
    if m == 0:
        return matches

    base = 256
    mod = 101
    pattern_hash = 0
    text_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        text_hash = (base * text_hash + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i : i + m] == pattern:
                matches.append(i)

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % mod

    return matches


def compute_lps(pattern: str):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_match(text: str, pattern: str):
    matches = []
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def demo():
    text = "ABABABCAABABABABAB"
    pattern = "ABABAB"

    print("Experiment 2: String Matching Algorithms")
    print("Text:", text)
    print("Pattern:", pattern)

    print("Naive:", naive_string_match(text, pattern))
    print("Rabin-Karp:", rabin_karp_match(text, pattern))
    print("KMP:", kmp_match(text, pattern))


if __name__ == "__main__":
    demo()
