import { Grid } from "@mui/material";
import FriendRequestCard from "./FriendRequestCard";

export default function FriendRequestCardList() {
    return (
        <div justifyContent="center">
            <Grid container justifyContent="space-evenly" spacing={1.5}>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <FriendRequestCard username="jaredspickard" email="jaredspickard@gmail.com" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <FriendRequestCard username="jaredspickard2" email="jaredspickard@gmail.com" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <FriendRequestCard username="jaredspickard3" email="jaredspickard@gmail.com" />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <FriendRequestCard username="jaredspickard4" email="jaredspickard@gmail.com" />
                </Grid>
            </Grid>
        </div>
    );
}