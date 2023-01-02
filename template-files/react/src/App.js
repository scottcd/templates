import React from 'react';
import './App.css';
import Navbar from './components/Navbar'
import AppHeader from './components/AppHeader'
import AppContent from './components/AppContent'
import AppFooter from './components/AppFooter'


class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      navOpen: false,
    }

    this.toggleNav = this.toggleNav.bind(this);
  }

  toggleNav = () => {
    this.setState({ navOpen: !this.state.navOpen });
  }

  // if nav menu is open and we click outside of it, close the nav menu.
  handlNavClose = (event) => {
    if (this.state.navOpen === true && event.target.className !== 'navBar') {
      this.setState({ 
        navOpen: false,  
      });
    }
  }

  render() {
    return (
      <div className='app-shell' onClick={this.handlNavClose}>
        <AppHeader toggleNav={this.toggleNav}/>
        <AppContent />
        <AppFooter />
        {this.state.navOpen ? <Navbar toggleNav={this.toggleNav}/> : null}
      </div>
    );
  }
}

export default App;
