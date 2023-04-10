import { Row, Col} from "react-bootstrap";
import TemperaturePanel from "../components/panel/temperaturePanel";
import HumidityPanel from "../components/panel/humidityPanel";
import LightPanel from "../components/panel/lightPanel";
import SoilMoisturePanel from "../components/panel/soilMoistPanel";



const Dashboard = ({data}) => {

  return (
    <div className="chart-container ">
      <Row className="justify-content-center">
        <Col>
          <TemperaturePanel data={data}/>
        </Col>
      </Row>
      <Row className="justify-content-center">
        <Col>
          <HumidityPanel data={data}/>
        </Col>
      </Row>
      <Row className="justify-content-center">
        <Col>
          <LightPanel data={data}/>
        </Col>
      </Row>
      <Row className="justify-content-center">
        <Col>
          <SoilMoisturePanel data={data}/>
        </Col>
      </Row>
    </div>
  );
}

export default Dashboard;
