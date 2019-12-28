import React from 'react';
import ProfileList from './ProfileList';
import ChannelList from './ChannelList';

function ProfileChannelLists({ channel_id }) {
  return (
    <>
      <ProfileList />
      <ChannelList channel_id={channel_id} />
    </>
  );
}

export default ProfileChannelLists;
