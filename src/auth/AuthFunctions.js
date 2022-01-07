const isAuthenticated = () => {
    if (localStorage.getItem('CruiserToken')) {
        return true;
    } else {
        return false;
    }
}

const getAuthToken = () => {
    const cruiserToken = localStorage.getItem('CruiserToken');
    if (cruiserToken) {
        return cruiserToken.getItem('access_token');
    } else {
        return null;
    }
}

export { isAuthenticated, getAuthToken }