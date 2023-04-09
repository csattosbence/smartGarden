package hu.ekke.smartgardenserver.cache;

import hu.ekke.smartgardenserver.model.SensorData;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.LinkedList;
import java.util.List;

@Slf4j
@Service
public class Cache {
    private static final List<SensorData> cache = new LinkedList<>();

    public static void addToCache(SensorData element){
        cache.add(element);
        log.info("element added to cache");
    }

    public static List<SensorData> getCache(){
        return cache;
    }
}
