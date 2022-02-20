import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Gravatar from 'react-gravatar';
import GroupAddIcon from '@mui/icons-material/GroupAdd';
import PersonRemoveIcon from '@mui/icons-material/PersonRemove';

export default function FriendRequestCard() {
    return (
        <Card sx={{ width: 250 }}>
            <CardMedia align='center'>
                <Gravatar email="jaredspickard@gmail.com" size={225} />
            </CardMedia>
            <CardContent>
                <Typography variant="h6" component="div" align='center' noWrap='true'>
                    jaredspickard
                </Typography>
            </CardContent>
            <CardActions>
                <Button fullWidth variant="outlined" startIcon={<GroupAddIcon />}>Accept</Button>
                <Button fullWidth variant="outlined" color="secondary" endIcon={<PersonRemoveIcon />}>Decline</Button>
            </CardActions>
        </Card>
    );
}
