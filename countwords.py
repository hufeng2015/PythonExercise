import string

path = 'Walden.txt'
with open(path, 'r') as text:
    #读出来的文字去掉标点符号并且全部转换为小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    #set化去重并且排序
    words_index = set(words)
    #循环生成dict key为文字 value为文字出现的次数
    counts_dict = {index: words.count(index) for index in words_index}
    print(words)
    #按照value排序，并且返回key的列表
    for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
        print(f'这个【{word}】词出现了【{words.count(word)}】次')
