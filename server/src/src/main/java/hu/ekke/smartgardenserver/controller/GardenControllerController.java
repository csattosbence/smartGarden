package hu.ekke.smartgardenserver.controller;

import hu.ekke.smartgardenserver.model.respons.ConsumerStatusResponse;
import hu.ekke.smartgardenserver.service.GardenControllerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GardenControllerController {

    @Autowired
    GardenControllerService controllerService;

    @GetMapping("/setHeater")
    public ResponseEntity<?> setHeater(@RequestParam("temperature") float temperature) {
        try{
            controllerService.setHeater(temperature);
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/turnOffHeater")
    public ResponseEntity<?> turnOffHeater() {
        try{
            controllerService.turnOffHeater();
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/setHumidifier")
    public ResponseEntity<?> setHumidifier(@RequestParam("humidity") float humidity) {
        try{
            controllerService.setHumidifier(humidity);
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/turnOffHumidifier")
    public ResponseEntity<?> turnOffHumidifier() {
        try{
            controllerService.turnOffHumidifier();
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/setLight")
    public ResponseEntity<?> setLight(@RequestParam("light") float light) {
        try{
            controllerService.setLight(light);
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/turnOffLight")
    public ResponseEntity<?> turnOffLight() {
        try{
            controllerService.turnOffLight();
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/setWateringSystem")
    public ResponseEntity<?> setWateringSystem(@RequestParam("soilMoist") float soilMoist) {
        try{
            controllerService.setWateringSystem(soilMoist);
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/turnOffWateringSystem")
    public ResponseEntity<?> turnOffWateringSystem() {
        try{
            controllerService.turnOffWateringSystem();
            return ResponseEntity.ok().build();
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/getConsumerStatus")
    public ResponseEntity<ConsumerStatusResponse> getStatusResponses(){
        try {
            ConsumerStatusResponse response = controllerService.getConsumerStatus();
            return ResponseEntity.ok().body(response);
        }catch (Exception e){
            return ResponseEntity.internalServerError().build();
        }
    }
}
