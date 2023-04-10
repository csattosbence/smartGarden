import { Row, Col} from "react-bootstrap";
import "../../style/dashboard-panel.css"
import HumidityControlPanel from "../panel/humidityControlPanel";
import HumidityChart from "../charts/humidityChart";



const HumidityPanel = ({data}) => {

  return (
   <div className="dashboard-panel">
    <Row>
      <Col xs={3}>
        <HumidityControlPanel/>  
      </Col>  
      <Col xs={9}>
        <HumidityChart data={data}/>
      </Col>
    </Row>
   </div>
  );
}

export default HumidityPanel;

