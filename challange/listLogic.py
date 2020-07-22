word = input("Enter an a-zA-Z word that typed with 10 fingers : ").strip().lower()

word_list = list(word)
letters_list = list("qwertasdfgzxcvbyuiophjklnm")

left_letters_list = letters_list[:15]
right_letters_list = letters_list[15:]

left_exist = False
right_exist = False

for i in range(0, len(word_list)):
    if word_list[i] in left_letters_list and word_list[i] not in right_letters_list:
        left_exist = True
    elif word_list[i] not in left_letters_list and word_list[i] in right_letters_list: 
        right_exist = True
    else:
        print("Not Covered Letter")


if(left_exist and right_exist):
    print("True")        
else:
    print("False")