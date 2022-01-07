import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  Link
} from "react-router-dom";
import { useAuth, authFetch, login, logout } from "./auth"

const checkAuth = () => {
  const auth_key = localStorage.getItem('REACT_TOKEN_AUTH_KEY');
  if (auth_key) {
    return true;
  } else {
    return false;
  }
}

const PrivateRoute = ({ children, session }) => {
  const isAuthenticated = checkAuth();
  console.log(isAuthenticated);
  return isAuthenticated ? children : <Navigate to='/login' />;
}

export default function App() {

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/secret">Secret</Link>
            </li>
          </ul>
        </nav>

        {/* <Routes> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Routes>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/secret" element={<PrivateRoute><Secret /></PrivateRoute>}></Route>
          <Route path="/" element={<Home />}></Route>
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function Login() {

  const [logged, session] = useAuth()
  console.log(session)
  console.log(logged)

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const onSubmitClick = (e) => {
    e.preventDefault()
    console.log("You pressed login")
    let opts = {
      'username': username,
      'password': password
    }
    console.log(opts)
    fetch('/api/login', {
      method: 'post',
      body: JSON.stringify(opts)
    }).then(r => r.json())
      .then(token => {
        if (token.access_token) {
          login(token)
          console.log(token)
        }
        else {
          console.log("Please type in correct username/password")
        }
      })
  }

  const handleUsernameChange = (e) => {
    setUsername(e.target.value)
  }

  const handlePasswordChange = (e) => {
    setPassword(e.target.value)
  }

  return (
    <div>
      <h2>Login</h2>
      {!logged ? <form action="#">
        <div>
          <input type="text"
            placeholder="Username"
            onChange={handleUsernameChange}
            value={username}
          />
        </div>
        <div>
          <input
            type="password"
            placeholder="Password"
            onChange={handlePasswordChange}
            value={password}
          />
        </div>
        <button onClick={onSubmitClick} type="submit">
          Login Now
        </button>
      </form>
        : <button onClick={() => logout()}>Logout</button>}
    </div>
  )
}

function Secret() {

  const [message, setMessage] = useState('')

  useEffect(() => {
    authFetch("/api/protected").then(response => {
      if (response.status === 401) {
        setMessage("Sorry you aren't authorized!")
        return null
      }
      return response.json()
    }).then(response => {
      if (response && response.message) {
        setMessage(response.message)
      }
    })
  }, [])
  return (
    <h2>Secret: {message}</h2>
  )
}