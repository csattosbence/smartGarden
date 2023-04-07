package hu.ekke.smartgardenserver.socketio.server;

import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;

@Configuration
@EnableWebSocket
@Slf4j
public class EngineIoWebSocketConfigurer implements WebSocketConfigurer {
    private final EngineIoHandler engineIoHandler;


    public EngineIoWebSocketConfigurer(EngineIoHandler engineIoHandler) {
        this.engineIoHandler = engineIoHandler;
    }


    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        log.info("-------------REGISTRY HANDLER");
        registry.addHandler(engineIoHandler, "/socket.io/*")
                .addInterceptors(engineIoHandler)
                .setAllowedOrigins("*");
    }
}
