import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import { createBrowserHistory } from 'history'

import { ThemeProvider } from '@mui/material';
import myTheme from './theme'
import Main from './Main';
import { AuthProvider } from './auth/Authentication';

const history = createBrowserHistory();

ReactDOM.render((
	<ThemeProvider theme={myTheme}>
		<Router>
			<AuthProvider>
				<Main history={history} />
			</AuthProvider>
		</Router>
	</ThemeProvider>
), document.getElementById('root'))
