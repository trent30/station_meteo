# Weather station with arduino


Output with python script using matplotlib.
-------------------------------------------
![](https://raw.githubusercontent.com/trent30/station_meteo/master/arduino/output.svg)

Pictures
--------
![](https://github.com/trent30/station_meteo/blob/master/arduino/sm_01.jpg?raw=true)![](https://github.com/trent30/station_meteo/blob/master/arduino/sm_02.jpg?raw=true)

Schema
------
<svg xmlns:svg='http://www.w3.org/2000/svg' xmlns='http://www.w3.org/2000/svg' version='1.2' baseProfile='tiny' x='0in' y='0in' width='8.17292in' height='4.45262in' viewBox='0 0 588.45 320.589' >
<g partID='57470'><g transform='translate(127.65,116.274)' ><g id="schematic">
<rect height="128.7" stroke="#000000" stroke-linecap="round" class="interior rect" stroke-width="0.9" width="56.7" x="14.85" y="14.85" fill="#FFFFFF"/>
<line stroke="none" stroke-linecap="round" y2="28.8" class="pin" x2="86.0499" stroke-width="0" y1="28.8" fill="none" x1="71.6499" id="connector45pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="28.4499" fill="none" id="connector45terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="28.8" class="pin" x2="86.0499" stroke-width="0.699999" y1="28.8" fill="none" x1="71.6499" id="connector57pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="29.4999">D13/SCK</text>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="28.4499" fill="none" id="connector57terminal"/>
<line stroke="none" stroke-linecap="round" y2="36" class="pin" x2="86.0499" stroke-width="0" y1="36" fill="none" x1="71.6499" id="connector30pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="35.6499" fill="none" id="connector30terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="36" class="pin" x2="86.0499" stroke-width="0.699999" y1="36" fill="none" x1="71.6499" id="connector55pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="36.6999">D12/MISO</text>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="35.6499" fill="none" id="connector55terminal"/>
<line stroke="none" stroke-linecap="round" y2="43.2" class="pin" x2="86.0499" stroke-width="0" y1="43.2" fill="none" x1="71.6499" id="connector29pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="42.8499" fill="none" id="connector29terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="43.2" class="pin" x2="86.0499" stroke-width="0.699999" y1="43.2" fill="none" x1="71.6499" id="connector58pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="43.8999">D11/MOSI</text>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="42.8499" fill="none" id="connector58terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="50.4" class="pin" x2="86.0499" stroke-width="0.699999" y1="50.4" fill="none" x1="71.6499" id="connector28pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="51.0999">D10</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="50.0499" fill="none" id="connector28terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="57.6" class="pin" x2="86.0499" stroke-width="0.699999" y1="57.6" fill="none" x1="71.6499" id="connector27pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="58.2999">D9</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="57.2499" fill="none" id="connector27terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="64.8" class="pin" x2="86.0499" stroke-width="0.699999" y1="64.8" fill="none" x1="71.6499" id="connector26pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="65.4999">D8</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="64.4499" fill="none" id="connector26terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="72" class="pin" x2="86.0499" stroke-width="0.699999" y1="72" fill="none" x1="71.6499" id="connector25pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="72.6999">D7</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="71.6499" fill="none" id="connector25terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="79.2" class="pin" x2="86.0499" stroke-width="0.699999" y1="79.2" fill="none" x1="71.6499" id="connector24pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="79.8999">D6</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="78.8499" fill="none" id="connector24terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="86.4" class="pin" x2="86.0499" stroke-width="0.699999" y1="86.4" fill="none" x1="71.6499" id="connector23pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="87.0999">D5</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="86.0499" fill="none" id="connector23terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="93.6" class="pin" x2="86.0499" stroke-width="0.699999" y1="93.6" fill="none" x1="71.6499" id="connector22pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="94.2999">D4</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="93.2499" fill="none" id="connector22terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="100.8" class="pin" x2="86.0499" stroke-width="0.699999" y1="100.8" fill="none" x1="71.6499" id="connector21pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="101.5">D3</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="100.45" fill="none" id="connector21terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="108" class="pin" x2="86.0499" stroke-width="0.699999" y1="108" fill="none" x1="71.6499" id="connector20pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="108.7">D2</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="107.65" fill="none" id="connector20terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="122.4" class="pin" x2="86.0499" stroke-width="0.699999" y1="122.4" fill="none" x1="71.6499" id="connector16pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="123.1">D1/TX</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="122.05" fill="none" id="connector16terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="129.6" class="pin" x2="86.0499" stroke-width="0.699999" y1="129.6" fill="none" x1="71.6499" id="connector17pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="70.2499" y="130.3">D0/RX</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="86.0499" y="129.25" fill="none" id="connector17terminal"/>
<line stroke="none" stroke-linecap="round" y2="28.8" class="pin" x2="14.75" stroke-width="0" y1="28.8" fill="none" x1="0.349999" id="connector33pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="28.4499" fill="none" id="connector33terminal"/>
<line stroke="none" stroke-linecap="round" y2="28.8" class="pin" x2="14.75" stroke-width="0" y1="28.8" fill="none" x1="0.349999" id="connector18pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="28.4499" fill="none" id="connector18terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="28.8" class="pin" x2="14.75" stroke-width="0.699999" y1="28.8" fill="none" x1="0.349999" id="connector59pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="29.4999">RESET</text>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="28.4499" fill="none" id="connector59terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="36" class="pin" x2="14.75" stroke-width="0.699999" y1="36" fill="none" x1="0.349999" id="connector43pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="36.6999">AREF</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="35.6499" fill="none" id="connector43terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="50.4" class="pin" x2="14.75" stroke-width="0.699999" y1="50.4" fill="none" x1="0.349999" id="connector42pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="51.0999">A0</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="50.0499" fill="none" id="connector42terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="57.6" class="pin" x2="14.75" stroke-width="0.699999" y1="57.6" fill="none" x1="0.349999" id="connector41pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="58.2999">A1</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="57.2499" fill="none" id="connector41terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="64.8" class="pin" x2="14.75" stroke-width="0.699999" y1="64.8" fill="none" x1="0.349999" id="connector40pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="65.4999">A2</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="64.4499" fill="none" id="connector40terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="72" class="pin" x2="14.75" stroke-width="0.699999" y1="72" fill="none" x1="0.349999" id="connector39pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="72.6999">A3</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="71.6499" fill="none" id="connector39terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="79.2" class="pin" x2="14.75" stroke-width="0.699999" y1="79.2" fill="none" x1="0.349999" id="connector38pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="79.8999">A4</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="78.8499" fill="none" id="connector38terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="86.4" class="pin" x2="14.75" stroke-width="0.699999" y1="86.4" fill="none" x1="0.349999" id="connector37pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="87.0999">A5</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="86.0499" fill="none" id="connector37terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="93.6" class="pin" x2="14.75" stroke-width="0.699999" y1="93.6" fill="none" x1="0.349999" id="connector36pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="94.2999">A6</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="93.2499" fill="none" id="connector36terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="100.8" class="pin" x2="14.75" stroke-width="0.699999" y1="100.8" fill="none" x1="0.349999" id="connector35pin"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="101.5">A7</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="100.45" fill="none" id="connector35terminal"/>
<line stroke="none" stroke-linecap="round" y2="158.05" class="pin" x2="43.2" stroke-width="0" y1="143.65" fill="none" x1="43.2" id="connector19pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="42.8499" y="158.05" fill="none" id="connector19terminal"/>
<line stroke="none" stroke-linecap="round" y2="158.05" class="pin" x2="43.2" stroke-width="0" y1="143.65" fill="none" x1="43.2" id="connector32pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="42.8499" y="158.05" fill="none" id="connector32terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="158.05" class="pin" x2="43.2" stroke-width="0.699999" y1="143.65" fill="none" x1="43.2" id="connector60pin"/>
<g transform="matrix(1, 0, 0, 1, 43.8999, 142.25)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">GND</text>
</g>
</g>
</g>
</g>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="42.8499" y="158.05" fill="none" id="connector60terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="28.8" stroke-width="0.699999" y1="0.349999" fill="none" x1="28.8" id="connector31pin"/>
<g transform="matrix(1, 0, 0, 1, 29.4999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">VIN</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="28.4499" y="-0.349999" fill="none" id="connector31terminal"/>
<line stroke="none" stroke-linecap="round" y2="14.75" class="pin" x2="43.2" stroke-width="0" y1="0.349999" fill="none" x1="43.2" id="connector34pin"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="42.8499" y="-0.349999" fill="none" id="connector34terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="43.2" stroke-width="0.699999" y1="0.349999" fill="none" x1="43.2" id="connector56pin"/>
<g transform="matrix(1, 0, 0, 1, 43.8999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">5V</text>
</g>
</g>
</g>
</g>
<rect height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="42.8499" y="-0.349999" fill="none" id="connector56terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="57.6" stroke-width="0.699999" y1="0.349999" fill="none" x1="57.6" id="connector44pin"/>
<g transform="matrix(1, 0, 0, 1, 58.2999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">3V3</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="57.2499" y="-0.349999" fill="none" id="connector44terminal"/>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="43.6499" y="72.8498" id="label">Arduino</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="43.6499" y="77.3833" id="label">Nano</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="43.6499" y="81.9167" id="label">(Rev3.0)</text>
</g>
</g></g><g partID='65090'><g transform='translate(487.65,94.6739)' ><g id="schematic">
<rect height="56.7" stroke="#000000" stroke-linecap="round" class="interior rect" stroke-width="0.9" width="71.1" x="14.85" y="14.85" fill="#FFFFFF"/>
<line stroke="#787878" stroke-linecap="round" y2="36" class="pin" x2="14.75" stroke-width="0.699999" y1="36" fill="none" x1="0.349999" id="connector9"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="36.6999">Data-signal</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="35.6499" fill="none" id="connector9terminal"/>
<line stroke="none" stroke-linecap="round" y2="86.0499" class="pin" x2="50.4" stroke-width="0" y1="71.6499" fill="none" x1="50.4" id="connector10"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="86.0499" fill="none" id="connector10terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="86.0499" class="pin" x2="50.4" stroke-width="0.699999" y1="71.6499" fill="none" x1="50.4" id="connector11"/>
<g transform="matrix(1, 0, 0, 1, 51.0999, 70.2499)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">GND 2</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="86.0499" fill="none" id="connector11terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="50.4" stroke-width="0.699999" y1="0.349999" fill="none" x1="50.4" id="connector8"/>
<g transform="matrix(1, 0, 0, 1, 51.0999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">Vcc</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="-0.349999" fill="none" id="connector8terminal"/>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="32.3164" id="label">Humidity</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="36.8498" id="label">and</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="41.3833" id="label">Temperature</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="45.9167" id="label">Sensor</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="50.4502" id="label">RHT03</text>
</g>
</g></g><g partID='74000'><g transform='translate(358.05,94.6739)' ><g id="schematic">
<rect height="56.7" stroke="#000000" stroke-linecap="round" class="interior rect" stroke-width="0.9" width="71.1" x="14.85" y="14.85" fill="#FFFFFF"/>
<line stroke="#787878" stroke-linecap="round" y2="36" class="pin" x2="14.75" stroke-width="0.699999" y1="36" fill="none" x1="0.349999" id="connector9"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="36.6999">Data-signal</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="35.6499" fill="none" id="connector9terminal"/>
<line stroke="none" stroke-linecap="round" y2="86.0499" class="pin" x2="50.4" stroke-width="0" y1="71.6499" fill="none" x1="50.4" id="connector10"/>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="86.0499" fill="none" id="connector10terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="86.0499" class="pin" x2="50.4" stroke-width="0.699999" y1="71.6499" fill="none" x1="50.4" id="connector11"/>
<g transform="matrix(1, 0, 0, 1, 51.0999, 70.2499)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">GND 2</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="86.0499" fill="none" id="connector11terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="50.4" stroke-width="0.699999" y1="0.349999" fill="none" x1="50.4" id="connector8"/>
<g transform="matrix(1, 0, 0, 1, 51.0999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">Vcc</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="50.0499" y="-0.349999" fill="none" id="connector8terminal"/>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="32.3164" id="label">Humidity</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="36.8498" id="label">and</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="41.3833" id="label">Temperature</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="45.9167" id="label">Sensor</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="50.8499" y="50.4502" id="label">RHT03</text>
</g>
</g></g><g partID='87650'><g transform='translate(213.7,177.978)' ><g xmlns="http://www.w3.org/2000/svg" id="schematic">
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="8.63003" stroke-width="0.432002" y1="3.096" x1="7.55002"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="10.43" stroke-width="0.432002" y1="0.216" x1="8.63003"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="12.23" stroke-width="0.432002" y1="5.976" x1="10.43"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="14.03" stroke-width="0.432002" y1="0.216" x1="12.23"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="15.8301" stroke-width="0.432002" y1="5.976" x1="14.03"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="17.6301" stroke-width="0.432002" y1="0.216" x1="15.8301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="19.4301" stroke-width="0.432002" y1="5.976" x1="17.6301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="21.2301" stroke-width="0.432002" y1="0.216" x1="19.4301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="3.096" class="other" x2="21.9501" stroke-width="0.432002" y1="5.976" x1="21.2301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="21.9501" stroke-width="0.700001" connectorname="2" y1="3.096" id="connector1pin" x1="29.1502"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="29.1502" y="3.096" fill="none" id="connector1terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="25.5501" y="2.046">2</text>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="7.55002" stroke-width="0.700001" connectorname="1" y1="3.096" id="connector0pin" x1="0.350001"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="0.350001" y="3.096" fill="none" id="connector0terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="3.95001" y="2.046">1</text>
</g>
</g></g><g partID='93280'><g transform='translate(242.499,191.226)' ><g transform='matrix(0,-1,1,0,0,0)'  ><g id="schematic">
<line stroke="#000000" stroke-linecap="round" y2="14.75" x2="10.152" stroke-width="0.5" fill="none" y1="14.75" x1="13.752"/>
<line stroke="#000000" stroke-linecap="round" y2="14.75" x2="6.552" stroke-width="0.5" fill="none" y1="14.75" x1="10.152"/>
<polygon stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0.9" fill="#FFFFFF" points="13.752,7.55,10.152,14.75,6.552,7.55,10.152,7.55"/>
<line stroke="#000000" stroke-linecap="round" y2="12.558" x2="1.543" stroke-width="0.5" fill="none" y1="9.71" x1="4.392"/>
<line stroke="#000000" stroke-linecap="round" y2="15.843" x2="1.859" stroke-width="0.5" fill="none" y1="12.951" x1="4.752"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" x2="10.152" stroke-width="0.75" fill="none" y1="21.951" id="connector0pin" x1="10.152"/>
<g height="0" width="0.001" x="10.152" y="21.951" fill="none" id="connector0terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" x2="10.152" stroke-width="0.75" fill="none" y1="21.951" id="connector3pin" x1="10.152"/>
<g height="0" width="0.001" x="10.152" y="21.951" fill="none" id="connector3terminal"/>
<g transform="matrix(1, 0, 0, 1, 3.21098, 6.47347)">
<g>
<g transform="rotate(270)">
<g>
<g transform="matrix(1, 0, 0, 1, -12.5641, 5.8908)">
<text fill="#8C8C8C" font-family="'DroidSans'" font-size="2.5">2</text>
</g>
</g>
</g>
</g>
</g>
<line stroke="#787878" stroke-linecap="round" y2="7.55" x2="10.152" stroke-width="0.75" fill="none" y1="0.35" id="connector2pin" x1="10.152"/>
<g height="0" width="0.001" x="10.152" y="0.35" fill="none" id="connector2terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="7.55" x2="10.152" stroke-width="0.75" fill="none" y1="0.35" id="connector1pin" x1="10.152"/>
<g height="0" width="0.001" x="10.152" y="0.35" fill="none" id="connector1terminal"/>
<g transform="matrix(1, 0, 0, 1, 3.21098, 1.39347)">
<g>
<g transform="rotate(270)">
<g>
<g transform="matrix(1, 0, 0, 1, -3.2457, 5.8908)">
<text fill="#8C8C8C" font-family="'DroidSans'" font-size="2.5">1</text>
</g>
</g>
</g>
</g>
</g>
<path stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0.2" d="M0.432,13.669l1.08,-2.52l1.44,1.439L0.432,13.669z"/>
<path stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0.2" d="M0.792,16.91l1.08,-2.52l1.439,1.439L0.792,16.91z"/>
</g>
</g></g></g><g partID='99450'><g transform='translate(358.4,133.77)' ><g transform='matrix(-1,0,0,-1,0,0)'  ><g xmlns="http://www.w3.org/2000/svg" id="schematic">
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="8.63003" stroke-width="0.432002" y1="3.096" x1="7.55002"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="10.43" stroke-width="0.432002" y1="0.216" x1="8.63003"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="12.23" stroke-width="0.432002" y1="5.976" x1="10.43"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="14.03" stroke-width="0.432002" y1="0.216" x1="12.23"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="15.8301" stroke-width="0.432002" y1="5.976" x1="14.03"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="17.6301" stroke-width="0.432002" y1="0.216" x1="15.8301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="19.4301" stroke-width="0.432002" y1="5.976" x1="17.6301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="21.2301" stroke-width="0.432002" y1="0.216" x1="19.4301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="3.096" class="other" x2="21.9501" stroke-width="0.432002" y1="5.976" x1="21.2301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="21.9501" stroke-width="0.700001" connectorname="2" y1="3.096" id="connector1pin" x1="29.1502"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="29.1502" y="3.096" fill="none" id="connector1terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="25.5501" y="2.046">2</text>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="7.55002" stroke-width="0.700001" connectorname="1" y1="3.096" id="connector0pin" x1="0.350001"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="0.350001" y="3.096" fill="none" id="connector0terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="3.95001" y="2.046">1</text>
</g>
</g></g></g><g partID='98950'><g transform='translate(488,133.77)' ><g transform='matrix(-1,0,0,-1,0,0)'  ><g xmlns="http://www.w3.org/2000/svg" id="schematic">
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="8.63003" stroke-width="0.432002" y1="3.096" x1="7.55002"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="10.43" stroke-width="0.432002" y1="0.216" x1="8.63003"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="12.23" stroke-width="0.432002" y1="5.976" x1="10.43"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="14.03" stroke-width="0.432002" y1="0.216" x1="12.23"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="15.8301" stroke-width="0.432002" y1="5.976" x1="14.03"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="17.6301" stroke-width="0.432002" y1="0.216" x1="15.8301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="0.216" class="other" x2="19.4301" stroke-width="0.432002" y1="5.976" x1="17.6301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="5.976" class="other" x2="21.2301" stroke-width="0.432002" y1="0.216" x1="19.4301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" y2="3.096" class="other" x2="21.9501" stroke-width="0.432002" y1="5.976" x1="21.2301"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="21.9501" stroke-width="0.700001" connectorname="2" y1="3.096" id="connector1pin" x1="29.1502"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="29.1502" y="3.096" fill="none" id="connector1terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="25.5501" y="2.046">2</text>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="3.096" class="pin" x2="7.55002" stroke-width="0.700001" connectorname="1" y1="3.096" id="connector0pin" x1="0.350001"/>
<g height="0.000283465" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.000283466" x="0.350001" y="3.096" fill="none" id="connector0terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.50001" x="3.95001" y="2.046">1</text>
</g>
</g></g></g><g partID='140250'><g transform='translate(26.85,152.274)' ><g id="schematic">
<rect height="63.9" stroke="#000000" stroke-linecap="round" class="interior rect" stroke-width="0.9" width="42.3" x="14.85" y="14.85" fill="#FFFFFF"/>
<line stroke="#787878" stroke-linecap="round" y2="43.2" class="pin" x2="71.6499" stroke-width="0.699999" y1="43.2" fill="none" x1="57.2499" id="connector9pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="55.8499" y="43.8999">SDA</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="71.6499" y="42.8499" fill="none" id="connector9terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="50.4" class="pin" x2="71.6499" stroke-width="0.699999" y1="50.4" fill="none" x1="57.2499" id="connector8pin"/>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="55.8499" y="51.0999">SCL</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="71.6499" y="50.0499" fill="none" id="connector8terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="43.2" class="pin" x2="14.75" stroke-width="0.699999" y1="43.2" fill="none" x1="0.349999" id="connector7"/>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="43.8999">SQW</text>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="42.8499" fill="none" id="connector7terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="93.2499" class="pin" x2="36" stroke-width="0.699999" y1="78.8499" fill="none" x1="36" id="connector6"/>
<g transform="matrix(1, 0, 0, 1, 36.6999, 77.4499)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">GND</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="35.6499" y="93.2499" fill="none" id="connector6terminal"/>
<line stroke="#787878" stroke-linecap="round" y2="14.75" class="pin" x2="36" stroke-width="0.699999" y1="0.349999" fill="none" x1="36" id="connector5pin"/>
<g transform="matrix(1, 0, 0, 1, 36.6999, 16.15)">
<g>
<g transform="rotate(270)">
<g>
<text stroke="none" text-anchor="end" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="0" y="0">5V</text>
</g>
</g>
</g>
</g>
<g height="0.699999" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="35.6499" y="-0.349999" fill="none" id="connector5terminal"/>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="29.1161" id="label">Real</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="33.6495" id="label">Time</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="38.183" id="label">Clock</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="42.7164" id="label">Module</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="47.2499" id="label">DS1307</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="51.7836" id="label">RTC</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="56.317" id="label">Breakout</text>
<text stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="36.4501" y="60.8505" id="label">Board</text>
</g>
</g></g><g partID='146940'><g transform='translate(250.05,15.4738)' ><g xmlns="http://www.w3.org/2000/svg" id="schematic">
<rect height="99.9" xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-linecap="round" class="interior rect" stroke-width="0.9" width="49.5" x="14.85" y="0.45" fill="#FFFFFF"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="7.2" class="pin" x2="14.75" stroke-width="0.699999" y1="7.2" fill="none" x1="0.349999" id="connector7pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="6.14999">1</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="7.89999">NC</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="6.85001" fill="none" id="connector7terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="14.4" class="pin" x2="14.75" stroke-width="0.699999" y1="14.4" fill="none" x1="0.349999" id="connector0pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="13.35">2</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="15.1">CS</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="14.05" fill="none" id="connector0terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="21.6" class="pin" x2="14.75" stroke-width="0.699999" y1="21.6" fill="none" x1="0.349999" id="connector1pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="20.55">3</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="22.3">DI</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="21.25" fill="none" id="connector1terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="28.8" class="pin" x2="14.75" stroke-width="0.699999" y1="28.8" fill="none" x1="0.349999" id="connector3pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="27.75">4</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="29.4999">VCC</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="28.4499" fill="none" id="connector3terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="36" class="pin" x2="14.75" stroke-width="0.699999" y1="36" fill="none" x1="0.349999" id="connector4pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="34.95">5</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="36.6999">SCK</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="35.6499" fill="none" id="connector4terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="43.2" class="pin" x2="14.75" stroke-width="0.699999" y1="43.2" fill="none" x1="0.349999" id="connector2pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="42.15">6</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="43.8999">GND</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="42.8499" fill="none" id="connector2terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="50.4" class="pin" x2="14.75" stroke-width="0.699999" y1="50.4" fill="none" x1="0.349999" id="connector6pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="49.35">7</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="51.0999">DO</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="50.0499" fill="none" id="connector6terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="57.6" class="pin" x2="14.75" stroke-width="0.699999" y1="57.6" fill="none" x1="0.349999" id="connector5pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="56.55">8</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="58.2999">RSV</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="57.2499" fill="none" id="connector5terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="72" class="pin" x2="14.75" stroke-width="0.699999" y1="72" fill="none" x1="0.349999" id="connector9pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="70.95">11</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="72.6999">SHIELD</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="71.6499" fill="none" id="connector9terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="79.2" class="pin" x2="14.75" stroke-width="0.699999" y1="79.2" fill="none" x1="0.349999" id="connector10pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="78.15">10</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="79.8999">SHIELD</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="78.8499" fill="none" id="connector10terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="86.4" class="pin" x2="14.75" stroke-width="0.699999" y1="86.4" fill="none" x1="0.349999" id="connector8pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="85.35">12</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="87.0999">SHIELD</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="86.0499" fill="none" id="connector8terminal"/>
<line xmlns="http://www.w3.org/2000/svg" stroke="#787878" stroke-linecap="round" y2="93.6" class="pin" x2="14.75" stroke-width="0.699999" y1="93.6" fill="none" x1="0.349999" id="connector11pin"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="2.5" x="7.54999" y="92.55">9</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="start" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#8c8c8c" font-size="3.49999" x="16.15" y="94.2999">SHIELD</text>
<g height="0.699999" xmlns="http://www.w3.org/2000/svg" stroke="none" class="terminal" stroke-width="0" width="0.699999" x="-0.349999" y="93.2499" fill="none" id="connector11terminal"/>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="40.0501" y="46.3164" id="label">microSD</text>
<text xmlns="http://www.w3.org/2000/svg" stroke="none" text-anchor="middle" class="text" stroke-width="0" font-family="'Droid Sans'" fill="#000000" font-size="4.25001" x="40.0501" y="50.8501" id="label">Socket</text>
</g>
</g></g><g partID='164710'><line stroke-linecap='round' stroke='#157de6' x1='214.05' y1='224.274' x2='487.65' y2='130.674' stroke-width='0.4' /></g><g partID='164730'><line stroke-linecap='round' stroke='#157de6' x1='487.65' y1='130.674' x2='487.65' y2='130.674' stroke-width='0.4' /></g><g partID='164750'><line stroke-linecap='round' stroke='#33ffc5' x1='242.849' y1='181.074' x2='242.85' y2='181.074' stroke-width='0.4' /></g><g partID='164770'><line stroke-linecap='round' stroke='#8c3b00' x1='214.05' y1='181.074' x2='214.05' y2='181.074' stroke-width='0.4' /></g><g partID='164790'><line stroke-linecap='round' stroke='#00a527' x1='214.05' y1='217.074' x2='358.05' y2='130.674' stroke-width='0.4' /></g><g partID='164810'><line stroke-linecap='round' stroke='#00a527' x1='358.05' y1='130.674' x2='358.05' y2='130.674' stroke-width='0.4' /></g><g partID='138890'><line stroke-linecap='round' stroke='#404040' x1='264.45' y1='181.074' x2='292.717' y2='181.074' stroke-width='0.699998' /></g><g partID='138910'><line stroke-linecap='round' stroke='#404040' x1='292.716' y1='181.074' x2='293.783' y2='188.007' stroke-width='0.699998' /></g><circle  fill="black" cx="292.716" cy="181.074" r="1.44" stroke-width="0" stroke="none" /><g partID='138930'><line stroke-linecap='round' stroke='#404040' x1='293.25' y1='188.274' x2='293.25' y2='181.074' stroke-width='0.699998' /></g><g partID='138950'><line stroke-linecap='round' stroke='#404040' x1='293.25' y1='181.074' x2='408.45' y2='181.074' stroke-width='0.699998' /></g><g partID='139730'><line stroke-linecap='round' stroke='#404040' x1='415.65' y1='181.074' x2='415.65' y2='181.074' stroke-width='0.699998' /></g><g partID='138970'><line stroke-linecap='round' stroke='#404040' x1='538.05' y1='181.074' x2='415.65' y2='181.074' stroke-width='0.699998' /></g><g partID='138990'><line stroke-linecap='round' stroke='#404040' x1='415.65' y1='181.074' x2='415.65' y2='188.274' stroke-width='0.699998' /></g><g partID='139010'><line stroke-linecap='round' stroke='#404040' x1='415.65' y1='188.274' x2='300.45' y2='188.274' stroke-width='0.699998' /></g><g partID='139030'><line stroke-linecap='round' stroke='#404040' x1='300.45' y1='188.274' x2='293.783' y2='188.007' stroke-width='0.699998' /></g><circle  fill="black" cx="300.45" cy="188.274" r="1.44" stroke-width="0" stroke="none" /><g partID='139050'><line stroke-linecap='round' stroke='#404040' x1='170.85' y1='274.674' x2='293.25' y2='274.674' stroke-width='0.699998' /></g><circle  fill="black" cx="293.25" cy="274.674" r="1.44" stroke-width="0" stroke="none" /><g partID='139070'><line stroke-linecap='round' stroke='#404040' x1='293.25' y1='274.674' x2='293.25' y2='188.274' stroke-width='0.699998' /></g><g partID='139210'><line stroke-linecap='round' stroke='#404040' x1='293.25' y1='188.274' x2='293.783' y2='188.007' stroke-width='0.699998' /></g><g partID='139610'><line stroke-linecap='round' stroke='#404040' x1='458.85' y1='94.6738' x2='458.85' y2='130.674' stroke-width='0.699998' /></g><circle  fill="black" cx="458.85" cy="94.6738" r="1.44" stroke-width="0" stroke="none" /><g partID='139620'><line stroke-linecap='round' stroke='#404040' x1='538.05' y1='94.6739' x2='458.85' y2='94.6738' stroke-width='0.699998' /></g><g partID='150240'><line stroke-linecap='round' stroke='#404040' x1='127.65' y1='202.674' x2='130.65' y2='204.339' stroke-width='0.699998' /></g><g partID='150260'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='204.339' x2='101.85' y2='204.339' stroke-width='0.699998' /></g><g partID='150280'><line stroke-linecap='round' stroke='#404040' x1='101.85' y1='204.339' x2='98.85' y2='202.674' stroke-width='0.699998' /></g><g partID='150300'><line stroke-linecap='round' stroke='#404040' x1='98.85' y1='195.474' x2='101.85' y2='197.139' stroke-width='0.699998' /></g><g partID='150320'><line stroke-linecap='round' stroke='#404040' x1='101.85' y1='197.139' x2='130.65' y2='197.139' stroke-width='0.699998' /></g><g partID='150340'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='197.139' x2='127.65' y2='195.474' stroke-width='0.699998' /></g><g partID='150360'><line stroke-linecap='round' stroke='#404040' x1='170.85' y1='116.274' x2='170.85' y2='103.539' stroke-width='0.699998' /></g><g partID='150380'><line stroke-linecap='round' stroke='#404040' x1='170.85' y1='103.539' x2='145.05' y2='103.539' stroke-width='0.699998' /></g><g partID='150420'><line stroke-linecap='round' stroke='#404040' x1='145.05' y1='103.539' x2='145.05' y2='117.939' stroke-width='0.699998' /></g><g partID='150440'><line stroke-linecap='round' stroke='#404040' x1='145.05' y1='117.939' x2='65.8501' y2='117.939' stroke-width='0.699998' /></g><g partID='150460'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='117.939' x2='65.85' y2='153.939' stroke-width='0.699998' /></g><g partID='150480'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='153.939' x2='62.8499' y2='152.274' stroke-width='0.699998' /></g><g partID='150500'><line stroke-linecap='round' stroke='#404040' x1='214.05' y1='166.674' x2='217.05' y2='168.339' stroke-width='0.699998' /></g><g partID='150520'><line stroke-linecap='round' stroke='#404040' x1='217.05' y1='168.339' x2='231.45' y2='168.339' stroke-width='0.699998' /></g><g partID='150540'><line stroke-linecap='round' stroke='#404040' x1='231.45' y1='168.339' x2='231.45' y2='146.739' stroke-width='0.699998' /></g><g partID='150560'><line stroke-linecap='round' stroke='#404040' x1='231.45' y1='146.739' x2='238.65' y2='146.739' stroke-width='0.699998' /></g><g partID='150580'><line stroke-linecap='round' stroke='#404040' x1='238.65' y1='146.739' x2='238.65' y2='31.5389' stroke-width='0.699998' /></g><g partID='150600'><line stroke-linecap='round' stroke='#404040' x1='238.65' y1='31.5386' x2='253.05' y2='31.5386' stroke-width='0.699998' /></g><g partID='150620'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='31.5386' x2='250.05' y2='29.8735' stroke-width='0.699998' /></g><g partID='150640'><line stroke-linecap='round' stroke='#404040' x1='214.05' y1='152.274' x2='217.05' y2='153.939' stroke-width='0.699998' /></g><g partID='150660'><line stroke-linecap='round' stroke='#404040' x1='217.05' y1='153.939' x2='245.85' y2='153.939' stroke-width='0.699998' /></g><g partID='150680'><line stroke-linecap='round' stroke='#404040' x1='245.85' y1='153.939' x2='245.85' y2='161.139' stroke-width='0.699998' /></g><g partID='150700'><line stroke-linecap='round' stroke='#404040' x1='245.85' y1='161.139' x2='267.45' y2='161.139' stroke-width='0.699998' /></g><g partID='150720'><line stroke-linecap='round' stroke='#404040' x1='267.45' y1='161.139' x2='267.45' y2='164.739' stroke-width='0.699998' /></g><g partID='150740'><line stroke-linecap='round' stroke='#404040' x1='267.45' y1='164.739' x2='271.05' y2='168.339' stroke-width='0.699998' /></g><g partID='150760'><line stroke-linecap='round' stroke='#404040' x1='271.05' y1='168.339' x2='274.65' y2='168.339' stroke-width='0.699998' /></g><g partID='150780'><line stroke-linecap='round' stroke='#404040' x1='274.65' y1='168.339' x2='274.65' y2='290.739' stroke-width='0.699998' /></g><g partID='150800'><line stroke-linecap='round' stroke='#404040' x1='274.65' y1='290.739' x2='159.45' y2='290.739' stroke-width='0.699998' /></g><g partID='150820'><line stroke-linecap='round' stroke='#404040' x1='159.45' y1='290.739' x2='159.45' y2='276.339' stroke-width='0.699998' /></g><g partID='150840'><line stroke-linecap='round' stroke='#404040' x1='159.45' y1='276.339' x2='130.65' y2='276.339' stroke-width='0.699998' /></g><g partID='150860'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='276.339' x2='130.65' y2='233.139' stroke-width='0.699998' /></g><g partID='150880'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='233.139' x2='116.25' y2='233.139' stroke-width='0.699998' /></g><g partID='150900'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='233.139' x2='116.25' y2='132.339' stroke-width='0.699998' /></g><g partID='150920'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='132.339' x2='130.65' y2='132.339' stroke-width='0.699998' /></g><g partID='150940'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='132.339' x2='130.65' y2='89.1389' stroke-width='0.699998' /></g><g partID='150960'><line stroke-linecap='round' stroke='#404040' x1='130.65' y1='89.1389' x2='224.25' y2='89.1389' stroke-width='0.699998' /></g><g partID='150980'><line stroke-linecap='round' stroke='#404040' x1='224.25' y1='89.1389' x2='224.25' y2='67.5389' stroke-width='0.699998' /></g><g partID='151000'><line stroke-linecap='round' stroke='#404040' x1='224.25' y1='67.5389' x2='253.05' y2='67.5389' stroke-width='0.699998' /></g><g partID='151020'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='67.5389' x2='250.05' y2='65.8738' stroke-width='0.699998' /></g><g partID='151040'><line stroke-linecap='round' stroke='#404040' x1='214.05' y1='145.074' x2='217.05' y2='146.739' stroke-width='0.699998' /></g><g partID='151060'><line stroke-linecap='round' stroke='#404040' x1='217.05' y1='146.739' x2='253.05' y2='146.739' stroke-width='0.699998' /></g><g partID='151080'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='146.739' x2='253.05' y2='125.139' stroke-width='0.699998' /></g><g partID='151100'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='125.139' x2='209.85' y2='125.139' stroke-width='0.699998' /></g><g partID='151120'><line stroke-linecap='round' stroke='#404040' x1='209.85' y1='125.139' x2='209.85' y2='53.1389' stroke-width='0.699998' /></g><g partID='151140'><line stroke-linecap='round' stroke='#404040' x1='209.85' y1='53.1386' x2='253.05' y2='53.1386' stroke-width='0.699998' /></g><g partID='151160'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='53.1386' x2='250.05' y2='51.4735' stroke-width='0.699998' /></g><g partID='151180'><line stroke-linecap='round' stroke='#404040' x1='458.85' y1='130.674' x2='458.85' y2='94.6739' stroke-width='0.699998' /></g><circle  fill="black" cx="458.85" cy="94.6739" r="1.44" stroke-width="0" stroke="none" /><g partID='151200'><line stroke-linecap='round' stroke='#404040' x1='458.85' y1='94.6739' x2='408.45' y2='94.6739' stroke-width='0.699998' /></g><circle  fill="black" cx="458.85" cy="94.6739" r="1.44" stroke-width="0" stroke="none" /><g partID='151320'><line stroke-linecap='round' stroke='#404040' x1='329.25' y1='130.674' x2='332.25' y2='132.339' stroke-width='0.699998' /></g><g partID='151340'><line stroke-linecap='round' stroke='#404040' x1='332.25' y1='132.339' x2='332.25' y2='110.739' stroke-width='0.699998' /></g><circle  fill="black" cx="332.25" cy="132.339" r="1.44" stroke-width="0" stroke="none" /><g partID='151360'><line stroke-linecap='round' stroke='#404040' x1='332.25' y1='110.739' x2='332.25' y2='94.6739' stroke-width='0.699998' /></g><g partID='151380'><line stroke-linecap='round' stroke='#404040' x1='332.25' y1='94.6739' x2='408.45' y2='94.6739' stroke-width='0.699998' /></g><circle  fill="black" cx="332.25" cy="94.6739" r="1.44" stroke-width="0" stroke="none" /><g partID='151440'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='116.274' x2='185.25' y2='116.274' stroke-width='0.699998' /></g><g partID='151460'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='116.274' x2='185.25' y2='37.0738' stroke-width='0.699998' /></g><g partID='151480'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='37.0738' x2='185.25' y2='37.0738' stroke-width='0.699998' /></g><g partID='151500'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='37.0738' x2='185.25' y2='37.0738' stroke-width='0.699998' /></g><g partID='151520'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='37.0738' x2='185.25' y2='8.27378' stroke-width='0.699998' /></g><g partID='151540'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='8.27378' x2='185.25' y2='1.07378' stroke-width='0.699998' /></g><g partID='151560'><line stroke-linecap='round' stroke='#404040' x1='185.25' y1='1.07378' x2='224.25' y2='2.7389' stroke-width='0.699998' /></g><g partID='151580'><line stroke-linecap='round' stroke='#404040' x1='224.25' y1='2.73858' x2='332.25' y2='2.73858' stroke-width='0.699998' /></g><g partID='151660'><line stroke-linecap='round' stroke='#404040' x1='332.25' y1='2.73858' x2='332.25' y2='110.739' stroke-width='0.699998' /></g><g partID='151680'><line stroke-linecap='round' stroke='#404040' x1='214.05' y1='159.474' x2='217.05' y2='161.139' stroke-width='0.699998' /></g><g partID='151700'><line stroke-linecap='round' stroke='#404040' x1='217.05' y1='161.139' x2='289.05' y2='161.139' stroke-width='0.699998' /></g><g partID='151720'><line stroke-linecap='round' stroke='#404040' x1='289.05' y1='161.139' x2='289.05' y2='305.139' stroke-width='0.699998' /></g><g partID='151740'><line stroke-linecap='round' stroke='#404040' x1='289.05' y1='305.139' x2='145.05' y2='305.139' stroke-width='0.699998' /></g><g partID='151760'><line stroke-linecap='round' stroke='#404040' x1='145.05' y1='305.139' x2='145.05' y2='290.739' stroke-width='0.699998' /></g><g partID='151780'><line stroke-linecap='round' stroke='#404040' x1='145.05' y1='290.739' x2='116.25' y2='290.739' stroke-width='0.699998' /></g><g partID='151800'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='290.739' x2='116.25' y2='261.939' stroke-width='0.699998' /></g><g partID='151820'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='261.939' x2='15.4501' y2='261.939' stroke-width='0.699998' /></g><g partID='151840'><line stroke-linecap='round' stroke='#404040' x1='15.45' y1='261.939' x2='15.45' y2='153.939' stroke-width='0.699998' /></g><g partID='151860'><line stroke-linecap='round' stroke='#404040' x1='15.45' y1='153.939' x2='51.45' y2='153.939' stroke-width='0.699998' /></g><g partID='151920'><line stroke-linecap='round' stroke='#404040' x1='51.45' y1='153.939' x2='51.45' y2='103.539' stroke-width='0.699998' /></g><g partID='151940'><line stroke-linecap='round' stroke='#404040' x1='51.45' y1='103.539' x2='116.25' y2='103.539' stroke-width='0.699998' /></g><g partID='151960'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='103.539' x2='116.25' y2='74.7389' stroke-width='0.699998' /></g><g partID='151980'><line stroke-linecap='round' stroke='#404040' x1='116.25' y1='74.7389' x2='170.85' y2='73.0738' stroke-width='0.699998' /></g><g partID='152000'><line stroke-linecap='round' stroke='#404040' x1='170.85' y1='73.0738' x2='170.85' y2='37.0738' stroke-width='0.699998' /></g><g partID='164290'><line stroke-linecap='round' stroke='#404040' x1='192.45' y1='37.0738' x2='253.05' y2='38.7389' stroke-width='0.699998' /></g><g partID='152020'><line stroke-linecap='round' stroke='#404040' x1='170.85' y1='37.0738' x2='192.45' y2='37.0738' stroke-width='0.699998' /></g><g partID='152040'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='38.7386' x2='250.05' y2='37.0735' stroke-width='0.699998' /></g><g partID='152060'><line stroke-linecap='round' stroke='#404040' x1='62.85' y1='245.874' x2='65.8501' y2='247.539' stroke-width='0.699998' /></g><g partID='152080'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='247.539' x2='65.85' y2='305.139' stroke-width='0.699998' /></g><circle  fill="black" cx="65.85" cy="305.139" r="1.44" stroke-width="0" stroke="none" /><g partID='152100'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='305.139' x2='65.85' y2='319.539' stroke-width='0.699998' /></g><g partID='152120'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='319.539' x2='173.85' y2='319.539' stroke-width='0.699998' /></g><g partID='152160'><line stroke-linecap='round' stroke='#404040' x1='173.85' y1='319.539' x2='173.85' y2='276.339' stroke-width='0.699998' /></g><g partID='152180'><line stroke-linecap='round' stroke='#404040' x1='173.85' y1='276.339' x2='170.85' y2='274.673' stroke-width='0.699998' /></g><circle  fill="black" cx="173.85" cy="276.339" r="1.44" stroke-width="0" stroke="none" /><g partID='152200'><line stroke-linecap='round' stroke='#404040' x1='250.05' y1='58.6738' x2='253.05' y2='60.3389' stroke-width='0.699998' /></g><g partID='152220'><line stroke-linecap='round' stroke='#404040' x1='253.05' y1='60.3389' x2='101.85' y2='60.3389' stroke-width='0.699998' /></g><g partID='152240'><line stroke-linecap='round' stroke='#404040' x1='101.85' y1='60.3389' x2='1.05008' y2='60.3389' stroke-width='0.699998' /></g><g partID='152260'><line stroke-linecap='round' stroke='#404040' x1='1.05' y1='60.3389' x2='1.05' y2='276.339' stroke-width='0.699998' /></g><g partID='152340'><line stroke-linecap='round' stroke='#404040' x1='1.05' y1='276.339' x2='65.85' y2='276.339' stroke-width='0.699998' /></g><g partID='152360'><line stroke-linecap='round' stroke='#404040' x1='65.85' y1='276.339' x2='65.85' y2='247.539' stroke-width='0.699998' /></g><g partID='74000' id='partLabel'><g transform='translate(444.45,89.0739)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>RHT2</text></g></g></g><g partID='87650' id='partLabel'><g transform='translate(243.2,166.778)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>R3</text><text x='0' y='8.75'>220&#x3a9;</text></g></g></g><g partID='93280' id='partLabel'><g transform='translate(231.299,177.115)' ><g transform='matrix(0,-1,1,0,0,0)'  ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>LED1</text><text x='0' y='8.75'>Blue</text></g></g></g></g><g partID='65090' id='partLabel'><g transform='translate(574.05,89.0739)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>RHT1</text></g></g></g><g partID='98950' id='partLabel'><g transform='translate(487.546,145.424)' ><g transform='matrix(0,1,-1,0,0,0)'  ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>R4</text><text x='0' y='8.75'>220&#x3a9;</text></g></g></g></g><g partID='99450' id='partLabel'><g transform='translate(357.946,145.424)' ><g transform='matrix(0,1,-1,0,0,0)'  ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>R5</text><text x='0' y='8.75'>220&#x3a9;</text></g></g></g></g><g partID='57470' id='partLabel'><g transform='translate(214.05,110.674)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>Part1</text></g></g></g><g partID='140250' id='partLabel'><g transform='translate(98.8501,146.674)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>Part2</text></g></g></g><g partID='146940' id='partLabel'><g transform='translate(314.85,9.87378)' ><g font-size='5' font-style='normal' font-weight='normal' fill='#000000' font-family="'DroidSans'" id='schematicLabel' fill-opacity='1' stroke='none' ><text x='0' y='3.75'>U2</text></g></g></g></svg>

