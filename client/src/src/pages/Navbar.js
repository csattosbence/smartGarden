import {Link} from "react-router-dom"
import { Row, Col} from "react-bootstrap";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

const AppNavbar = () =>{
    return(
        <Navbar bg="light" expand="lg">
            <Container>
                <Navbar.Brand>
                    <Link to="/">
                        Smart Garden
                    </Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link ><Link to="/ControlPanel">Control Panel</Link></Nav.Link>
                        <Nav.Link ><Link to="/SimController">Sim Controller</Link></Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
            </Navbar>
    )
}

export default AppNavbar;