def length_of_longest_substring(s: str) -> int:
    l = 0
    longest = 0
    sett = set()

    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        sett.add(s[r])
        longest = max(longest, r - l + 1)

    return longest

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_string>")
    else:
        input_str = sys.argv[1]
        result = length_of_longest_substring(input_str)
        print(f"Length of longest substring without repeating characters: {result}")
