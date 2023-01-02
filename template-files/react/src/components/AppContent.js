import React from 'react';
import { Routes, Route } from 'react-router-dom'
import Home from '../views/Home'
import Two from '../views/Two'
import { COLORS } from '../values/colors.js'

class AppContent extends React.Component {
    render() {
        return (
            <div className='app-content' style={{
                backgroundColor: COLORS.primaryBackground,
                color: COLORS.primaryText
            }}>
                <Routes>
                    <Route path="/" element={Home()} exact />
                    <Route path="/two" element={Two()} />
                </Routes>
            </div>
        );
    }
}

export default AppContent;