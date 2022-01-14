import MenuItem from '@mui/material/MenuItem';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import { useAuth } from '../auth/Authentication';

const LogoutButton = () => {

    const { logout } = useAuth();

    return (
        <MenuItem key='logout_button' onClick={logout} component={Link} to="/login">
            <Typography textAlign="center">Logout</Typography>
        </MenuItem>
    );
};

export default LogoutButton;