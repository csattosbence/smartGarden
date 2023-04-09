import '../../style/current-panels.css'
import { Col } from 'react-bootstrap';

const CurrentHumididtyPanel = ({data}) =>{
    
    var currentTemp = 0;
    if(data.length !== 0){
        var b = data.slice(-1);
        var currentTemp = b[0].temperature
    }
    
    return(
        <Col xs={4}>
            <div className='current-panels'>
                <h3>{currentTemp}°C</h3>
            </div>
        </Col>
    )
} 

export default CurrentHumididtyPanel;