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
