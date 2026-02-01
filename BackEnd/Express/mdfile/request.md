# Request

> The `req` object represents the `HTTP` request and has properties for the
>
> - request query string,
> - parameters,
> - body,
> - HTTP headers
> - and so on.

### Properites

1. **req.body**

   > Contains `key-value` pairs of data submitted in the request body. By default, it is `undefined`, and is populated when you use body-parsing middleware such as `express.json()` or `express.urlencoded()`.

2. **req.cookies**

   > When using `cookie-parser middleware`, this property is an object that contains cookies sent by the request. If the request contains no cookies, it `defaults to {}`.

   ```js
   // Cookie: name=tj
   console.dir(req.cookies.name);
   // => "tj"
   ```

3. **req.params** => dynamic id

   ```js
   // GET /user/tj
   console.dir(req.params.name);
   // => "tj"
   ```

4. **req.path**

   > Contains the path part of the request URL.

   ```js
   // example.com/users?sort=desc
   console.dir(req.path);
   // => "/users"
   ```

5. **req.query**

   > This property is an object containing a property for each query string parameter in the route. When query parser is set to disabled, it is an empty object {}, otherwise it is the result of the configured query parser.

### Methods

1. **req.accepts(types)**

   > Checks if the specified content types are acceptable, based on the request’s `Accept HTTP header field`. The method returns the best match, or if none of the specified content types is acceptable, returns false (in which case, the application should respond with `406 "Not Acceptable"`).
   >
   > The type value may be a single MIME type string (such as `“application/json”`), an extension name such as “json”, a comma-delimited list, or an array. For a list or array, the method returns the best match (if any).

   ```js
   req.accepts("application/json");
   // => "application/json"

   // Accept: text/*, application/json
   req.accepts("image/png");
   req.accepts("png");
   // => false
   ```

2. **req.get(field)**

   > Returns the specified `HTTP request header field` (case-insensitive match). The Referrer and Referer fields are interchangeable.

   ```js
   req.get("Content-Type"); // case insensitive
   // => "text/plain"

   req.get("content-type");
   // => "text/plain"

   req.get("Something");
   // => undefined
   ```

## Common method

> `http://localhost:4000/user/5?filter=name`

- req.baseUrl
- req.`originalUrl`: `/user/5`
- req.`path`: `/user/5`
- req.`hostname`: `localhost`

```js
const app = express();

const adminRoute = express.Router();

app.use("/admin", adminRoute);

adminRoute.get("/dashboard", (req, res) => {
  res.send(`This is admin page`);
});
```

> `http://localhost:4000/admin/dashboard`

- `base url`: `/admin`
- `original url`: `/admin/dashboard`
- `path`: `/dashboard`
- `hostname`: `localhost`

* req.`ip`: `::ffff:127.0.0.1`
* req.`method`: `GET/POST/PUT/PATCH/DELETE`
* req.`protocol`: `http`
* req.`params`: `{id: '5}`
* req.`query`: `{filter: 'name'}`

### req.`body`:

---

```js
// to send data through body need to use app.use(express.json())
// without using this middlewere it consoles `undifined`
// also send some data through body
app.use(express.json());
app.post("/", (req, res) => {
  console.log(req.body);
  res.send("This is post method!");
});
```

```json
{
  "name": "express practice"
}
// console.log: { name: 'express practice' }
```

### req.`cookies`

---

- step 1: To use cookies in express:

  ```bash
  npm i cookie-parser
  ```

* step 2:

  ```js
  const cookeParser = require("cookie-parser");

  app.use(cookeParser());
  ```

* step 3: create cookie from postman (for manually)

- req.`signedCookies`: if want to make cookie `cryptographycally secure`
- req.`secure`: `true` from `https`, `false` from `http`
