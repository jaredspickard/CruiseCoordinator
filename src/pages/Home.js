import React from 'react';
import { Button } from '@mui/material';

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.testTripCreation = this.testTripCreation.bind(this);
    }

    testTripCreation() {
        const data = {};
        data['method'] = 'POST';
        data['body'] = JSON.stringify({
            token: 'token'
        });
        data['headers'] = {
            'Content-Type': 'application/json'
        };
        // authFetch('/api/trips/create', data).then(resp => console.log(resp));
        fetch('/api/trips/create', data).then(resp => console.log(resp));
    }

    render() {
        return (
            <div>
                <h2>Home Page</h2>
                <Button onClick={() => this.testTripCreation()}>Create Trip</Button>
            </div>
        )
    }
}

export default Home;