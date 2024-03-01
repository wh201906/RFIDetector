import matplotlib.pyplot as plt

FILE_PATH_LIST = [
    "hardware/rev0.1/test_results/0.1_1mm_HF_LF4.7nF-HF0_10k-20M_10k.csv",
    "hardware/rev0.1/test_results/0.1_1mm_HF_LF4.7nF-HF22pF_10k-20M_10k.csv",
    "hardware/rev0.11/test_results/0.11_1mm_HF_LF4.7nF-HF0_10k-20M_10k.csv",
    "hardware/rev0.11/test_results/0.11_1mm_HF_LF4.7nF-HF22pF_10k-20M_10k.csv",
    "hardware/rev0.2/test_results/0.2_1.6mm_HF_LF6.8nF-HF0_10k-20M_10k.csv",
    "hardware/rev0.2/test_results/0.2_1.6mm_HF_LF6.8nF-HF22pF_10k-20M_10k.csv",
    "hardware/rev0.2/test_results/0.21_1.6mm_HF_LF6.8nF-HF0_10k-20M_10k.csv",
    "hardware/rev0.2/test_results/0.21_1.6mm_HF_LF6.8nF-HF22pF_10k-20M_10k.csv",
    "hardware/rev0.22/test_results/0.22_1.6mm_HF_LF8.8nF-HF0_10k-20M_10k.csv",
    "hardware/rev0.22/test_results/0.22_1.6mm_HF_LF8.8nF-HF22pF_10k-20M_10k.csv",
]

plotId = 1
for filePath in FILE_PATH_LIST:
    valueDict = {}
    with open(filePath, "r", encoding="utf-8") as f:
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
    plt.plot(freqList, valueList, label=str(plotId))
    plotId += 1

xRange = plt.xlim()
if xRange[0] <= 125000 <= xRange[1]:
    plt.axvline(x=125000, c="red", linestyle="--", label="125kHz")
if xRange[0] <= 134200 <= xRange[1]:
    plt.axvline(x=134200, c="green", linestyle="--", label="134.2kHz")
if xRange[0] <= 13560000 <= xRange[1]:
    plt.axvline(x=13560000, c="blue", linestyle="--", label="13.56MHz")

plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
plt.subplots_adjust(right=0.75)

plt.show()
