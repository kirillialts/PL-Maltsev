text = input('введите строку:')
len_text = len(text)
len_text_2 = len_text//2
new_text = ''
for i in range(len_text):
    if i < len_text_2 and text[i].lower() == 'п':  
        new_text += '*'
    else:
        new_text += text[i]
print(new_text)