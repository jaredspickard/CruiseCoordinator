import MenuItem from '@mui/material/MenuItem';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';

const logout = () => {
    console.log('Logging Out User');
    localStorage.removeItem('CruiserToken');
}

const LogoutButton = () => {
    return (
        <MenuItem key='logout_button' onClick={logout} component={Link} to="/login">
            <Typography textAlign="center">Logout</Typography>
        </MenuItem>
    );
};

export default LogoutButton;