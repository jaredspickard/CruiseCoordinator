import React from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated } from './AuthFunctions';

const ProtectedRoute = ({ children }) => {
    const auth = isAuthenticated();
    return auth ? children : <Navigate to='/login' />;
}

export default ProtectedRoute;