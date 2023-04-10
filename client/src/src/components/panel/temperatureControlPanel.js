import '../../style/current-panels.css'
import upArrow from '../../icons/up-arrow.png'
import downArrow from '../../icons/down-arrow.png'
import { Col, Row } from 'react-bootstrap';
import axios from 'axios';
import { useEffect, useState} from 'react';
import ToggleButton from 'react-bootstrap/ToggleButton';
import tempIcon from '../../icons/Temperature.svg';



const  TemperatureControlPanel = () => {
  
  const [desiredTemperature, setDesiredTemperature] = useState(0);
  const [heaterStatus, setHeaterStatus] = useState(false)
  const [checked, setChecked] = useState();
  

  useEffect(() => {
    axios.get('/getConsumerStatus')
    .then(response => {
      setDesiredTemperature(response.data.desiredTemperature);
      setChecked(response.data.heaterStatus);
    })
    .catch(error => {
      console.log(error);
    });
  },[]);

  useEffect(() => {
    if(checked){
      axios.get('/setHeater?temperature=' + desiredTemperature)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },[desiredTemperature]);

  useEffect(()=>{
    if(checked){
      axios.get('/setHeater?temperature=' + desiredTemperature)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }else if(!checked){
      axios.get('/turnOffHeater')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }

  },[checked])

  const onClickUpArrow = () => {
    setDesiredTemperature(desiredTemperature + 1);
  }

  const onClickDownArrow = () => {
    setDesiredTemperature(desiredTemperature - 1);
  }
      
  return(
    <div className='controller-panel'>
    <Row className='justify-content-center text-align-center'>
        <img src={tempIcon} className='icon'></img>
        <h3>Temperature</h3>
      
    </Row>
    <Row>
      <Col>
        <h2>{desiredTemperature}°C</h2>
      </Col>
      <Col>
        <ToggleButton
            className="mb-2"
            id="temp-switch-button"
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

export default TemperatureControlPanel;