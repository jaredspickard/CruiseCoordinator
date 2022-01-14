import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';


export default function Footer(props) {
    return (
        <AppBar position="static" color="secondary">
            <Container maxWidth="md">
                <Toolbar>
                    <Typography variant="body2" color="text.secondary" align="center" {...props}>
                        {'Copyright © '}
                        <Link color="inherit" href="https://cruisecoordinator.com/">
                            CruiseCoordinator
                        </Link>{' '}
                        {new Date().getFullYear()}
                        {'.'}
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    )
}