import React, { useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:8080', {
  autoConnect: true,
  transports: ['websocket', 'polling']
});


const DataSocketComponent =({data, setData})=>{

    socket.emit("data_from_server","send_data");

    useEffect(()=>{
        socket.on('data_from_server', (sensorDataJson) => {
        var sensorData = JSON.parse(sensorDataJson);
        setData(currentData => [...currentData,sensorData]);
        });
    }, []);

    useEffect(() =>{
        if (data.length > 1000){
        setData(currentData =>[...currentData.slice(1)])
        }
    })
}

export default DataSocketComponent;

