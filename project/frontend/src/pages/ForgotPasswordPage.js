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
    const email = event.target[0].value;

    // Quick validation
    if (!email) return;

    // Send to backend
    axios.post(`/auth/passwordreset/request`, { email })
      .then((response) => {
        console.log(response);
        props.history.push('/reset_password');
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
          Forgot Password
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
            type="email"
            autoFocus
          />
          <Button type="submit" fullWidth variant="contained" color="primary">
            Send Recovery Email
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
