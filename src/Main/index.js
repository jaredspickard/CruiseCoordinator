import React from 'react';
import { Routes, Route } from 'react-router-dom'
import '../index.css'

import { useAuth } from '../auth/Authentication'
import NavBar from '../components/NavBar';
import Home from '../pages/Home';
import Dashboard from '../pages/Dashboard';
import Trips from '../pages/Trips';
import About from '../pages/About';
import Profile from '../pages/Profile';
import ProtectedRoute from '../auth/ProtectedRoute';

function Main() {

    const { loading } = useAuth();

    return (
        <div className='ROOT'>
            <NavBar />
            {loading ? (
                <div> Loading... </div>
            ) : (
            <Routes>
                <Route path="/" element={<Home />}></Route>
                <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>}></Route>
                <Route path="/trips" element={<ProtectedRoute><Trips /></ProtectedRoute>}></Route>
                <Route path="/about" element={<ProtectedRoute><About /></ProtectedRoute>}></Route>
                <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>}></Route>
            </Routes>
            )}
        </div>
    );
}

export default Main;