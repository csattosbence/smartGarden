import '../../style/current-panels.css'
import upArrow from '../../icons/up-arrow.png'
import downArrow from '../../icons/down-arrow.png'
import { Col, Row } from 'react-bootstrap';
import axios from 'axios';
import { useEffect, useState} from 'react';
import ToggleButton from 'react-bootstrap/ToggleButton';
import humidityIcon from '../../icons/Humidity.svg';



const  HumidityControlPanel = () => {
  
  const [desiredHumidity, setDesiredHumidity] = useState(0);
  const [humidifierStatus, setHumidifierStatus] = useState(false)
  const [checked, setChecked] = useState();
  

  useEffect(() => {
    axios.get('/getConsumerStatus')
    .then(response => {
      setDesiredHumidity(response.data.desiredHumidity);
      setChecked(response.data.humidifierStatus);
    })
    .catch(error => {
      console.log(error);
    });
  },[]);

  useEffect(() => {
    if(checked){
      axios.get('/setHumidifier?humidity=' + desiredHumidity)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },[desiredHumidity]);

  useEffect(()=>{
    if(checked){
      axios.get('/setHumidifier?humidity=' + desiredHumidity)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }else if(!checked){
      axios.get('/turnOffHumidifier')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }

  },[checked])

  const onClickUpArrow = () => {
    setDesiredHumidity(desiredHumidity + 1);
  }

  const onClickDownArrow = () => {
    setDesiredHumidity(desiredHumidity - 1);
  }
      
  return(
    <div className='controller-panel'>
    <Row className='justify-content-center text-align-center'>
        <img src={humidityIcon} className='icon'></img>
        <h3>Humidity</h3>
      
    </Row>
    <Row>
      <Col>
        <h2>{desiredHumidity}%</h2>
      </Col>
      <Col>
        <ToggleButton
            className="mb-2"
            id="humidifier-switch-button"
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

export default HumidityControlPanel;