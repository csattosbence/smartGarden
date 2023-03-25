package uni.ekke.backendtest.controller;

import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class TestController {
    @GetMapping("/callPi")
    public String callPi(){
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> response = restTemplate.exchange(
                "http://localhost:5000/getTemp",
                HttpMethod.GET,
                null,
                String.class
                );
        return response.getBody();
    }
}
