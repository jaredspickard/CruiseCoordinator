import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import { GoogleLogin } from 'react-google-login';
import { useAuth } from '../auth/Authentication';
import { Stack } from '@mui/material';

const googleClientId = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'

function handleLoginFailure(err) {
  console.log('failed to log in');
  console.log(err);
}

export default function LoginModal() {

  const { login } = useAuth();

  const [open, setOpen] = React.useState(false);

  const [email, setEmail] = React.useState("");

  const [password, setPassword] = React.useState("");

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailLogin = async () => {
    login(email, password)
  }

  return (
    <div>
      <Button color="inherit" variant="outlined" onClick={handleClickOpen}>
        Log in
      </Button>
      <Dialog open={open} onClose={handleClose} maxWidth="xs">
        <DialogTitle>Log in to CruiseCoordinator</DialogTitle>
        <DialogContent>
          <Stack spacing={2}>
            {/* <GoogleLogin
                variant="contained"
                color="primary"
                clientId={googleClientId}
                buttonText='Continue with Google'
                onSuccess={login}
                onFailure={handleLoginFailure}
                cookiePolicy={'single_host_origin'}
              /> */}
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Email</InputLabel>
              <Input id="login-email" value={email} onChange={handleEmailChange} />
            </FormControl>
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Password</InputLabel>
              <Input id="login-password" type="password" value={password} onChange={handlePasswordChange} />
            </FormControl>
            <Button variant="contained" onClick={handleEmailLogin}>Login</Button>
          </Stack>
        </DialogContent>
      </Dialog>
    </div>
  );
}
