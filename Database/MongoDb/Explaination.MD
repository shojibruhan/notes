<details>

<summary>What is enum in mongoose?</summary>

> Restricting a field so it can have only specific predefined values

```text
Think of enum like a menu 🍽️
Menu: user | admin | moderator
You can only order what’s on the menu.
```

```js
  role: {
    type: String,
    enum: ["user", "admin", "moderator"],
    default: "user",
  }
```

- Valid

```js
await User.create({
  name: "Ruhan",
  role: "admin",
});
```

- Invalid

```js
await User.create({
  name: "Ruhan",
  role: "superman",
});
```

```swift
`superman` is not a valid enum value for path `role`
```

</details>

<details><summary>Why MongoDb</summery>

> Why MongoDB? Why not PostgreSQL?

1. Most of out data in the world has no shape. You can't put it in a table. If you try, either you will make duplicate data or data can go missing.

2. We can collect & store as much data as we want in same collection within same database without fear of missing a single data or duplicating data.
3. Data belongs to the same to origin: Data is stored together with the entity that owns it, instead of being spread across many tables.

🎯 When MongoDB is better than SQL

✅ Read-heavy applications.  
✅ Rapid development  
✅ Flexible schema  
✅ JSON-based APIs  
✅ Horizontal scaling

🎯 When SQL is better

✅ Financial systems  
✅ Complex transactions  
✅ Strong relational integrity  
✅ Heavy reporting & analytics

</details>
