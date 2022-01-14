import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import { Link } from 'react-router-dom';
import LogoutButton from '../components/LogoutButton'
import { useAuth } from '../auth/Authentication';
import LoginModal from './LoginModal';
import SignUpModal from './SignUpModal';


const NavBar = () => {

    const { authed } = useAuth();

    const [anchorElNav, setAnchorElNav] = React.useState(null);
    const [anchorElUser, setAnchorElUser] = React.useState(null);

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget);
    };
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    return (
        <AppBar position="static">
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{ mr: 2, display: { xs: 'none', md: 'flex' } }}
                    >
                        CruiseCoordinator
                    </Typography>

                    <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
                        <IconButton
                            size="large"
                            aria-label="account of current user"
                            aria-controls="menu-appbar"
                            aria-haspopup="true"
                            onClick={handleOpenNavMenu}
                            color="inherit"
                        >
                            <MenuIcon />
                        </IconButton>
                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorElNav}
                            anchorOrigin={{
                                vertical: 'bottom',
                                horizontal: 'left',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'left',
                            }}
                            open={Boolean(anchorElNav)}
                            onClose={handleCloseNavMenu}
                            sx={{
                                display: { xs: 'block', md: 'none' },
                            }}
                        >
                            <MenuItem key="dashboard_page" onClick={handleCloseNavMenu} component={Link} to="/dashboard">
                                <Typography textAlign="center">Dashboard</Typography>
                            </MenuItem>
                            <MenuItem key="trips_page" onClick={handleCloseNavMenu} component={Link} to="/trips">
                                <Typography textAlign="center">Trips</Typography>
                            </MenuItem>
                            <MenuItem key="about_page" onClick={handleCloseNavMenu} component={Link} to="/about">
                                <Typography textAlign="center">About</Typography>
                            </MenuItem>
                        </Menu>
                    </Box>
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}
                    >
                        CruiseCoordinator
                    </Typography>
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                        <Button key="dashboard_page" component={Link} to="/dashboard" sx={{ my: 2, color: 'white', display: 'block' }}>Dashboard</Button>
                        <Button key="trips_page" component={Link} to="/trips" sx={{ my: 2, color: 'white', display: 'block' }}>Trips</Button>
                        <Button key="about_page" component={Link} to="/about" sx={{ my: 2, color: 'white', display: 'block' }}>About</Button>
                    </Box>

                    {authed ? (
                        <>
                            <Box sx={{ flexGrow: 0 }}>
                                <Tooltip title="Open settings">
                                    <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                                        <Avatar alt="Remy Sharp" />
                                    </IconButton>
                                </Tooltip>
                                <Menu
                                    sx={{ mt: '45px' }}
                                    id="menu-appbar"
                                    anchorEl={anchorElUser}
                                    anchorOrigin={{
                                        vertical: 'top',
                                        horizontal: 'right',
                                    }}
                                    keepMounted
                                    transformOrigin={{
                                        vertical: 'top',
                                        horizontal: 'right',
                                    }}
                                    open={Boolean(anchorElUser)}
                                    onClose={handleCloseUserMenu}
                                >
                                    <MenuItem key='profile_menu_item' onClick={handleCloseUserMenu} component={Link} to="/profile">
                                        <Typography textAlign="center">Profile</Typography>
                                    </MenuItem>
                                    <LogoutButton />
                                </Menu>
                            </Box>
                        </>
                    ) : (
                        <>
                            <LoginModal />
                            <SignUpModal />
                        </>
                    )}
                </Toolbar>
            </Container>
        </AppBar>
    );
};

export default NavBar;
