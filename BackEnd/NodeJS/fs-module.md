# Read & Write: fs/ response

`Read` and `write` just mean moving data.

> `Read` = take data from somewhere into your program

> `Write` = send data from your program to somewhere else

The key is: where is “somewhere”?
That depends on the API.

---

## 1️⃣ fs.readFile() / fs.writeFile() (File System)

What is it talking to?

👉 The server’s hard disk

Who uses it?

👉 Your backend (Node.js server)

Example

```js
fs.readFile("data.txt", "utf8", (err, data) => {
  console.log(data);
});
```

Node asks the operating system

OS reads bytes from the file on disk

Data comes into your Node app

✅ Client is NOT involved  
✅ Database is NOT involved (unless the file is a database file)

Think of it like:

> “Hey computer, open this file and give me its contents.”

---

## 2️⃣. fs.readFileSync() vs async (small note)

> `readFileSync()` → waits until done (blocking)

> `readFile()` → doesn’t wait, continues execution (non-blocking)

Both still:
👉 read from disk
👉 used by server

---

## 3️⃣ res.write() / res.end() (HTTP Response)

What is it talking to?

👉 The network (HTTP connection)

Who uses it?

👉 The server, to talk to the client (browser, mobile app, Postman, etc.)

Example

```js
res.write("Hello");
res.write(" World");
res.end();
```

Server is sending data

Data goes over the internet

Client receives it

Think:

“Send this text back to the browser.”

📌 res.write() does not write to disk  
📌 It writes to the response stream

---

## 4️⃣ req.read() / request data

When a client sends data (POST body, form, JSON):

```js
app.post("/login", (req, res) => {
  console.log(req.body);
});
```

What happened?

Client wrote data to the request

Server read data from the request

So:

Client writes

Server reads

---

## 5️⃣ Streams (why everything is “read” / “write”)

Node treats many things as streams:

| Thing         | You read from | You write to |
| ------------- | ------------- | ------------ |
| File          | File          | File         |
| HTTP request  | Client        | —            |
| HTTP response | —             | Client       |
| Socket        | Network       | Network      |

So:

> `read` = data coming into Node

> `write` = data going out of Node

---

## 6️⃣ Who uses what? (super clear table)

| API              | Read / Write | Who is doing it | Talking to |
| ---------------- | ------------ | --------------- | ---------- |
| `fs.readFile()`  | read         | Server          | Disk       |
| `fs.writeFile()` | write        | Server          | Disk       |
| `req`            | read         | Server          | Client     |
| `res.write()`    | write        | Server          | Client     |
| `Database query` | read/write   | Server          | Database   |

---

One sentence mental model

> Node.js is in the middle.  
>  It reads data from files, clients, or databases  
>  and writes data to files, clients, or databases.
