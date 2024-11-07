from pdb import set_trace as stx

# word = "internationalization"
# abbr = "i5a11o1"

word = "hi"
abbr = "hi1"
# abbr = "2"
# abbr = "2i"

# word = 'word'
# abbr = '2'

is_abbr = True              # 把 abbr 中的数字展开
word_idx = 0
i = 0
while i < len(abbr) and word_idx < len(word):
    # 当前的字符要么是数字，要么是字母
    if abbr[i] <= 'z' and abbr[i] >= 'a':
        if abbr[i] != word[word_idx]:
            is_abbr = False
            break
        else:
            word_idx += 1
            i += 1
            continue
    if abbr[i] == '0':
        is_abbr = False
        break
    if '2' <= abbr[i] and abbr[i]  <= '9':
        if i < len(abbr) - 1:
            if '0' <= abbr[i+1] and abbr[i+1] <= '9':
                is_abbr = False
                break
        word_idx += int(abbr[i])
        i += 1
        if word_idx > len(word):
            is_abbr = False
            break
        if word_idx == len(word):
            if i != len(abbr):
                is_abbr = False
                break
        continue
    if abbr[i] == '1' :
        if i < len(abbr) - 1:
            if '0' <= abbr[i+1] and abbr[i+1] <= '9':
                two_digit_num = int(abbr[i:i+2])
                if i < len(abbr) - 2:
                    if '0' <= abbr[i+2] and abbr[i+2] <= '9':
                        is_abbr = False
                        break
                word_idx += int(two_digit_num)
                i += 2
                if word_idx > len(word):
                    is_abbr = False
                    break
                if word_idx == len(word):
                    if i != len(abbr):
                        is_abbr = False
                        break
                continue
            else:
                word_idx += 1
                i += 1
                if word_idx > len(word):
                    is_abbr = False
                    break
                if word_idx == len(word):
                    if i != len(abbr):
                        is_abbr = False
                        break
                continue
        else:
            # stx()
            word_idx += 1
            i += 1
            if word_idx != len(word):
                is_abbr = False
                break
            break

# stx()

if word_idx != len(word) or i != len(abbr):
    is_abbr = False


print(is_abbr)