word = set(input("Enter an a-zA-Z word that typed with 10 fingers : ").strip().lower())
# print(word)
left_finger_keys = set("qwertasdfgzxcvb")
right_finger_keys = set("yuiophjklnm")
# all_keys = set("qwertasdfgzxcvbyuiophjklnm")

if word.intersection(left_finger_keys) and not word.intersection(right_finger_keys) or word.intersection(right_finger_keys) and not word.intersection(left_finger_keys):
    print(False)
else:
    print(True)
