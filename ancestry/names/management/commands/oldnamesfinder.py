

def lastnames(path):
    with open(path, 'r') as f:
        return f.read()


ronaldbrown = lastnames('ronald_brown.txt').lower()
lloydlacey = lastnames('lloydlacey.txt').lower()

cousins = [ronaldbrown, lloydlacey]

text_data = re.findall(r'title="[a-zA-Z]* +[a-zA-Z]* +[a-zA-Z]*', cousins[0])
text_data = [e[7::] for e in text_data]

text_data2 = re.findall(r'title="[a-zA-Z]* +[a-zA-Z]* +[a-zA-Z]*', cousins[1])
text_data2 = [e[7::] for e in text_data2]
data = []
data2 = []



def test(txtdta):
    datas = []
    for datum in txtdta:
        datas.append(datum)
        if datum == 'Non members cannot' or \
                datum == 'If you contact' or \
                datum == 'Review DNA Matches' or \
                datum == 'MyHeritage blog ' or \
                datum == 'MyHeritage privacy policy' or \
                datum == 'MyHeritage terms and' or datum == 'Have a question':
            datas.remove(datum)
    # print(datas)
    return datas

data = str(test(text_data))
data2 = str(test(text_data2))

data = list(data.split(","))
data2 = list(data2.split(","))


# for datum in text_data:
#     data.append(datum)
#     if datum == 'Non members cannot' or \
#             datum == 'If you contact' or \
#             datum == 'Review DNA Matches' or \
#             datum == 'MyHeritage blog ' or \
#             datum == 'MyHeritage privacy policy' or \
#             datum == 'MyHeritage terms and' or datum == 'Have a question':
#         data.remove(datum)

# data.append('TEST')
# data.append('MORETESTING')

#
# data2 = []
# for datum2 in text_data2:
#     data2.append(datum2)
#     if datum2 == 'Non members cannot' or \
#             datum2 == 'If you contact' or \
#             datum2 == 'Review DNA Matches' or \
#             datum2 == 'MyHeritage blog ' or \
#             datum2 == 'MyHeritage privacy policy' or \
#             datum2 == 'MyHeritage terms and' or datum2 == 'Have a question':
#         data2.remove(datum2)
# print(data2)
data2.append('TEST, moretesting')
data.append('TEST, moretesting')
print(f'+++++++++ {data} + +++++++++++')
print(f'+++++++++ {data2} + ++++++++++')

newlist = []
for item in data:
    for item1 in data2:
        if item == item1:
            newlist.append(item)
            print(f'These are the names they have in common {newlist}')


