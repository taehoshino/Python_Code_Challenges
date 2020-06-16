import re

# def is_palindrome(text):
#     cleaned_text = "".join(e for e in text if e.isalnum()).lower()
#     for i in range(0, int(len(cleaned_text)/2)+1):
#         if cleaned_text[i] == cleaned_text[-1-i]:
#             pass
#         else:
#             return False
#     return True


def is_palindrome(text):
    forwards = "".join(re.findall(r"[a-z]+", text.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(is_palindrome("Go hang a salami - I'm a lasagna hog"))
