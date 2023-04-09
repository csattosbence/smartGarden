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
    public PiBasicResponse heaterOnPiCall() {
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
    public PiBasicResponse heaterOffPiCall() {
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

}
