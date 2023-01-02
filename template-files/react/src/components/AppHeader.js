import React from "react";
import { FaBars } from 'react-icons/fa'
import './AppHeader.css';
import { COLORS } from '../values/colors.js'

class AppHeader extends React.Component {
  render() {
    return (
      <header className='app-header' style={{
        backgroundColor: COLORS.secondaryBackground,
        color: COLORS.secondaryText
      }}>
        <div className='header-icon-container' onClick={() => {
          this.props.toggleNav();
        }}>
          <FaBars className='header-icon' style={{
            color: COLORS.highlightColor
          }} />
        </div>
        <div className='header-title-container'>
          <h1 className="header-title">A Fantastic Website</h1>
        </div>
      </header>
    );
  }
}

export default AppHeader;