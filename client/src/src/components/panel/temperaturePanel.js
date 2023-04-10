import { Row, Col} from "react-bootstrap";
import TemperatureControlPanel from "./temperatureControlPanel";
import TempChart from "../charts/tempChart";
import "../../style/dashboard-panel.css"



const TemperaturePanel = ({data}) => {

  return (
   <div className="dashboard-panel">
    <Row>
      <Col xs={3}>
        <TemperatureControlPanel/>  
      </Col>  
      <Col xs={9}>
        <TempChart data={data}/>
      </Col>
    </Row>
   </div>
  );
}

export default TemperaturePanel;

