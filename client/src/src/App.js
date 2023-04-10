import { useEffect, useState } from "react";
import {Route, Routes} from "react-router-dom"
import DataSocketComponent from "./components/dataSocket";
import Dashboard from "./pages/Dashboard";
import SimController from "./pages/SimController"
import ControlPanel from "./pages/ControlPanel"
import AppNavbar from "./pages/Navbar";
import { Row, Col} from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';





function App() {
  const [data, setData] = useState([]);


  


  return (
    <div className="App">
      <DataSocketComponent data={data} setData={setData}/>
      <AppNavbar/>
      <div className="container">
            <Routes>
              <Route path="/" element={<Dashboard data={data}/>} />
              <Route path="/simController" element={<SimController />} />
              <Route path="/ControlPanel" element={<ControlPanel />} />
            </Routes>
      </div>
      
    </div>
  );
}

export default App;
