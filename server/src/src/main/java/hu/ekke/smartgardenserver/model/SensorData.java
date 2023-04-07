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
    private String temperature;
    private String humidity;
    private String totalConsumption;
    private String momentaryConsumption;
    private String currentDate;
    private String light;
    private String soilMoisture;

}
