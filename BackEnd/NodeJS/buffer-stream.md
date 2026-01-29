# Buffer & Stream

- `Buffer` = a temporary box to hold data. A Buffer is a chunk of memory where Node temporarily stores raw data (bytes).  
  Not text or JSON. Just Raw bytes.

**Why Buffer exists at all**

Computers understand bytes, not strings. So when Node receives:

- file data
- network data
- image
- video

It first goes into a Buffer.

- `Stream` = a pipe that moves data little by little. A Stream is a way to process data piece by piece, instead of all at once. Streams always use `buffers` internally.
  > `Stream` = many small `buffers` flowing

**Why streams matter**  
Imagine a 5GB video file.

```js
fs.readFile("video.mp4", ...)
```

Node:

- loads entire file into memory
- RAM explodes 💥
- server slows or crashes

✅ With streams

```js
fs.createReadStream("video.mp4");
```

Node:

- reads 64KB
- sends it
- reads next 64KB
- repeats

Memory stays calm 😌

**How streams actually work internally
Under the hood**

1. Data arrives from disk/network
2. Node puts it in a buffer
3. Emits a data event
4. Consumer handles it
5. Repeat

So streams are basically:

> EventEmitter + Buffer + flow control
> | Type | Meaning | Example |
> | --------- | ---------------- | ------------- |
> | Readable | You read from it | file, request |
> | Writable | You write to it | response |
> | Duplex | Both | socket |
> | Transform | Modify data | gzip, crypto |

**The MOST important real example (HTTP)**

- Incoming request => `req` <= Readable Stream
- Outgoing response => `res`<= Writable Stream
- `Pipe` 🚿 — connecting streams

** When SHOULD you use Buffer explicitly ✅**

- Working with binary data
- Encoding/decoding
- Cryptography
- Low-level network work

**Avoid when:**

- You just want to read files
- You’re sending responses
- Data is large

Streams already manage buffers safely.

**When SHOULD you use Streams ✅**

- Large files
- File uploads/downloads
- Video/audio
- Real-time data
- Proxying data

**Final mental image 🧠**

> `Buffer` = bucket  
> `Stream` = flowing river of buckets  
> `Pipe` = connect rivers
