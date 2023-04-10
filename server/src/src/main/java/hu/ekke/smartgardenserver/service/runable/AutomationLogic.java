package hu.ekke.smartgardenserver.service.runable;

import hu.ekke.smartgardenserver.cache.Cache;
import hu.ekke.smartgardenserver.model.SensorData;
import hu.ekke.smartgardenserver.model.AutomationLogicState;
import hu.ekke.smartgardenserver.model.respons.ConsumerStatusResponse;
import hu.ekke.smartgardenserver.service.PiApiCalls;
import lombok.extern.slf4j.Slf4j;

import java.util.List;

@Slf4j
public class AutomationLogic implements Runnable{
    
    private final float INITIAL_TEMPERATURE = 20f;
    private final float INITIAL_HUMIDITY = 40f;
    private final float INITIAL_LIGHT = 1500f;
    private final float INITIAL_SOIL_MOISTURE = 20f;
    private boolean isRunning = true;

    AutomationLogicState state;

    List<SensorData> cache = Cache.getCache();

    PiApiCalls piApiCalls;

    private boolean areStatusesSynched = false;

    @Override
    public void run() {
        setInitialState();
        try {
            while(isRunning){
                syncConsumersStatus();
                controlHumidifier();
                controlLight();
                controlWateringSystem();
                controlHeater();
                Thread.sleep(1000);
            }
        }catch (InterruptedException e){
            log.error("AN ERROR HAS OCCURRED IN AUTOMATION LOGIC " + e.getMessage());
        }
    }

    private void controlHeater() {
        if (state.isHeaterOn()){
            if(cache != null && !cache.isEmpty()){
                SensorData lastData = cache.get(cache.size() -1);
                if (lastData.getTemperature() < state.getDesiredTemperature() && !lastData.getHeaterStatus()){
                    piApiCalls.heaterOn();
                }
                else if (lastData.getTemperature() > state.getDesiredTemperature() && lastData.getHeaterStatus()){
                    piApiCalls.heaterOff();
                }
            }
        }
    }

    private void controlHumidifier(){
        if (state.isHumidifierOn()){
            if(cache != null && !cache.isEmpty()){
                SensorData lastData = cache.get(cache.size() -1);
                if (lastData.getHumidity() < state.getDesiredHumidity() && !Boolean.TRUE.equals(lastData.getHumidifierStatus())){
                    piApiCalls.humidifierOn();
                }
                else if (lastData.getHumidity() > state.getDesiredHumidity() ){
                    piApiCalls.humidifierOff();
                }
            }
        }
    }

    private void controlWateringSystem(){
        if (state.isWaterSystemOn()){
            if(cache != null && !cache.isEmpty()){
                SensorData lastData = cache.get(cache.size() -1);
                if (lastData.getSoilMoisture() < state.getDesiredSoilMoisture() && !Boolean.TRUE.equals(lastData.getWaterSysStatus())){
                    piApiCalls.wateringSystemOn();
                }
                else if ((lastData.getSoilMoisture() > state.getDesiredSoilMoisture())){
                    piApiCalls.wateringSystemOff();
                }
            }
        }
    }

    private void controlLight(){
        if (state.isLightOn()){
            if(cache != null && !cache.isEmpty()){
                SensorData lastData = cache.get(cache.size() -1);
                if(!lastData.getLightStatus()){
                    piApiCalls.turnOnLight();
                }
                if (lastData.getLight() <= state.getDesiredLight() - 50){
                    float incrementValue = state.getDesiredLight() - lastData.getLight();
                    piApiCalls.setLight(incrementValue);
                }
            }
        }
    }

    public void setPiApiCallsService(PiApiCalls piApiCalls){
        this.piApiCalls = piApiCalls;
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


    // Szinkron szükséges a szerver ujrainditás miatt, mert lehet olyan eset hogy az egyik fogyasztó bekapcsolva marad ujraiditásnál és nem kapcsolki
    private void syncConsumersStatus(){
        if(!areStatusesSynched) {
            if (cache != null && !cache.isEmpty()) {
                SensorData lastData = cache.get(cache.size() - 1);
                //SYNC HEATER
                if (!lastData.getHeaterStatus().equals(state.isHeaterOn())) {
                    state.setHeaterOn(lastData.getHeaterStatus());
                }
                //SYNC HUMIDIFIER
                if (!lastData.getHumidifierStatus().equals(state.isHumidifierOn())){
                    state.setHumidifierOn(lastData.getHumidifierStatus());
                }
                //SYNC WATER SYSTEM
                if (!lastData.getWaterSysStatus().equals(state.isWaterSystemOn())){
                    state.setWaterSystemOn(lastData.getWaterSysStatus());
                }
                //LIGHT SYSTEM
                if(!lastData.getLightStatus().equals(state.isLightOn())){
                    state.setLightOn(lastData.getLightStatus());
                }
                areStatusesSynched = true;
            }
        }
    }

    //-----------------------STATE SETTERS-----------------------
    public ConsumerStatusResponse getConsumerStatus(){
        ConsumerStatusResponse response = new ConsumerStatusResponse();

        response.setHeaterStatus(state.isHeaterOn());
        response.setHumidifierStatus(state.isHumidifierOn());
        response.setLightStatus(state.isLightOn());
        response.setWaterSysStatus(state.isWaterSystemOn());

        response.setDesiredLight(state.getDesiredLight());
        response.setDesiredHumidity(state.getDesiredHumidity());
        response.setDesiredSoilMoisture(state.getDesiredSoilMoisture());
        response.setDesiredTemperature(state.getDesiredTemperature());

        return response;
    }
    public synchronized void turnOnHeater(){
        this.state.setHeaterOn(true);
    }

    public synchronized void turnOffHeater(){
        this.state.setHeaterOn(false);
        piApiCalls.heaterOff();
    }

    public synchronized void setTemperatureState(float temp){
        this.state.setDesiredTemperature(temp);
    }

    public void turnOnHumidifier() {
        this.state.setHumidifierOn(true);
    }

    public void setHumidity(float humidity) {
        this.state.setDesiredHumidity(humidity);
    }

    public void turnOffHumidifier() {
        this.state.setHumidifierOn(false);
        piApiCalls.humidifierOff();
    }

    public void turnOnLight() {
        this.state.setLightOn(true);
    }

    public void setLight(float light) {
        this.state.setDesiredLight(light);
    }

    public void turnOffLight() {
        this.state.setLightOn(false);
        piApiCalls.turnOffLight();
    }

    public void turnOnWateringSystem() {
        this.state.setWaterSystemOn(true);
    }

    public void setSoilMoist(float soilMoist) {
        this.state.setDesiredSoilMoisture(soilMoist);
    }

    public void turnOffWateringSystem() {
        this.state.setWaterSystemOn(false);
        piApiCalls.wateringSystemOff();
    }
}
