import React from 'react';
import { Navigate } from 'react-router-dom'
import Button from '@material-ui/core/Button';

class Login extends React.Component {

    constructor(props) {
        super(props);
        this.login = this.login.bind(this);
        this.authenticatedUser = this.authenticatedUser.bind(this);
    }

    async login() {
        // acquire ThirdPartyToken and save to localStorage
        await this.getThirdPartyToken();
        // acquire BackendToken using the ThirdPartyToken and save to localStorage
        await this.getBackendToken();
        // rerender the component so successful logins redirect to the home page
        this.setState({})
    }

    async getThirdPartyToken() {
        localStorage.setItem('thirdPartyToken', 'abcdef');
    }

    async getBackendToken() {
        const thirdPartyToken = localStorage.getItem('thirdPartyToken');
        if (!thirdPartyToken) {
            console.log('Unable to retrieve ThirdPartyToken.');
        }
        const backendToken = 'ghijk';
        localStorage.setItem('backendToken', backendToken);
    }

    authenticatedUser() {
        const backendToken = localStorage.getItem('backendToken');
        console.log(backendToken);
        console.log(Boolean(backendToken));
        return Boolean(backendToken);
    }

    render() {

        const auth = this.authenticatedUser()

        if (auth) {
            return <Navigate to='/' />
        } else {
            return (
                <div>
                    <h2>Login Page</h2>
                    <Button
                        variant='contained'
                        onClick={this.login}
                    >Login to "Google"</Button>
                </div>
            )
        }
    }
}

export default Login;