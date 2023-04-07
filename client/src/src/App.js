import { useEffect, useState } from "react";
import io from 'socket.io-client';
import {
  Line,
  LineChart,
  XAxis,
  YAxis,
} from 'recharts';


const socket = io('http://localhost:8080', {
  autoConnect: true,
  transports: ['websocket', 'polling']
});

function App() {


  const [data, setData] = useState([]);

  

  socket.emit("data_from_server","send_data");

  useEffect(()=>{
    socket.on('data_from_server', (sensorDataJson) => {
      var sensorData = JSON.parse(sensorDataJson);
      setData(currentData => [...currentData,sensorData]);
    });
  }, []);

  

  return (
    <div className="App">
      <LineChart width={500} height={300} data={data}>
        <XAxis dataKey="currentDate"/>
        <YAxis dataKey="temperature"/>
        <Line type="monotone" dataKey="temperature" stroke="#8884d8" />
      </LineChart>
    </div>
  );
}

export default App;
