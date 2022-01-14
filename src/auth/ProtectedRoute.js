import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from './Authentication'

const ProtectedRoute = ({ children }) => {
    // check if the user is authenticated
    const { authed } = useAuth(); 
    return authed ? children : <Navigate to='/' />
}

export default ProtectedRoute;