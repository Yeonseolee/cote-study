sent = input()
keyword = input()

sent_ = ''
for word in sent:
    if not word.isdigit():
        sent_+=word

if keyword in sent_:
    print(1)
else:
    print(0)
