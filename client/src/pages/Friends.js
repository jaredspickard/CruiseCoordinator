import { Container } from '@mui/material';
import React from 'react';
import FriendsTabsPanel from '../components/friends/FriendsTabsPanel';

class Friends extends React.Component {
    render() {
        return (
            <Container maxWidth="xl">
                <h2>Friends Page</h2>
                <FriendsTabsPanel />
            </Container>
        )
    }
}

export default Friends;