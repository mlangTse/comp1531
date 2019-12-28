import React from 'react';
import axios from 'axios';

import {
  Badge,
  IconButton,
} from '@material-ui/core';

import ThumbUpIcon from '@material-ui/icons/ThumbUp';
import ThumbUpOutlinedIcon from '@material-ui/icons/ThumbUpOutlined';

import AuthContext from '../../AuthContext';
import {StepContext} from '../Channel/ChannelMessages';

function MessageReact({
  message_id,
  reacts = [] /* [{ react_id, u_ids }] */,
}) {

  const token = React.useContext(AuthContext);
  let step = React.useContext(StepContext);
  step = step ? step : () => {}; // sanity check

  const messageReact = (is_reacted) => {
    if (is_reacted) {
      axios.post(`/message/unreact`, {
        token,
        message_id,
        react_id: 1 /* FIXME */,
      })
      .then(() => {
        step();
      });
    } else {
      axios.post(`/message/react`, {
        token,
        message_id,
        react_id: 1 /* FIXME */,
      })
      .then(() => {
        step();
      });
    }
  };

  let thumbUpCount = 0;
  let is_reacted = false;
  const thumbUpIndex = reacts.findIndex((react) => react.react_id === 1);
  if (thumbUpIndex !== -1) {
    thumbUpCount = reacts[thumbUpIndex].u_ids.length;
    is_reacted = reacts[thumbUpIndex].is_this_user_reacted;
  }

  return (
    <Badge
      anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      badgeContent={thumbUpCount}
      color="secondary"
    >
      <IconButton
        onClick={() => messageReact(is_reacted)}
        style={{ margin: 1 }}
        size="small"
        edge="end"
        aria-label="delete"
      >
        {is_reacted ? (
          <ThumbUpIcon fontSize="small" />
          ) : (
          <ThumbUpOutlinedIcon fontSize="small" />
        )}
      </IconButton>
    </Badge>
  );
}

export default MessageReact;
