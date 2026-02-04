# Mongoose

# Steps

1. install mongoose
2. create Schema(scheme like a shape/ list of properties) in a js file
3. Schema is a class object where you have to give a key and value is data type
4. create a model by mongoose.model(model-Name, schema)
5. export the model

# install

```bash
npm i mongoose
```

# create a Schema + model

- step 1: Create a schema
- step 2: Create a model using schema

```js
const schemaName = new mongoose.Schema({
  fieldName: DataType,
});

const ModelName = mongoose.model("ModelName", schemaName);

module.exports = ModelName;
```

# example

```js
const { Schema, model } = require("mongoose");
const { schema } = require("./user");

const profileSchema = new Schema({
  firstName: String,
  lastName: String,
  phone: String,
  avatar: String,
  user: {
    type: Schema.Types.ObjectId,
    ref: "User", // why don't use hardcore? :: in runtime search User, if not found throw error
  },
});

const Profile = model("Profile", profileSchema);

module.exports = Profile;
```

---

# Connection through mongodb Compass

```js
const mongoose = require("mongoose");

mongoose
  .connect("mongodb://localhost:27017/<dbname>")
  .then(() => {
    console.log("✅ Connected through compass!");
  })
  .catch((err) => {
    console.log("❌ Can't Connect", err);
  });
```

> async await

```bash
# for using .env file accessable::  process.env.MONGODB_URI
npm i dotenv
```

```js
require("dotenv").config();

const dbConnect = async () => {
  try {
    const connect = await mongoose.connect(process.env.MONGODB_URI);
    console.log("✅ Connected with database");
  } catch (err) {
    console.error(err);
    console.log("❌ Can't Connect");
  }
};

dbConnect();
```
