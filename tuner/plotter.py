import matplotlib.pyplot as plt

FILE_PATH = "hardware/rev0.1/test_results/lf_4.7nf.csv"

valueDict = {}
with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line in f.readlines():
        firstChar = ord(line[0])
        if firstChar < ord("0") or firstChar > ord("9"):
            continue

        freq, value = line.strip().split(",")
        # new value will override the old one
        valueDict[int(freq)] = int(value)

freqList, valueList = zip(*sorted(valueDict.items()))
# print(freqList)
# print(valueList)
plt.plot(freqList, valueList)
plt.show()
