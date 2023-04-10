import { Row, Col} from "react-bootstrap";
import "../../style/dashboard-panel.css"
import SoilMoistureControlPanel from "./soilMoistControlPanel";
import SoilMoistChart from "../charts/soilMoistChart"

const SoilMoisturePanel = ({data}) => {

  return (
   <div className="dashboard-panel">
    <Row>
      <Col xs={3}>
        <SoilMoistureControlPanel/>  
      </Col>  
      <Col xs={9}>
        <SoilMoistChart data={data}/>
      </Col>
    </Row>
   </div>
  );
}

export default SoilMoisturePanel;

