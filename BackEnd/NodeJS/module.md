## Module system

> An `Immediately Invoked Function Expression (IIFE)`, pronounced `"iffy,"` is a JavaScript function that runs as soon as it is defined. It is a design pattern used to create a private scope for variables, thus preventing them from polluting the global namespace.

```js
(function() {
    const var = 'something'
})();
```

> What we write something in a file/module it goes to iffy.

```js
(function (exports = {}, require, module, __filename, __dirname) {
  const fs = require("fs");

  const a = ["a", "b", "c"];

  module.exports = a; // it returns modlue.exports

  //   retunr module.exports
})();
```

- `exports` have a default value= {}
- when write `require` => we actually require the whole function
- when we write `require` it actually calls the function => returns modlue.exports

# Core Module

[Complete Guide: W3 School](https://www.w3schools.com/nodejs/ref_modules.asp)

- path module
- os
- fs
- events
- `🕸️ http:` module which communicate with network `🕸️`

> _*NOTE:*_ Every `async` operation in nodeJs takes a `callback` with two parameter: `error` & `data`

```js
// sync operation
const data = fs.readFileSync("yourFileName.txt");
console.log(data.toString());

// async operation
fs.readFile("yourFileName.txt", (err, chunk) => {
  console.log(chunk.toString());
});
```

## 🧨 Events

> Symple Analogy
>
> - **Event** = bell
> - **on()** = “When bell rings, do this”
> - **emit()** = “Ring the bell”
>
> ---
>
> - **Event** → the doorbell ringing
> - .**on()** → “When the doorbell rings, do this”
> - .**emit()** → someone presses the doorbell
>
>   Nothing happens until the doorbell is pressed.

```js
const EventEmitter = require("events");
const myEmitter = new EventEmitter();

// Register an event listener
myEmitter.on("event", () => {
  console.log("An event occurred!");
});

// Emit the event
myEmitter.emit("event");
```

1.  **on:** Listening 👂
    > `registering` a reaction. You are not doing anything yet.
    > You are just promising what to do later.
    >
    > - “Hey system, when something called `'event' happens, run this function.”
    > - “When the doorbell rings, open the door.”
1.  **emit:** TRIGGERING 🛎️
    > `Raising` an event. This line `causes action`.  
    > You are doing it
    >
    > Pressing the doorbell button.  
    > 👉 When this line runs:
    >
    > - “Do I have listeners for 'event'?”
    > - "Yes"
    > - “Run all of them — in order”

- .emit() → sending a message
- .on() → receiving the message

### Stream evnets

Some events are predifined. Streams in Node emit specific, predefined events.

```js
// code won't work if named something else except "data"
req.on("data", (chunk) => {
  console.log("chunk:", chunk);
});
```

```js
const fs = require("fs");

const file = fs.createReadStream(`${__dirname}/index.html`);

file.on("data", (value) => {
  console.log(value.toString());
});
```

works only because `"data"` is a real event name that Node `emits`. If changes to something else that event never fires. Node doesn’t know about it.

some example like 'data':

- "error"
- "end"
- "close"
- "pipe"
- "pause"
- "resume"

_*Note:*_ `request` is a readable stream & `response` is writable stream

> _*[Here `data` is called readable stream. Full list of stream from NodeJs Doc.](https://nodejs.org/api/stream.html#:~:text=Writable%20streams-,Class:%20stream.Writable,%5B%2C%20encoding%5D%5B%2C%20callback%5D)*_
