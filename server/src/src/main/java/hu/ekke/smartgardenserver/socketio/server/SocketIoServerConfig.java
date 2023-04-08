package hu.ekke.smartgardenserver.socketio.server;

import com.google.gson.Gson;
import hu.ekke.smartgardenserver.cache.Cache;
import io.socket.engineio.server.EngineIoServer;
import io.socket.engineio.server.EngineIoServerOptions;
import io.socket.socketio.server.*;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@Slf4j
public class SocketIoServerConfig {

    private final String ALL = "/";

    @Bean
    public EngineIoServer engineIoServer(){
        EngineIoServerOptions options = EngineIoServerOptions.newFromDefault();
        options.setAllowedCorsOrigins(new String[]{"*"});
        options.setAllowSyncPolling(true);
        options.setPingTimeout(300000000);
        return new EngineIoServer(options);
    }

    @Bean
    public SocketIoServer socketIoServer(EngineIoServer engineIoServer){
        return new SocketIoServer(engineIoServer);

    }

    @Bean
    SocketIoNamespace namespace(SocketIoServer socketIoServer){
        SocketIoNamespace nsAll = socketIoServer.namespace(ALL);
        SocketIoAdapter adapter = new SocketIoMemoryAdapter.Factory().createAdapter(nsAll);
        Gson gson = new Gson();
        nsAll.on("connection", connectionArgs -> {
            SocketIoSocket socket = (SocketIoSocket) connectionArgs[0];

            log.info("--------------------- User Connected ---------------------");
            socket.send("my_event", "Hello World!");

            socket.on("disconnect", args ->{
                log.info("--------------------- User Disconnected ---------------------");
            });




            socket.on("data_from_server", args -> {
                if (!Cache.cache.isEmpty()) {
                    while (true) {
                        try {
                            Thread.sleep(1000);
                            socket.send("data_from_server", gson.toJson(Cache.cache.get(Cache.cache.size() - 1)));
                        } catch (Exception e) {
                            break;
                        }
                    }
                }
            });
        });
        return nsAll;
    }

}
