import '../../style/current-panels.css'
import upArrow from '../../icons/up-arrow.png'
import downArrow from '../../icons/down-arrow.png'
import { Col, Row } from 'react-bootstrap';
import axios from 'axios';
import { useEffect, useState} from 'react';
import ToggleButton from 'react-bootstrap/ToggleButton';
import lightIcon from '../../icons/Light.svg';



const LightControlPanel = () => {
  
  const [desiredLight, setDesiredLight] = useState(0);
  const [lightStatus, setLightStatus] = useState(false)
  const [checked, setChecked] = useState();
  

  useEffect(() => {
    axios.get('/getConsumerStatus')
    .then(response => {
        setDesiredLight(response.data.desiredLight);
        setChecked(response.data.lightStatus);
    })
    .catch(error => {
      console.log(error);
    });
  },[]);

  useEffect(() => {
    if(checked){
      axios.get('/setLight?light=' + desiredLight)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },[desiredLight]);

  useEffect(()=>{
    if(checked){
      axios.get('/setLight?light=' + desiredLight)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }else if(!checked){
      axios.get('/turnOffLight')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }

  },[checked])

  const onClickUpArrow = () => {
    setDesiredLight(desiredLight + 1);
  }

  const onClickDownArrow = () => {
    setDesiredLight(desiredLight - 1);
  }
      
  return(
    <div className='controller-panel'>
    <Row className='justify-content-center text-align-center'>
        <img src={lightIcon} className='icon'></img>
        <h3>Light</h3>
      
    </Row>
    <Row>
      <Col>
        <h2>{desiredLight}Lux</h2>
      </Col>
      <Col>
        <ToggleButton
            className="mb-2"
            id="light-switch-button"
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

export default LightControlPanel;