import React from "react";
import { Text, View } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import ModalDemo from "../components/Modal";

const Map = () => {
return (
	<View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
		<Text style={{ color: "#006600", fontSize: 40 }}>Map Screen!</Text>
		<Ionicons name="md-map-sharp" size={80} color="#006600" />
	</View>
);
};

export default Map;
