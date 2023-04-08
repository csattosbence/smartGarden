import HumidityChart from "../components/charts/humidityChart";
import LightChart from "../components/charts/lightChart";
import SoilMoistChart from "../components/charts/soilMoistChart";
import TempChart from "../components/charts/tempChart";
import { Row, Col} from "react-bootstrap";



const Home = ({data}) => {

  return (
    <div className="chart-container text-align-center">
      <Row className="justify-content-center">
        <Col>
          
        </Col>
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

export default Home;
