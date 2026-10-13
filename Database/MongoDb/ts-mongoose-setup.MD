```ts
import mongoose from "mongoose";
import { DATABASE_URL } from ".";

export const connectDB = async (): Promise<void> => {
  try {
    await mongoose.connect(DATABASE_URL);
    console.log("✅ Connected with database");

    process.on("SIGINT", async () => {
      await mongoose.connection.close();
      process.exit(0);
    });
  } catch (error) {
    console.log("❌ Can't Connect. Error: ", error);
    throw new Error(`Failed to connect to databse: ${error}`);
  }
};

export const disConnectDb = async (): Promise<void> => {
  try {
    await mongoose.connection.close();
  } catch (error) {
    throw new Error(`Failed to disconnect database: ${error}`);
  }
};

connectDB();
```
