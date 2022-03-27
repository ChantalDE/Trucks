import React, {useState} from "react";
import { Text, View, ScrollView, TextInput } from "react-native";
import { Ionicons } from "@expo/vector-icons";

const User = () => {

	const [username, setUsername] = useState(''); 
	const [password, setPassword] = useState(''); 
	const [confirmationPassword, setConfirmationPassword] = useState(''); 

function confirmPasswordsMatch(props) {
	const { nativeEvent: {text} } = props; 

	if (text !== password)
	{
		alert('Passwords do not match, please try again.')
	}
}

return (
	<View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
	    <Text style={{ color: "#006600", fontSize: 40 }}>User Screen!</Text>
	    <Ionicons name="md-person-circle-outline" size={80} color="#006600" />
		<InputWithLabel
			label = "Username"
			placeholder = "Enter Username here"
			value = {username}
			onChangeText = {setUsername}
		/>
		<InputWithLabel
			label = "Password"
			placeholder = "Enter Password Here"
			value = {password}
			onChangeText = {setPassword}
			secureTextEntry
		/>
		<InputWithLabel
			label = "Confirm Password"
			placeholder = "Please confirm your Password"
			value = {confirmationPassword}
			onChangeText = {setConfirmationPassword}
			secureTextEntry
			onSubmitEditing = {confirmPasswordsMatch}
		/>
	</View>
);
};

function InputWithLabel(props) {
	const { label, placeholder, value, onChangeText, secureTextEntry, onSubmitEditing } = props; 
	return (
		<View style = {{ padding: 16}}>
			<Text style = {{ padding: 8, fontSize: 18 }}>{label}</Text>
			<TextInput
				placeholder = {placeholder}
				value = {value}
				onChangeText = {onChangeText}
				secureTextEntry={secureTextEntry}
				onSubmitEditing={onSubmitEditing}
				style = {{ padding: 8, fontSize: 18 }}
			/>
		</View>
	);
}

export default User;
