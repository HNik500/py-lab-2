def findlcs(x, y):
    m = len(x)  # Length of first string
    n = len(y)  # Length of second string
    c = [[0] * (n + 1) for _ in range(m + 1)]  # DP table initialization

    # Build DP table for LCS length
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # Characters match
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])  # Max of top or left cell

    # Reconstruct LCS from DP table
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:  # If characters match, add to LCS
            lcs_str.append(x[i - 1])
            i -= 1
            j -= 1
        elif c[i - 1][j] > c[i][j - 1]:  # Move up in table
            i -= 1
        else:  # Move left in table
            j -= 1

    return ''.join(reversed(lcs_str))  # Return LCS as a string


if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    result = findlcs(str1, str2)
    print("Longest Common Subsequence:", result)

