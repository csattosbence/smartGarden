package hu.ekke.smartgardenserver.service;

import hu.ekke.smartgardenserver.model.respons.PiBasicResponse;

public interface GardenControllerService {

    void setHeater(float temp);

    void turnOffHeater();
    
    void setHumidifier(float humidity);

    void turnOffHumidifier();

    void setLight(float light);

    void turnOffLight();

    void setWateringSystem(float soilMoist);

    void turnOffWateringSystem();
}
