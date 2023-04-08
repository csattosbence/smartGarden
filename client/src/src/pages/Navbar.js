import {Link} from "react-router-dom"

const Navbar = () =>{
    return(
        <nav>
            <Link to="/" className="site-title">
                Smart Garden
            </Link>
            <ul>
                <li>
                    <Link to="/ControlPanel">Control Panel</Link>
                </li>
                <li>
                    <Link to="/SimController">Sim Controller</Link>
                </li>
            </ul>

        </nav>
    )
}

export default Navbar;