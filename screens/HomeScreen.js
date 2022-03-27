import * as React from "react";
import { Text, View, Image, SafeAreaView, ScrollView, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";

const Avatar = (props) => (
	<Image
	  style={styles.avatar}
	  source={{ uri: props.url }}
	/>
  );
  
  const Heading = (props) => (
	<Text style={styles.heading}>
	  {props.children}
	</Text>
  );
  
  const Title = (props) => (
	<Text style={styles.title}>
	  {props.children}
	</Text>
  );
  
  const styles = StyleSheet.create({
	avatar: {
		height: 64, 
		width: 64, 
		borderRadius: '50%', 
	},
	heading: {
		fontSize: 20, 
		fontWeight: '600',
		paddingTop: 20, 
		paddingBottom: 12, 
		paddingHorizontal: 24, 
		color: '#08060B',
	},
	title: {
		color: '#280D5F', 
		fontSize: 12, 
		fontWeight: '600', 
		textTransform: 'uppercase', 
	},
  });
  
  // App-specific components
  
  const WoofCard = (props) => (
	<View>
	  <Avatar />
	  <Title>Todo</Title>
	</View>
  );
  
  const woofCardStyles = StyleSheet.create({
	card: {},
	title: {},
  });
  
  const WoofPost = (props) => (
	<View>
	  <Image source={{ uri: 'todo' }} />
	  <View>
		<Text>todo</Text>
		<Text>todo</Text>
	  </View>
	</View>
  );
  
  const woofPostStyles = StyleSheet.create({
	layout: {},
	image: {},
	content: {},
	title: {},
	description: {},
  });
  
  // The screen rendering everything
  const HomeScreen = () => (
	<ScrollView>
	  <Heading>Generic heading</Heading>
	  <Avatar url="https://picsum.photos/64/64" />
	  <Title>Generic title</Title>
	</ScrollView>
  );

const Home = () => {
return (
	<View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
	    <Text style={{ color: "#006600", fontSize: 40 }}>Home Screen!</Text>
	    <Ionicons name="md-home" size={80} color="#006600" />
	</View>
	);
};

export default Home;
