import React from "react";
import { Link } from "react-router-dom";
import { FaArrowLeft } from 'react-icons/fa'
import './Navbar.css';


class Navbar extends React.Component {
  render() {
    return (
      <div className='navBar' >
        <div className="navBar-header">
          <FaArrowLeft className='navBar-header-icon' onClick={this.props.toggleNav}/>
          <h3 className="navBar-header-title">Views</h3>
        </div>
        <div className="navBar-links">
          <Link className="navBar-link" to="/">Home</Link>
          <Link className="navBar-link" to="/two">Placeholder</Link>
        </div>
      </div>
    );
  }
}

export default Navbar;