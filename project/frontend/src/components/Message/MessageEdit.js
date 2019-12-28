import React from 'react';
import axios from 'axios';

import {
    IconButton,
} from '@material-ui/core';

import EditIcon from '@material-ui/icons/Edit';

import AuthContext from '../../AuthContext';
import {StepContext} from '../Channel/ChannelMessages';

function MessageEdit({
    message_id,
    disabled=false,
}) {

    const token = React.useContext(AuthContext);

    let step = React.useContext(StepContext);
    step = step ? step : () => {}; // sanity check

    const messageEdit = () => {
        const message = prompt();
        if (message === null) return; // basic validation

        /**
         * Empty message should delete original
         */
        if (message === "") {
            axios.delete(`/message/remove`, {
                data: {
                    token,
                    message_id,
                }
            })
            .then(() => {
                step();
            });
            return;
        }

        /**
         * Default message edit behaviour
         */
        axios.put(`/message/edit`, {
            token,
            message_id,
            message,
        })
        .then(() => {
            step();
        });
    };

    return (
        <IconButton
            disabled={disabled}
            onClick={messageEdit}
            style={{ margin: 1 }}
            size="small"
            edge="end"
            aria-label="delete"
        >
            <EditIcon fontSize="small" />
        </IconButton>
    );
}

export default MessageEdit;
