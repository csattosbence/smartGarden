package hu.ekke.smartgardenserver.socketio.client;

import com.google.gson.Gson;
import hu.ekke.smartgardenserver.cache.Cache;
import hu.ekke.smartgardenserver.model.SensorData;
import io.socket.client.IO;
import io.socket.client.Socket;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.net.URI;

@Configuration
@Slf4j
@RequiredArgsConstructor(onConstructor_ = @Autowired)
public class SocketIoClientConfig {

    @Value("${pi.ws.url}")
    private String piSocketUrl;

    @Value("${pi.ws.path}")
    private String piSocketPath;

    @Bean
    public Socket socketIoClient(){
        URI uri = URI.create(piSocketUrl);
        Gson gson = new Gson();

        IO.Options options = IO.Options.builder()
                .setPath(piSocketPath).build();

        Socket socket = IO.socket(uri,options);

        socket.on("data_from_pi", args -> {
            String data = args[0].toString();
            if (data != null){
                SensorData sensorData = gson.fromJson(data,SensorData.class);
                Cache.addToCache(sensorData);
            }
            log.info(data != null ? data.toString() : "EMPTY DATA");
        });

        socket.connect();
        return socket;
    }

}
