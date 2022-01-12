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

const authFetch = async (url, data={}) => {
    console.log(url)
    // set the auth token in the header
    const authToken = localStorage.getItem('CruiserToken');
    if (!authToken) {
        console.log('Unable to retrieve auth token.');
        return;
    }
    if (!data['headers']) {
        data['headers'] = {}
    }
    const headers = data['headers'];
    headers['Authorization'] = 'Bearer ' + authToken;
    console.log(data)
    return fetch(url, data).then(async resp => {
        if (resp.status === 401) {
            console.log('Unauthorized Request');
            return null;
        } else {
            return resp.json();
        }
    });
}

export { isAuthenticated, getAuthToken, authFetch }