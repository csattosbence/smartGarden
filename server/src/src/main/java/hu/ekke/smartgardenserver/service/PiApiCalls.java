package hu.ekke.smartgardenserver.service;

import hu.ekke.smartgardenserver.model.respons.PiBasicResponse;

public interface PiApiCalls {
    PiBasicResponse heaterOnPiCall();

    PiBasicResponse heaterOffPiCall();
}
