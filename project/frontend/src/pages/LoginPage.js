import axios from 'axios';
import {
  Avatar,
  Box,
  Button,
  Container,
  Grid,
  Link,
  makeStyles,
  TextField,
  Typography,
} from '@material-ui/core';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import React from 'react';

const useStyles = makeStyles((theme) => ({
  '@global': {
    body: {
      backgroundColor: theme.palette.primary.light,
    },
  },
  card: {
    backgroundColor: theme.palette.background.paper,
    marginTop: theme.spacing(8),
    padding: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    borderRadius: theme.shape.borderRadius,
  },
}));

function LoginPage({ setAuth, ...props }) {
  function handleSubmit(event) {
    event.preventDefault();

    // Get user inputs (TODO:)
    const email = event.target[0].value;
    const password = event.target[2].value;

    // Quick validation
    if (!email || !password) return;

    // Send to backend
    axios.post(`/auth/login`, { email, password })
      .then((response) => {
        console.log(response);
        const data = response.data;
        setAuth(data.token, data.u_id);
        props.history.push('/');
      })
      .catch((err) => {});
  }

  const classes = useStyles();

  return (
    <Container component="main" maxWidth="sm">
      <Box boxShadow={3} className={classes.card}>
        <Avatar>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Login
        </Typography>
        <form noValidate onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email"
            name="email"
            type="text"
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button type="submit" fullWidth variant="contained" color="primary">
            Sign In
          </Button>
          <Grid container direction="column" alignItems="center">
            <Grid item>
              <br />
              <Link href="/register" variant="body1">
                {"Don't have an account? Register"}
              </Link>
            </Grid>
            <Grid item>
              <br />
              <Link href="/forgot_password" variant="body1">
                Forgot password?
              </Link>
            </Grid>
          </Grid>
        </form>
      </Box>
    </Container>
  );
}

export default LoginPage;
