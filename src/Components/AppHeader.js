import {useNavigation} from '@react-navigation/native';
import React from 'react';
import {Appbar, Avatar} from 'react-native-paper';

const AppHeader = function ({withBackButton}) {
  const nav = useNavigation();
  return (
    <Appbar.Header
      style={{
        backgroundColor: 'white',
        paddingHorizontal: withBackButton ? 0 : 10,
      }}>
      {withBackButton && (
        <Appbar.BackAction
          onPress={() => {
            nav.goBack();
          }}
        />
      )}
      <Avatar.Image
        size={40}
        source={require('../assets/Images/edu_logo.jpeg')}
        style={{padding: 0, margin: 0}}
      />
      <Appbar.Content
        title="Education Board Result"
        subtitle=""
        style={{
          paddingHorizontal: 3,
        }}
      />
    </Appbar.Header>
  );
};

export default AppHeader;
