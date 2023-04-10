import { Row, Col} from "react-bootstrap";
import "../../style/dashboard-panel.css"
import LightControlPanel from "../panel/lightControlPanel";
import LightChart from "../charts/lightChart";


const LightPanel = ({data}) => {

  return (
   <div className="dashboard-panel">
    <Row>
      <Col xs={3}>
        <LightControlPanel/>  
      </Col>  
      <Col xs={9}>
        <LightChart data={data}/>
      </Col>
    </Row>
   </div>
  );
}

export default LightPanel;

