package hu.ekke.smartgardenserver.model.respons;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ConsumerStatusResponse {
    private Boolean heaterStatus;
    private Boolean lightStatus;
    private Boolean humidifierStatus;
    private Boolean waterSysStatus;

    private float desiredTemperature;
    private float desiredHumidity;
    private float desiredSoilMoisture;
    private float desiredLight;

}
