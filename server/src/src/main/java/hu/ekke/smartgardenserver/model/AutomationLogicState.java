package hu.ekke.smartgardenserver.model;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class AutomationLogicState {
    private boolean heaterOn;
    private boolean humidifierOn;
    private boolean lightOn;
    private boolean waterSystemOn;


    private float desiredTemperature;
    private float desiredHumidity;
    private float desiredSoilMoisture;
    private float desiredLight;
}
