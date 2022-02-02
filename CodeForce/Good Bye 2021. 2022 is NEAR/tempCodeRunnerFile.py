    for i in range(n):
            for letter in letters:
                if s[i] in letter:
                    ansl.append(s[i])
                    ansr.append(s[i])
                    letter.remove(s[i])
    