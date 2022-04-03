import React from 'react';
import {LogBox} from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import {requestStoragePermission, ROUTE} from './src/Constants/';
import {Provider} from 'react-native-paper';
const Stack = createStackNavigator();
LogBox.ignoreLogs(['new NativeEventEmitter']);
const App = function () {
  React.useEffect(() => {
    requestStoragePermission();
  }, []);

  return (
    <Provider>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{headerShown: false}}>
          {ROUTE.map(route => (
            <Stack.Screen
              name={route.name}
              key={route.key}
              component={route.Component}
            />
          ))}
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  );
};

export default App;
