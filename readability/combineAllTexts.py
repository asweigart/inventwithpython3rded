#! python3
fullText = []

for i in range(1, 5):
    fp = open('chapter%s.txt' % i, encoding='UTF=8')
    fullText.append(fp.read())
    fp.close()

fp = open('fullText.txt', 'w', encoding='UTF-8')
fp.write('\n\n'.join(fullText))
fp.close()