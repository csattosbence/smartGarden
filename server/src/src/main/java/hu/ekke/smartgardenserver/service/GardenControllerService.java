package hu.ekke.smartgardenserver.service;

import hu.ekke.smartgardenserver.model.respons.PiBasicResponse;

public interface GardenControllerService {

    void setHeater(float temp);

    void turnOffHeater();


}
