import React from 'react';
import ReactDOM from 'react-dom';
import { Router } from 'react-router-dom'
import { createBrowserHistory } from 'history'

import { ThemeProvider } from '@mui/material';
import myTheme from './theme'
import Main from './Main';
import App from './App';

// const history = createBrowserHistory();

// ReactDOM.render((
// 	<Router history={history}>
// 		<ThemeProvider theme={myTheme}>
// 			<Main history={history} />
// 		</ThemeProvider>
// 	</Router>
// ), document.getElementById('root'))

ReactDOM.render((
    <Main />
),
  document.getElementById('root'))
