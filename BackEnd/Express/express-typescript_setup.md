# Step: 1 Initial setup
```js
npm i express cors 
npm i -D typescript tsx @types/express @tsconfig/node24 @types/cors
```

# Step 2: Create config file and add the followings

```bash
touch tsconfig.json
```
add the json

```json
{
  "extends": "@tsconfig/node24/tsconfig.json",
  "compilerOptions": {
    "rootDir": "src",
    "outDir": "dist"
  }
}
```
# Step 3: Script file

```json
"scripts": {
    "build": "npx tsc",
    "start": "npx tsc && node dist/index.js",
    "dev": "tsx watch src/index.ts"
  }
```

