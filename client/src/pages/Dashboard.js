import React from 'react';
import { Container } from '@mui/material';

class Dashboard extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Container maxWidth="xl">
                <h2>Dashboard Page</h2>
            </Container>
        )
    }
}

export default Dashboard;