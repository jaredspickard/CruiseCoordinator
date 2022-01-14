import React, { Component } from 'react';
import { Routes, Route } from 'react-router-dom'

import { useAuth } from '../auth/Authentication'
import Login from '../pages/Login';
import Home from '../pages/Home';
import Trips from '../pages/Trips';
import About from '../pages/About';
import Profile from '../pages/Profile';
import ProtectedRoute from '../auth/ProtectedRoute';
import NavBar from '../components/NavBar';

function Main() {

    const { loading } = useAuth();

    return (
        <div className='ROOT'>
            <NavBar />
            {loading ? (
                <div> Loading... </div>
            ) : (
            <Routes>
                <Route path="login" element={<Login />}></Route>
                <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>}></Route>
                <Route path="/trips" element={<ProtectedRoute><Trips /></ProtectedRoute>}></Route>
                <Route path="/about" element={<ProtectedRoute><About /></ProtectedRoute>}></Route>
                <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>}></Route>
            </Routes>
            )}
        </div>
    );
}

export default Main;