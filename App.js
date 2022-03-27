import React from "react";
import { Ionicons } from "@expo/vector-icons";
import { createAppContainer } from "react-navigation";
import { createBottomTabNavigator } from "react-navigation-tabs";
import { StatusBar } from 'expo-status-bar';
import 'react-native-gesture-handler'; 


import HomeScreen from "./screens/HomeScreen";
import UserScreen from "./screens/UserScreen";
import MapScreen from "./screens/MapScreen";

const TabNavigator = createBottomTabNavigator({
Home: {
	screen: HomeScreen,
	navigationOptions: {
	tabBarLabel: "Home",
	tabBarOptions: {
		activeTintColor: "#006600",
	},
	tabBarIcon: (tabInfo) => {
		return (
		<Ionicons
			name="md-home"
			size={24}
			color={tabInfo.focused ? "#006600" : "#8e8e93"}
		/>
		);
	},
	},
},
User: {
	screen: UserScreen,
	navigationOptions: {
	tabBarLabel: "User",
	tabBarOptions: {
		activeTintColor: "#006600",
	},
	tabBarIcon: (tabInfo) => {
		return (
		<Ionicons
			name="md-person-circle-outline"
			size={24}
			color={tabInfo.focused ? "#006600" : "#8e8e93"}
		/>
		);
	},
	},
},
Map: {
	screen: MapScreen,
	navigationOptions: {
	tabBarLabel: "Map",
	tabBarOptions: {
		activeTintColor: "#006600",
	},
	tabBarIcon: (tabInfo) => {
		return (
		<Ionicons
			name="md-map-sharp"
			size={24}
			color={tabInfo.focused ? "#006600" : "#8e8e93"}
		/>
		);
	},
	},
},
});

const Navigator = createAppContainer(TabNavigator);

export default function App() {
return (
	<Navigator>
    <StatusBar style="auto"/>
	  <HomeScreen/>
	</Navigator>
);
}
