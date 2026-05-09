# Auth Strategy

HTTP is stateless i.e it doesn't remember who send the request. Every request looks like a stranger. So you have to send your identity every time when you request to the browser. So application use `token` to remember the user. Application can use 2
ways to remember the session.

There are 2 ways for authorization

- Session Token
- JWT Token

## Session-based Authentication

When user authenticate, server creates a `session` and trac the user using `session log`. This create a `Session Id` for that user and give it to the user. Now when the user create another request, he send the
`Session Id` with request. Server search in `session log` with that id to confirm the user.

Usually user save the `Session Id` in the `browser cookie`. When he hit the request, browser autometicaly add it to the request header.

**Real-life analogy: Hotel reception 🏨**

1. You show passport (login)

2. Reception creates a record in their computer

3. They give you a room key card

4. Every time you come back, you show the key

5. Reception checks their computer

Now there is a problem, because modern world there are multiple server running which are maintain by load balancer. Solution is use `Redis Cache` to save the `Session Id`. But if the `redis` is down for some reason then authentication always fail.

**Cons ❌**

- Needs server memory / DB
- Harder to scale
- Not great for mobile / APIs

That's where `JSON Web Token` come into play.

## Token-based authentication (JWT)

When user authenticate, instead of creating `Session Id or log` server creates a `JSON with a signature` using the user info. Send it to the user. So server doesn't save anything. When user send request he send the `JSON token` with the request.

Normaly User save the `JWT` in either `cookies` or `local Storage`.

**Real-life analogy: Airport boarding pass ✈️**

1. You show passport once (login)
2. Airport gives you a signed boarding pass
3. You carry it yourself
4. Every checkpoint checks the signature
5. No need to call central database. It's `a signed identity card`

`JWT` has 3 parts.

- Header (algorithm for convertion & Token Type)
- Payload (it's the user info encoded with base64)
- signature (Hashed String - server can validate this!)

> ## **Sample JWT:**
>
> `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`.eyJ1c2VybmFtZSI6InNob2ppYjcxIiwidXNlcklkIjoiNjk4MzdhYzBiMmVjMWRkNzU4ZDAxYTljIiwiaWF0IjoxNzcwMjI4NjY3LCJleHAiOjE3NzAyMzIyNjd9.`VyRXV1L7OSD3Oqyucp8JxKjiU4Zgeo3Msmki9bPYGxk`
>
> check: [jwt.io](https://www.jwt.io/) use secret key from .env file for varification.

_Note: Encoding is not for security purpose. It's just for simplification. Cause not all application use json. So don't put secret key or sensitive info here. Just the public info._

| Thing               | Session            | JWT           |
| ------------------- | ------------------ | ------------- |
| State               | Server-side        | Client-side   |
| Storage             | Server memory / DB | Browser / app |
| Scales easily       | ❌                 | ✅            |
| Revocation          | Easy               | Hard          |
| Mobile/API friendly | ❌                 | ✅            |
