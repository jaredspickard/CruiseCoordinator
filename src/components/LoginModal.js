import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
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

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button color="inherit" variant="outlined" onClick={handleClickOpen}>
        Log in
      </Button>
      <Dialog open={open} onClose={handleClose} maxWidth="xs">
        <DialogTitle>Log in to CruiseCoordinator</DialogTitle>
        <DialogContent>
          <Stack spacing={2}>
              <GoogleLogin
                variant="contained"
                color="primary"
                clientId={googleClientId}
                buttonText='Continue with Google'
                onSuccess={login}
                onFailure={handleLoginFailure}
                cookiePolicy={'single_host_origin'}
              />
            <form>
              <label>username <input type="text" name="username"></input></label>
            </form>
            <Button variant="contained">Continue with email</Button>
          </Stack>
        </DialogContent>
      </Dialog>
    </div>
  );
}
