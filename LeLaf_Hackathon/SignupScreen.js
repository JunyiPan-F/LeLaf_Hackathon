// SignupScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Text,ImageBackground } from 'react-native';
import axios from 'axios';

const SERVER_URL = 'http://172.20.10.2:3000'; // Replace with your Flask server URL

const SignupScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSignup = async () => {
      console.log(username);
      console.log(password);
      axios.post('http://172.20.10.2:3000/signup', {
        username:username, password:password
      },{ headers: { 'Content-Type': 'application/json' } })
      .then(function (response) {
          <View>
            <Text>"Successfully made an account!"</Text>
          </View>
          console.log(response);
      })
      .catch(function (error) {
          console.log(error.response.data);
      });
  };

  return (
    <ImageBackground 
    source={require('./bg.png')}
    style={styles.container}>
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="username"
        value={username}
        onChangeText={(text) => setUsername(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={(text) => setPassword(text)}
      />
      <Button title="Sign Up" onPress={handleSignup} color='#300040'/>
      <Button title="Go to Login" onPress={() => navigation.navigate('Login')}color='#300040' />
    </View>
    </ImageBackground>

  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
    width: 200,
  },
});

export default SignupScreen;