import React from 'react';
import { GoogleLogin } from 'react-google-login';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.checkGoogleAvailability = this.checkGoogleAvailability.bind(this);
    }

    async checkGoogleAvailability(googleData) {
        const resp = await fetch('/api/external_account/available/google/' + googleData.tokenId);
        const data = await resp.json()
        console.log(data);
    }

    render() {
        return (
            <div>
                <h2>Landing Page</h2>
                <GoogleLogin
                    variant="contained"
                    color="primary"
                    clientId={googleClientId}
                    buttonText='Check account availability'
                    onSuccess={this.checkGoogleAvailability}
                    cookiePolicy={'single_host_origin'}
                />
            </div>
        )
    }
}

export default Home;