import React from 'react';
import { Navigate } from 'react-router-dom'
import Button from '@material-ui/core/Button';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

class Login extends React.Component {

    constructor(props) {
        super(props);
        this.handleLogin = this.handleLogin.bind(this);
        this.handleLoginFailure = this.handleLoginFailure.bind(this);
    }

    async handleLogin(googleData) {
        console.log('successful login');
        console.log(googleData);

        // TODO: figure out if we want to automatically create user accounts
        // or redirect them to a page to create their own account

        // fetch user data for our backend 
        const resp = await fetch('/api/authenticate/google', {
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
        console.log(data);
        // TODO: figure out how to store the user
    }

    async handleLoginFailure(err) {
        console.log('failed login');
        console.log(err);
    }

    render() {

        if (false) {
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