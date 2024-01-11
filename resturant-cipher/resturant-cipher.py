n = int(input())

if 1 <= n <= 20: # Constraints

    for i in range(n):
        secret_msg = input().strip()
        
        letter_count = {}
        for letter in secret_msg:
            if letter.isalpha() and letter.islower():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
                    
        max_count = 0
        max_letters = []
        for letter, count in letter_count.items():
            if count > max_count:
                max_count = count
                max_letters = [letter]
                
            elif count == max_count:
                max_letters.append(letter)
                
        max_letters.sort()
                
        if max_letters:
            print(max_letters[0].upper())