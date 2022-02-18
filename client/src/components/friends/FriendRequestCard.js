import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Gravatar from 'react-gravatar';

export default function FriendRequestCard() {
  return (
    <Card sx={{ width: 250 }}>
      <CardMedia display="flex" justifyContent="center">
          <Gravatar email="jaredspickard@gmail.com" size={250} />
      </CardMedia>
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          jaredspickard
        </Typography>
      </CardContent>
      <CardActions justifyContent="space-between">
        <Button size="small">Accept</Button>
        <Button size="small">Decline</Button>
      </CardActions>
    </Card>
  );
}
