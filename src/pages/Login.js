import React from 'react';

import '../index.css'

import { Navigate } from 'react-router-dom';
import { GoogleLogin } from 'react-google-login';
import { useAuth } from '../auth/Authentication';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

function handleLoginFailure(err) {
    console.log('failed to log in');
    console.log(err);
}

function Login() {

    const { authed, login } = useAuth();

    return (
        <div>
            {authed ? (<Navigate to='/' />) : (
                <>
                    <h2>Log in Page</h2>
                    <GoogleLogin
                        clientId={googleClientId}
                        buttonText='Sign In with Google'
                        onSuccess={login}
                        onFailure={handleLoginFailure}
                        cookiePolicy={'single_host_origin'}
                    />
                </>
            )}
        </div>
    );
}

export default Login;