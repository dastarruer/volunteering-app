import { View, StyleSheet, ScrollView } from "react-native";
import BottomNav from "../components/BottomNav";

export default function Index() {
  return (
    <View style={styles.container}>

      <ScrollView style={styles.content}>
      </ScrollView>

      <BottomNav />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#dad7cd",
  },
  content: {
    flex: 1, // This takes up all available space
    justifyContent: "center",
    alignItems: "center",
  },
});
