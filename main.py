with open('1.txt', 'rt', encoding='utf-8') as f1:
    text1 = f1.readlines()
with open('2.txt', 'rt', encoding='utf-8') as f2:
    text2 = f2.readlines()
with open('3.txt', 'rt', encoding='utf-8') as f3:
    text3 = f3.readlines()


def res_write(name_file, text):
    with open('result.txt', 'at', encoding='utf-8') as res:
        res.write(f'{name_file}\n')
        res.write(f'{str(len(text))}\n')
        for line in text:
            res.write(line)
        res.write('\n')


if len(text1) < len(text2) < len(text3):
    res_write('1.txt', text1)
    res_write('2.txt', text2)
    res_write('3.txt', text3)
elif len(text1) < len(text3) < len(text2):
    res_write('1.txt', text1)
    res_write('3.txt', text3)
    res_write('2.txt', text2)
    #     text = text1+text3+text2
elif len(text2) < len(text1) < len(text3):
    res_write('2.txt', text2)
    res_write('1.txt', text1)
    res_write('3.txt', text3)
    #     text = text2+text1+text3
elif len(text2) < len(text3) < len(text1):
    res_write('2.txt', text2)
    res_write('3.txt', text3)
    res_write('1.txt', text1)
    #     text = text2+text3+text1
elif len(text3) < len(text1) < len(text2):
    res_write('3.txt', text3)
    res_write('1.txt', text1)
    res_write('2.txt', text2)
    #     text = text3+text1+text2
elif len(text3) < len(text2) < len(text1):
    res_write('3.txt', text3)
    res_write('2.txt', text2)
    res_write('1.txt', text1)
    #     text = text3+text2+text1
