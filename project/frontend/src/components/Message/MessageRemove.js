import React from 'react';
import axios from 'axios';

import { IconButton } from '@material-ui/core';

import DeleteIcon from '@material-ui/icons/Delete';

import AuthContext from '../../AuthContext';
import {StepContext} from '../Channel/ChannelMessages';

function MessageRemove({
  message_id,
  disabled=false,
}) {

  const token = React.useContext(AuthContext);

  let step = React.useContext(StepContext);
  step = step ? step : () => {}; // sanity check

  const messageRemove = () => {
    axios.delete(`/message/remove`, {
      data: {
        token,
        message_id,
      }
    })
    .then(() => {
      step();
    });
  };


  return (
    <IconButton
      disabled={disabled}
      onClick={messageRemove}
      style={{ margin: 1 }}
      size="small"
      edge="end"
      aria-label="delete"
    >
      <DeleteIcon fontSize="small" />
    </IconButton>
  );
}

export default MessageRemove;
