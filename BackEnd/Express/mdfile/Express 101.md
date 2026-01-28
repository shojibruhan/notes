# Express 101

## setup

```bash
npm init -y
npm i -D nodemon
npm i express
```

> add a script file in package.json

```js
"scripts": {
    "dev": "nodemon index.js"
  },
```

_*Note:*_ to run programe use `npm run dev` but for `start` or `test` just `run start` or `run test`

> **🛎️ Important method:**
>
> ## 🧨 express method()
>
> - express.json()
> - express.Router()
> - express.static()
> - express.urlencoded()

## app.method()

The `app` object conventionally denotes the Express application. Create it by calling the top-level express() function exported by the Express module:

_**The app object has methods for:**_

- Routing HTTP requests
- Configuring middleware
- Rendering HTML views
- Registering a template engine
