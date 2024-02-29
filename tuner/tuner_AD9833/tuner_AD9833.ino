// Using AD9833 and Seeeduino XIAO for tuning
//
// 8: ADC_IN
// 2: SPI_CS(FSYNC)
// 1: SPI_SCK(SCLK)
// 0: SPI_MOSI(SDATA)
#include "AD9833.h"

AD9833 ad9833(2, 0, 1);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  SPI.begin();
  ad9833.begin();
  delay(10);
  ad9833.setFrequency(1000);
  ad9833.setWave(AD9833_SINE);
  Serial.println(ad9833.getWave());
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
  ad9833.setFrequency(freq);
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
