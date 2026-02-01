# Response

> The `res` object represents the `HTTP response` that an `Express app` sends when it gets an HTTP request.

## Properties => (not important)

1. res.app
2. res.headersSent
3. res.locals

## Methods

1.  **res.append(field [, value])**

    > Appends the specified `value` to the `HTTP response header field`. If the header is not already set, it creates the header with the specified value. The `value` parameter can be a string or an array.

    ````js
    res.append("Link", ["<http://localhost/>", "<http://localhost:3000/>"]);

    res.append("Set-Cookie", "foo=bar; Path=/; HttpOnly");

    res.append("Warning", "199 Miscellaneous warning");
    ```.

    ````

2.  **res.cookie(name, value [, options])**.

    ```js
    res.cookie("name", "tobi", {
      domain: ".example.com",
      path: "/admin",
      secure: true,
    });

    res.cookie("rememberme", "1", {
      expires: new Date(Date.now() + 900000),
      httpOnly: true,
    });
    ```

    > You can set multiple cookies in a single response by calling res.cookie multiple times, for example:

    ```js
    res
      .status(201)
      .cookie("access_token", `Bearer ${token}`, {
        expires: new Date(Date.now() + 8 * 3600000), // cookie will be removed after 8 hours
      })
      .cookie("test", "test")
      .redirect(301, "/admin");
    ```

3.  **res.end([data[, encoding]][, callback])**
    > Ends the response process
    ```js
    res.end();
    res.status(404).end();
    ```
4.  **res.format(object)**

    > say if request comes from website you want to send json data but if it comes through mobile device you will send html data

    ```js
    res.format({
      "text/plain"() {
        res.send("hey");
      },

      "text/html"() {
        res.send("<p>hey</p>");
      },

      "application/json"() {
        res.send({ message: "hey" });
      },

      default() {
        // log the request and respond with 406
        res.status(406).send("Not Acceptable");
      },
    });
    ```

    > In addition to canonicalized MIME types, you may also use extension names mapped to these types for a slightly less verbose implementation:

    ```js
    res.format({
      text() {
        res.send("hey");
      },

      html() {
        res.send("<p>hey</p>");
      },

      json() {
        res.send({ message: "hey" });
      },
    });
    ```

5.  **res.get(field)**

    > Returns the HTTP response header specified by field. The match is case-insensitive.

    ```js
    res.get("Content-Type");
    // => "text/plain"
    ```

6.  **res.json([body])**
    > Sends a `JSON response`. This method sends a response (with the correct `content-type`) that is the parameter converted to a JSON string using `JSON.stringify()`.
    >
    > The parameter can be any JSON type, including object, array, string, Boolean, number, or null, and you can also use it to convert other values to JSON.
    ```js
    res.json(null);
    res.json({ user: "tobi" });
    res.status(500).json({ error: "message" });
    ```
7.  **res.redirect([status,] path)**

    ```js
    res.redirect("/foo/bar");
    res.redirect("http://example.com");
    res.redirect(301, "http://example.com");
    res.redirect("../login");
    ```

8.  **res.send([body])**

    > Sends the HTTP response.
    >
    > The body parameter can be a Buffer object, a String, an object, Boolean, or an Array. For example:

    ```js
    res.send(Buffer.from("whoop"));
    res.send({ some: "json" });
    res.send("<p>some html</p>");
    res.status(404).send("Sorry, we cannot find that!");
    res.status(500).send({ error: "something blew up" });
    ```

    > difference between `res.end()` & `res.send()` is, first one ending connection between client & server without data, second one with data.

9.  **res.set(field [, value])**

    > Sets the response’s HTTP header field to value. To set multiple fields at once, pass an object as the parameter.

    ```js
    res.set("Content-Type", "text/plain");

    res.set({
      "Content-Type": "text/plain",
      "Content-Length": "123",
      ETag: "12345",
    });
    ```

10. **res.status(code)**

    > Sets the HTTP status for the response. It is a chainable alias of Node’s response.statusCode.

    ```js
    res.status(403).end();
    res.status(400).send("Bad Request");
    res.status(404).sendFile("/absolute/path/to/404.png");
    ```

11. **res.type(type)**

    > Sets the `Content-Type HTTP header` to the MIME type as determined by the specified type. If type contains the “/” character, then it sets the Content-Type to the exact value of type, otherwise it is assumed to be a file extension and the MIME type is looked up using the contentType() method of the mime-types package.

    ```js
    res.type(".html"); // => 'text/html'
    res.type("html"); // => 'text/html'
    res.type("json"); // => 'application/json'
    res.type("application/json"); // => 'application/json'
    res.type("png"); // => image/png:
    ```
