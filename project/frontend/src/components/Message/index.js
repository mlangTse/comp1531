import React from 'react';
import timeago from 'epoch-timeago';
import axios from 'axios';

import {
  Avatar,
  ListItem,
  ListItemIcon,
  ListItemText,
} from '@material-ui/core';

import AuthContext from '../../AuthContext';
import MessagePin from './MessagePin';
import MessageReact from './MessageReact';
import MessageRemove from './MessageRemove';
import MessageEdit from './MessageEdit';

import {isMatchingId} from '../../utils';
import {extractUId} from '../../utils/token';

function Message({
  message_id,
  message = '',
  u_id,
  time_created,
  is_unread = false,
  is_pinned = false,
  reacts = [] /* [{ react_id, u_ids }] */,
}) {

  const [name, setName] = React.useState("");
  const [imgUrl, setImgUrl] = React.useState();
  const token = React.useContext(AuthContext);
  const isUser = isMatchingId(u_id, extractUId(token));

  const msgToList = msg => msg.split("\n");

  React.useEffect(() => {
    setName();
    setImgUrl()
    axios
      .get(`/user/profile`, {
        params: {
          token,
          u_id,
        },
      })
      .then(({ data }) => {
        const {
          email = '',
          name_first = '',
          name_last = '',
          handle_str = '',
          profile_img_url = '',
        } = data;
        setName(`${name_first} ${name_last}`);
        setImgUrl(`${profile_img_url}`)
      })
      .catch((err) => {
        console.error(err);
      });
  }, [message_id, token, u_id]);

  return (
    <ListItem key={message_id} style={{ width: '100%' }}>
      {message && (
        <>
          <ListItemIcon>
            <img className="avatar-small" src={imgUrl} />
          </ListItemIcon>
          <div
            style={{
              display: 'flex',
              width: '100%',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <ListItemText
              primary={
                <>
                  <span>{name}</span>
                  <span style={{ paddingLeft: 10, fontSize: 10 }}>
                    {timeago(time_created * 1000)}
                  </span>
                </>
              }
              secondary={
                <div>
                  {msgToList(message).map((msg, i) => (
                    <p>{msg}</p>
                  ))}
                </div>
              }
            />
            <div style={{ display: 'flex', height: 30, marginLeft: 20 }}>
              <MessageReact
                message_id={message_id}
                reacts={reacts}
                u_id={u_id}
              />
              <MessagePin
                message_id={message_id}
                is_pinned={is_pinned}
              />
              <MessageEdit
                message_id={message_id}
                // disabled={!isUser} /* We have no way of checking admin status */
              />
              <MessageRemove
                message_id={message_id}
                // disabled={!isUser} /* We have no way of checking admin status */
              />
            </div>
          </div>
        </>
      )}
    </ListItem>
  );
}

export default Message;
