package hu.ekke.smartgardenserver.service.impl;

import com.google.gson.Gson;
import hu.ekke.smartgardenserver.model.respons.PiBasicResponse;
import hu.ekke.smartgardenserver.service.PiApiCalls;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;


@Service
public class PiApiCallsImpl implements PiApiCalls {
    @Value("${pi.host.url}")
    private String piHostUrl;

    private final Gson gson = new Gson();

    @Override
    public PiBasicResponse heaterOn() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/heater_on",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse heaterOff() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/heater_off",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse humidifierOn() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/humidifier_on",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse humidifierOff() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/humidifier_off",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse wateringSystemOn() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/water_on",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse wateringSystemOff() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/water_off",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse turnOnLight() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/light_on",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse turnOffLight() {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/light_off",
                HttpMethod.GET,
                null,
                String.class
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }

    @Override
    public PiBasicResponse setLight(float incrementValue) {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.exchange(
                piHostUrl + "/set_light?light={incrementValue}",
                HttpMethod.GET,
                null,
                String.class,
                incrementValue
        );
        PiBasicResponse response = gson.fromJson(responseEntity.getBody(), PiBasicResponse.class);
        return response;
    }
}
