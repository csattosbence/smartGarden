package hu.ekke.smartgardenserver.service.impl;

import hu.ekke.smartgardenserver.service.GardenControllerService;
import hu.ekke.smartgardenserver.service.PiApiCalls;
import hu.ekke.smartgardenserver.service.runable.AutomationLogic;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GardenControllerServiceImpl implements GardenControllerService {

    @Autowired
    PiApiCalls piApiCalls;

    private final AutomationLogic automationLogic = new AutomationLogic();

    Thread controllerThread = new Thread(automationLogic);


    @Override
    public void setHeater(float temp) {
        automationLogic.turnOnHeater();
        automationLogic.setTemperatureState(temp);
    }

    @Override
    public void turnOffHeater() {
        automationLogic.turnOffHeater();
    }

    public GardenControllerServiceImpl(PiApiCalls piApiCalls){
        this.piApiCalls = piApiCalls;
        this.automationLogic.setPiApiCallsService(piApiCalls);
        controllerThread.start();
    }

}
