[[chr((j + i - ord(chr_s)) % (ord(chr_e) - ord(chr_s) + 1) + ord(chr_s))
            for j in range(ord(chr_s), ord(chr_e) + 1)]
            for i in range(ord(chr_e) - ord(chr_s) + 1)]