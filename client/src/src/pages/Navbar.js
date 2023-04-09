import {Link} from "react-router-dom"
import { Row, Col} from "react-bootstrap";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import '../style/navbar-style.css'

const AppNavbar = () =>{
    return(
        <div className="nav-bar">
            <Navbar  expand="lg">
            <Container>
                <Row>
                    <div className="navbar-items">
                    <div className="title">
                    <Link to="/">
                        Smart Garden
                    </Link>
                </div>
                
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link to="/ControlPanel">Control Panel</Link>
                        <Link to="/SimController">Sim Controller</Link>
                    </Nav>
                </Navbar.Collapse>
                </div>
                </Row>
            </Container>
            </Navbar>
        </div>
    )
}

export default AppNavbar;