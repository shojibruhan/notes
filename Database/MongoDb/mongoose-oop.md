# Class, instance & instance method

Schema: structure of the data that we put in database

```js
const { Schema, model } = require("mongoose");
const schemaName = new mongoose.Schema({
  fieldName: DataType,
});

const ModelName = mongoose.model("ModelName", schemaName);

const todo = new Todo(req.body);
todo.save();
```
