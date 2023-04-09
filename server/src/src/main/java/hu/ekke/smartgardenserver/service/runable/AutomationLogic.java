package hu.ekke.smartgardenserver.service.runable;

import hu.ekke.smartgardenserver.cache.Cache;
import hu.ekke.smartgardenserver.model.SensorData;
import hu.ekke.smartgardenserver.model.AutomationLogicState;
import hu.ekke.smartgardenserver.service.PiApiCalls;

import java.util.List;

public class AutomationLogic implements Runnable{
    
    private final float INITIAL_TEMPERATURE = 20f;
    private final float INITIAL_HUMIDITY = 40f;
    private final float INITIAL_LIGHT = 20f;
    private final float INITIAL_SOIL_MOISTURE = 20f;
    private boolean isRunning = true;

    AutomationLogicState state;

    List<SensorData> cache = Cache.getCache();

    PiApiCalls piApiCalls;

    @Override
    public void run() {
        try {
        setInitialState();
        while(isRunning){
            Thread.sleep(1000);
            controlHeater();
        }

        }catch (InterruptedException e){

        }
    }

    public void stop() {
        isRunning = false;
    }

    private void controlHeater() {
        if (state.isHeaterOn()){
            if(cache != null && !cache.isEmpty()){
                SensorData lastData = cache.get(cache.size() -1);
                if (lastData.getTemperature() < state.getDesiredTemperature()){
                    piApiCalls.heaterOnPiCall();
                }
                else if ((lastData.getTemperature() > state.getDesiredTemperature())){
                    piApiCalls.heaterOffPiCall();
                }
            }
        }
    }

    private void setInitialState(){
        if (this.state == null) {
            this.state = AutomationLogicState.builder()
                    .heaterOn(false)
                    .humidifierOn(false)
                    .lightOn(false)
                    .waterSystemOn(false)
                    .desiredLight(INITIAL_LIGHT)
                    .desiredTemperature(INITIAL_TEMPERATURE)
                    .desiredHumidity(INITIAL_HUMIDITY)
                    .desiredSoilMoisture(INITIAL_SOIL_MOISTURE)
                    .build();
        }
    }

    public synchronized void turnOnHeater(){
        this.state.setHeaterOn(true);
    }

    public synchronized void turnOffHeater(){
        this.state.setHeaterOn(false);
    }

    public synchronized void setTemperatureState(float temp){
        this.state.setDesiredTemperature(temp);
    }

    public void setPiApiCallsService(PiApiCalls piApiCalls){
        this.piApiCalls = piApiCalls;
    }
}
