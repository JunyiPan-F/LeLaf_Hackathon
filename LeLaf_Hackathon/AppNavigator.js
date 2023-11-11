// AppNavigator.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './HomeScreen'; // Replace with the actual name of your home screen component
import LoginScreen from './LoginScreen'; // Replace with the actual name of your other screen component
import SignupScreen from './SignupScreen'; // Replace with the actual name of your other screen component
import AvatarScreen from './AvatarScreen'; // Replace with the actual name of your other screen component
import CommunityScreen from './CommunityScreen'; // Replace with the actual name of your other screen component
import PostScreen from './PostScreen'; // Replace with the actual name of your other screen component




const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Signup" component={SignupScreen} />
        <Stack.Screen name="Avatar" component={AvatarScreen} />
        <Stack.Screen name="Community" component={CommunityScreen} />
        <Stack.Screen name="Post" component={PostScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;
