curse = ['darn', 'dang', 'freakin', 'heck', 'shoot']
text = "Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freakin try".split(
    ' ')

count = 0
for i in range(len(text)):
    for j in range(len(curse)):
        if text[i].lower() == curse[j].lower():
            text[i] = '*'*len(curse[j])

print(' '.join(text))
