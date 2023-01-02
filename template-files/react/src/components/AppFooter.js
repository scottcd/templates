import React from "react";
import { FaSkull } from 'react-icons/fa'
import './AppFooter.css';
import { COLORS } from '../values/colors.js'


class AppFooter extends React.Component {
  render() {
    return (
      <footer className='app-footer' style={{
        backgroundColor: COLORS.secondaryBackground,
        color: COLORS.secondaryText
      }}>
        <div className="footer-icon-container">
          <FaSkull className="footer-icon" style={{
            color: COLORS.highlightColor
          }} />
        </div>
        <p className='footer-title'>CS Development</p>
      </footer>
    );
  }
}

export default AppFooter;