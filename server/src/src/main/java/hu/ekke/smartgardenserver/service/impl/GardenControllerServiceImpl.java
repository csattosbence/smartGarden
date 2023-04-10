package hu.ekke.smartgardenserver.service.impl;

import hu.ekke.smartgardenserver.model.respons.ConsumerStatusResponse;
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

    @Override
    public void setHumidifier(float humidity) {
        automationLogic.turnOnHumidifier();
        automationLogic.setHumidity(humidity);
    }

    @Override
    public void turnOffHumidifier() {
        automationLogic.turnOffHumidifier();
    }

    @Override
    public void setLight(float light) {
        automationLogic.turnOnLight();
        automationLogic.setLight(light);
    }

    @Override
    public void turnOffLight() {
        automationLogic.turnOffLight();
    }

    @Override
    public void setWateringSystem(float soilMoist) {
        automationLogic.turnOnWateringSystem();
        automationLogic.setSoilMoist(soilMoist);
    }

    @Override
    public void turnOffWateringSystem() {
        automationLogic.turnOffWateringSystem();
    }

    @Override
    public ConsumerStatusResponse getConsumerStatus() {
        return automationLogic.getConsumerStatus();
    }

    public GardenControllerServiceImpl(PiApiCalls piApiCalls){
        this.piApiCalls = piApiCalls;
        this.automationLogic.setPiApiCallsService(piApiCalls);
        controllerThread.start();
    }

}
