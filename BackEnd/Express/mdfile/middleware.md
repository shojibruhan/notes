# Middleware

## purpose:

- handle common tasks
- requests logs
- filter requests
- modify/ reshape requests
- add additional details in requests body
- checking authentication i.e does the user logged in?
- permission/ authorization/ validation
- validate request body
- response bad requests
- refractoring
- sanitaization
- data transfer
- pass requests to next middleware or response handler
- etc

## Power

- it has access to both `request` & `response` object
- if it's true then it send to handler function
- it can modify request
- can send response from anywhere

## Advantage

> reduce the duplicate code

## difference between middleware & controller:

- if everything seems alright controller will call response method
- if everything seems alright middleware will call next method

```js
// handler/controller
const handleFunction = (req, res, next) => {
  // read request object
  // process request object
  // response back the result
};

// middleware
const middlewareSignature = (req, res, next) => {
  next();
};
```

## Types of middleware: global & local

```js
// global - direct application by use method
app.use(cors());

// local
app.get("/", cors(), (req, res) => {
  res.send("local middleware");
});
```

### Signature of Global Middleware

```js
const middleware = (req, res, next) => {
  console.log(`${req.method} - ${req.url}`);
  console.log("I am a middleware!");
  next();
};

// using globally
app.use(globalMiddleware);
```

### Signature of Local Middleware

```js
// using locally
app.get("/local", middleware, (req, res) => {
  res.send(`<h1>Local Middleware!</h1>`);
});
```

### Types of Middleware

- application level middleware: `app.use()`
- router level middleware: `router.use()`
- error handling middleware
- build in middleware: `express.json()`/ `express.static()`
- third-party middleware: `cookie-parser`
