// Using AD9851 and Seeeduino XIAO for tuning
//
// 0: W_CLK
// 1: FQ_UD
// 2: DATA(D7)
// 3: RESET
// 5: CS(dummy pin)
// 8: ADC_IN
#include "AD985X.h"

AD9851 ad9851(5, 3, 1, 2, 0);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  ad9851.begin();
  ad9851.powerUp();
  delay(10);
  ad9851.setAutoRefClock(false);
  ad9851.setRefClockHigh();
  ad9851.setFrequency(1000);
  analogReadResolution(12);
}

void loop() {
  if (!Serial.available()) {
    return;
  }
  float freq = Serial.parseFloat();
  while (Serial.available()) {
    Serial.read();
  }
  ad9851.setFrequency(freq);
  delayMicroseconds(100);
  int maxVal = 0;
  for (int i = 0; i < 1000; i++) {
    // It works as long as the period there is not the multiple of the waveform's period.
    // The period there is a little bit longer than 1us, which is expected.
    int val = analogRead(8);
    // SAMD21 ADC max speed: 350ksps -> 2.86us
    delayMicroseconds(3);
    maxVal = val > maxVal ? val : maxVal;
  }
  Serial.println(maxVal);
}
