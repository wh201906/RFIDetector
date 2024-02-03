import serial
import matplotlib.pyplot as plt

PORT = "xxx"
FREQ_START = 10000
FREQ_END = 9000000
FREQ_STEP = 10000

def getVal(freq):
    ser.write(str(freq).encode())
    return int(ser.readline().decode().strip())

ser = serial.Serial(PORT, 115200)
freqList = []
valueList = []

for freq in range(FREQ_START, FREQ_END + 1, FREQ_STEP):
    freqList.append(freq)
    value = getVal(freq)
    if len(valueList) > 0 and abs(value - valueList[-1]) > 20:
        value = getVal(freq) # try again
    print(f"freq:{freq}, value:{value}", flush=True)
    valueList.append(value)

plt.plot(freqList, valueList)
plt.show()

with open("output.csv", "a", encoding="utf-8") as f:
    f.write("freq,val\n")
    for i in range(len(freqList)):
        f.write(f"{freqList[i]},{valueList[i]}\n")
