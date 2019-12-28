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
import DeveloperOutlinedIcon from '@material-ui/icons/DeveloperModeOutlined';
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

function ForgotPasswordPage(props) {
  function handleSubmit(event) {
    event.preventDefault();

    // Get user inputs (TODO:)
    const reset_code = event.target[0].value;
    const new_password = event.target[2].value;

    // Quick validation
    if (!reset_code || !new_password) return;

    // Send to backend
    axios.post(`/auth/passwordreset/reset`, { reset_code, new_password })
      .then((response) => {
        console.log(response);
        props.history.push('/login');
      })
      .catch((err) => {});
  }

  const classes = useStyles();

  return (
    <Container component="main" maxWidth="sm">
      <Box boxShadow={3} className={classes.card}>
        <Avatar>
          <DeveloperOutlinedIcon color="secondary" />
        </Avatar>
        <Typography component="h1" variant="h5">
          Reset Password
        </Typography>
        <form noValidate onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="reset_code"
            label="Reset code"
            name="reset_code"
            type="text"
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="new_password"
            label="New Password"
            name="new_password"
            type="password"
          />
          <Button type="submit" fullWidth variant="contained" color="primary">
            Change Password
          </Button>
          <Grid container>
            <Grid item>
              <br />
              <Link href="/login" variant="body1">
                {'Remember your password? Login'}
              </Link>
            </Grid>
          </Grid>
        </form>
      </Box>
    </Container>
  );
}

export default ForgotPasswordPage;
