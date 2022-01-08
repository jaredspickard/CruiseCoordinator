import React from 'react';
import NavBar from '../components/NavBar'
import { Button } from '@mui/material';
import { authFetch } from '../auth/AuthFunctions'

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.testProtected = this.testProtected.bind(this);
    }

    testProtected() {
        authFetch('/api/protected').then(resp => console.log(resp));
    }

    render() {
        return (
            <div>
                <NavBar />
                <h2>Home Page</h2>
                <Button onClick={() => this.testProtected()}>Test Protected API</Button>
            </div>
        )
    }
}

export default Home;