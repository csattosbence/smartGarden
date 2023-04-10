package hu.ekke.smartgardenserver.model;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class SensorData {
    private Float temperature;
    private Float humidity;
    private Float totalConsumption;
    private Float momentaryConsumption;
    private String currentDate;
    private Float light;
    private Float soilMoisture;
    private Boolean heaterStatus;
    private Boolean lightStatus;
    private Boolean humidifierStatus;
    private Boolean waterSysStatus;

}
