#include <DS3231.h>
#include <SD.h>
#include <SPI.h>
#include <DHT.h>

#define DHTTYPE DHT22 
#define CS_PIN 10

File fd;
char filename [] = "data.csv";
int cpt = 0;
DS3231 myRTC(SDA, SCL);
DHT mysensor(2, DHTTYPE);
DHT sensor2(3, DHTTYPE);
int v_boolean = 1;

void setup() {
	int init_sd = 1;
	digitalWrite(8, LOW);
	Serial.begin(9600);
	myRTC.begin();
	while (init_sd) {
		Serial.print("Init SD... ");
		if (SD.begin()) {
			Serial.println("Ok.");
			digitalWrite(8, LOW);
			init_sd = 0;
		} else {
			Serial.println("Fail.");
			digitalWrite(8, HIGH);
			delay(1000);
		}
	 }
	fd = SD.open(filename, FILE_WRITE);
	if (fd) {
		fd.println("date,time,h1,t1,h2,t2,");
	}
	fd.close();
	write_sensors_values_to_sd();
}

void adjust_time() {
	String t = "23:59:59";
	String time = String(myRTC.getTimeStr());
	if ((time == t) && (v_boolean == 1)) {
		myRTC.setTime(23, 59, 50); // moins 9s par jour
		write_sensors_values_to_sd();
		v_boolean = 0;
	} else {
		if (time == t) {
			v_boolean = 1;
			delay(1200);
		}
	}
}

int write_sensors_values_to_sd() {
	float humidity = mysensor.readHumidity();
	float temp = mysensor.readTemperature();
	float h2 = sensor2.readHumidity();
	float t2 = sensor2.readTemperature();
	if (humidity == NULL || temp == NULL || h2 == NULL || t2 == NULL) {
		Serial.println("sensor : read error");
		return 2;
	}
	Serial.print(humidity);
	Serial.print("; ");
	Serial.print(temp);
	Serial.print("; ");
	Serial.print(h2);
	Serial.print("; ");
	Serial.println(t2);
	fd = SD.open(filename, FILE_WRITE);
	if (fd) {
		int r = fd.print(String(myRTC.getDateStr()) + "," + String(myRTC.getTimeStr()) + ",");
		if ( r == 0 ) {
			digitalWrite(8, HIGH);
		} else {
			digitalWrite(8, LOW);	
		}
		fd.print(humidity);
		fd.print(',');
		fd.print(temp);
		fd.print(',');
		fd.print(h2);
		fd.print(',');
		fd.println(t2);
	}
	fd.close();
}

void loop() {
	adjust_time();
	if (cpt >= 1200) {
	//~ if (cpt >= 2) {
		//~ 1200 * 500 ms = 10 min
		write_sensors_values_to_sd();
		cpt = 0;
	}
	delay(500);
	//~ delay(1000);
	cpt += 1;
}

