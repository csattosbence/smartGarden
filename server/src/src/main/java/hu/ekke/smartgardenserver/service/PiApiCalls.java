package hu.ekke.smartgardenserver.service;

import hu.ekke.smartgardenserver.model.respons.PiBasicResponse;

public interface PiApiCalls {
    PiBasicResponse heaterOn();

    PiBasicResponse heaterOff();

    PiBasicResponse humidifierOn();

    PiBasicResponse humidifierOff();

    PiBasicResponse wateringSystemOn();

    PiBasicResponse wateringSystemOff();

    PiBasicResponse turnOnLight();

    PiBasicResponse turnOffLight();

    PiBasicResponse setLight(float incrementValue);
}
