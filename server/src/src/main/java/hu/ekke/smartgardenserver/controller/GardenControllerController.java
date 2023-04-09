package hu.ekke.smartgardenserver.controller;

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
}
