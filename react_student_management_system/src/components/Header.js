import './Header.css';
import logo from '../images/rnsit_cse_cover.jpeg';
import rns from '../images/rns.jpeg';

function Header(){

    return(
        <header>
            <img id='logo1' src={rns}/>
            <img id='logo2' src={logo}/>
        </header>
    );

}

export default Header;