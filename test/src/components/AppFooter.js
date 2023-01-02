import React from "react";
import { FaSkull } from 'react-icons/fa'
import './AppFooter.css';


class AppFooter extends React.Component {
  render() {
    return (
        <footer className='app-footer'>
          <div className="footer-icon-container">
            <FaSkull className="footer-icon"/>
          </div>
          <p className='footer-title'>CS Development</p>
        </footer>
      );
  }
}

export default AppFooter;