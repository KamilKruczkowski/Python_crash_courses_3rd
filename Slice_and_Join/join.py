text = ['Hello', 'python', 'world' '!']
print(f"Original text: {text}")
new_text = ' '.join(text)
print(f" Joined text: {new_text}")
print()

url = ['www', 'example', 'com']
print(f"Original url: {url}")
new_url = '.'.join(url)
print(f"Joined url: {new_url}")
print()

phone = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Original phone: {phone}")
phone_str = [str(num) for num in phone]
print(f"Original list of strings phone {phone_str}")
area_code = "".join(phone_str[:3])
second_part = "".join(phone_str[3:6])
last_part = "".join(phone_str[6:])
print(f"Correct phone number is: ({area_code}) {second_part}-{last_part}")
print()

def reverse_string(s):
    return ''.join(reversed(s))
text_2 = 'Here comes an example'
print(f"Original text: {text_2}")
print(f"Reversed text: {reverse_string(text_2)}")
print()

words = ['apple', 'plum', 'banana', 'raspberry', 'cherry', 'kiwi']
print(f"Original words: {words}")
long_words = [word for word in words if len(word) > 5]
result = ', '.join(long_words)
print(f"Words longer than 5 letters: {result}")