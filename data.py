#data
#заполнение словаря из базы данных
with open('country_info.txt', 'r') as file:
    countryInfo = {}
    for line in file:
        word = line.split()
        countryInfo[word[0]] = float(word[1])
    #print(countryInfo)
