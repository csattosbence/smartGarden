import '../../style/current-panels.css'
import upArrow from '../../icons/up-arrow.png'
import downArrow from '../../icons/down-arrow.png'
import { Col, Row } from 'react-bootstrap';
import axios from 'axios';
import { useEffect, useState} from 'react';
import ToggleButton from 'react-bootstrap/ToggleButton';
import soilMoistIcon from '../../icons/Soil_moisture.svg';



const  SoilMoistureControlPanel = () => {
  
  const [desiredSoilMoisture, setDesiredSoilMoisture] = useState(0);
  const [waterSysStatus, setWaterSysStatus] = useState(false)
  const [checked, setChecked] = useState();
  

  useEffect(() => {
    axios.get('/getConsumerStatus')
    .then(response => {
        setDesiredSoilMoisture(response.data.desiredSoilMoisture);
        setChecked(response.data.waterSysStatus);
    })
    .catch(error => {
      console.log(error);
    });
  },[]);

  useEffect(() => {
    if(checked){
      axios.get('/setWateringSystem?soilMoist=' + desiredSoilMoisture)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },[desiredSoilMoisture]);

  useEffect(()=>{
    if(checked){
      axios.get('/setWateringSystem?soilMoist=' + desiredSoilMoisture)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }else if(!checked){
      axios.get('/turnOffWateringSystem')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }

  },[checked])

  const onClickUpArrow = () => {
    setDesiredSoilMoisture(desiredSoilMoisture + 1);
  }

  const onClickDownArrow = () => {
    setDesiredSoilMoisture(desiredSoilMoisture - 1);
  }
      
  return(
    <div className='controller-panel'>
    <Row className='justify-content-center text-align-center'>
        <img src={soilMoistIcon} className='icon'></img>
        <h3>Soil moisture</h3>
      
    </Row>
    <Row>
      <Col>
        <h2>{desiredSoilMoisture}%</h2>
      </Col>
      <Col>
        <ToggleButton
            className="mb-2"
            id="soil-moist-switch-button"
            type="checkbox"
            variant="outline-primary"
            checked={checked}
            value="1"
            onChange={(e) => setChecked(e.currentTarget.checked)}
        >
          {checked? "ON":"OFF"}
        </ToggleButton>
      </Col>
      <Col>
        <div className='up-arrow' onClick={onClickUpArrow} >
              <img className='arrow' src={upArrow}></img>
          </div>
          
          <div className='down-arrow' onClick={onClickDownArrow}>
              <img className='arrow' src={downArrow}></img>
          </div>
      </Col>
    </Row>
    </div>
  )
    
} 

export default SoilMoistureControlPanel;