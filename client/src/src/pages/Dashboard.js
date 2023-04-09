import HumidityChart from "../components/charts/humidityChart";
import LightChart from "../components/charts/lightChart";
import SoilMoistChart from "../components/charts/soilMoistChart";
import TempChart from "../components/charts/tempChart";
import { Row, Col} from "react-bootstrap";
import CurrentHumididtyPanel from "../components/panel/humidityPanel";



const Dashboard = ({data}) => {

  return (
    <div className="chart-container text-align-center">
      <Row className="justify-content-center">
        <CurrentHumididtyPanel data={data}/>
      </Row>
      <Row className="justify-content-center">
        <Col >
            <TempChart data={data}/>
        </Col>
        <Col>
          <SoilMoistChart data={data}/>
        </Col>
      </Row>
      <Row className="justify-content-center">
        <Col >
          <LightChart data={data}/>
        </Col>
        <Col>
          <HumidityChart data={data}/>
        </Col>
      </Row>
    </div>
  );
}

export default Dashboard;
