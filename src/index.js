import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from 'history'

import { ThemeProvider } from '@mui/material';
import myTheme from './theme'
import Main from './Main';

const history = createBrowserHistory();

ReactDOM.render((
		<ThemeProvider theme={myTheme}>
			<Main history={history} />
		</ThemeProvider>
), document.getElementById('root'))
