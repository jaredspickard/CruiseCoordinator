import React from 'react';
import { Navigate } from 'react-router-dom'
import { GoogleLogin } from 'react-google-login';
import { isAuthenticated } from '../auth/AuthFunctions';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

class Login extends React.Component {

    constructor(props) {
        super(props);
        this.handleLogin = this.handleLogin.bind(this);
        this.handleLoginFailure = this.handleLoginFailure.bind(this);
    }

    async handleLogin(googleData) {

        // fetch user data for our backend 
        const resp = await fetch('/api/login/google', {
            method: 'POST',
            body: JSON.stringify({
                token: googleData.tokenId
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        //store the user in the client
        const data = await resp.json();
        if (data) {
            const token = data['access_token']
            localStorage.setItem('CruiserToken', token);
            this.setState({});
        }
    }

    async handleLoginFailure(err) {
        console.log('Failed to login');
        console.log(err);
    }

    render() {

        const auth = isAuthenticated();

        if (auth) {
            return <Navigate to='/' />
        } else {
            return (
                <div>
                    <h2>Login Page</h2>
                    <div>
                        <GoogleLogin
                            clientId={googleClientId}
                            buttonText='Login with Google'
                            onSuccess={this.handleLogin}
                            onFailure={this.handleLoginFailure}
                            cookiePolicy={'single_host_origin'}
                        />
                    </div>
                </div>
            )
        }
    }
}

export default Login;