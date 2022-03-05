import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Container } from '@mui/material';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

class Home extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Container maxWidth="xl">
                <h2>Landing Page</h2>
            </Container>
        )
    }
}

export default Home;