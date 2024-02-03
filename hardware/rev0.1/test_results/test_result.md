# Test Result

1. Both the LF circuit and the HF circuit are working.
2. The capacity of tuning capacitor for the LF antenna is around 4.7nF.
3. The inductance of the HF antenna is too high so the best performance is achieved with no tuning capacitor.
4. Most PCB manufactors claim the minimum width from trace to outline is less than 0.3mm, but the physical prototype of Rev 0.1 shows it's risky to set it to 0.3mm.
5. The sensing distance doesn't get increased a lot by using high-capacity capacitor in the voltage multiplier circuit.
6. Capacitors in the voltage multiplier with higher capacity introduce a longer response time to the change in distance. This is noticeable when the capacity is over 47uF.
7. It's still unclear how many stages in the voltage multiplier brings the longest sensing distance. The distance is affected by both the voltage multiplier and the tuning circuit, so I need to finalise the antenna design then test the voltage multiplier.
