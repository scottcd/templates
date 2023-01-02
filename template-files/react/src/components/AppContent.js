import React from 'react';
import { Routes, Route } from 'react-router-dom'
import Home from '../views/Home'
import Two from '../views/Two'

class AppContent extends React.Component {
    render() {
        return (
            <div className='app-content'>
                <Routes>
                    <Route path="/" element={Home()} exact />
                    <Route path="/two" element={Two()} />
                </Routes>
            </div>
        );
    }
}

export default AppContent;