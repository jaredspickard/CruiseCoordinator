import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from 'react-router-dom'

import Login from '../pages/Login';
import Home from '../pages/Home';
import Trips from '../pages/Trips';
import About from '../pages/About';

class Main extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path="login" element={<Login />}></Route>
                    <Route path="/" element={<Home />}></Route>
                    <Route path="/trips" element={<Trips />}></Route>
                    <Route path="/about" element={<About />}></Route>
                </Routes>
            </Router>
        );
    }
}

export default Main;