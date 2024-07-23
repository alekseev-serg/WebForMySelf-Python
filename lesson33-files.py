# f = open('file.txt', encoding='utf-8')
# text = f.read(2)
# text2 = f.read(8)
# text = f.read()
# f.close()


# print(text)
# print(text2)
# print(text)


# fr = open('file.txt', 'a', encoding='utf-8')
# fr.write('Hello World\n')
# fr.close()

# lines = ['New string 1', 'New string 2', 'New string 3']
# fq = open('file.txt', 'a', encoding='utf-8')
# fq.write('\n'.join(lines))
# fq.writelines(lines)
# fq.writelines(f'{i}\n' for i in lines)
# fq.close()

fw = open('file.txt', 'r', encoding='utf-8')
for line in fw:
    print(line, end='')
fw.close()
