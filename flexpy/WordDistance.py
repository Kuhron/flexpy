# input_fp = "export-wordforms-2019-10-24.txt"
# with open(input_fp) as f:
#     lines = f.readlines()

# lines = [line.split("\t") for line in lines]
# lines = lines[1:]  # remove header row

# # keep only wordform and gloss
# lines = [line[:2] for line in lines]

# restrict to words with a gloss since there is a lot of extra stuff in there for some reason (incl. "oeuaoeu", which I cannot find in the database??)
#lines = [line for line in lines if line[1] != ""]

# print(lines[:5])


# copied from https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    # matrix = np.zeros ((size_x, size_y))
    matrix = [[0 for y in range(size_y)] for x in range(size_x)]
    for x in range(size_x):
        matrix [x][0] = x
    for y in range(size_y):
        matrix [0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1],
                    matrix[x][y-1] + 1
                )
            else:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1] + 1,
                    matrix[x][y-1] + 1
                )
    # print (matrix)
    return (matrix[size_x - 1][size_y - 1])


def normalized_levenshtein(x, y):
    d = levenshtein(x, y)
    max_d = max(len(x), len(y))
    return d / max_d


# def approx_word(w):
#     replacements = [
#         ["\u0301", ""], ["ː", ""], [":", ""], 
#         ["ɣ", "g"], ["β", "b"], ["ɛ", "e"], ["ɔ", "o"],
#         ["ɪ", "i"], ["ɨ", "i"], ["w", "u"], ["y", "i"], ["j", "i"],
#         ["ŋ", "n"], ["ɾ", "r"],
#     ]
#     for pair in replacements:
#         w = w.replace(pair[0], pair[1])
#     return w


# n_words = len(lines)
# mat = np.zeros((n_words, n_words))
# distances_dict = {}
# for i in range(n_words):
#     for j in range(i+1, n_words):
#         # duplicating and filling diagonal but good to be able to check (only constant multiple of 2 on runtime); VERIFIED
#         w1 = approx_word(lines[i][0])
#         w2 = approx_word(lines[j][0])
#         d = levenshtein(w1, w2)
#         mat[i, j] = d
#         if d not in distances_dict:
#             distances_dict[d] = []
#         distances_dict[d].append([lines[i], lines[j]])

# # assert mat[2, 2] == 0
# # assert mat[5, 5] == 0
# # assert mat[3, 2] == mat[2, 3]
# # assert mat[1, 6] == mat[6, 1]

# for d in range(0, 3):
#     print()
#     print("----\ndistance {}\n----".format(d))
#     for pair in distances_dict.get(d, []):
#         w1, g1 = pair[0]
#         w2, g2 = pair[1]
#         if w1 == w2 and (g1 == g2 or g1 == "" or g2 == ""):
#             continue
#         print("{} ({}) vs {} ({})".format(w1, g1, w2, g2))
#     print()


