# Step: 1 Initial setup

```js
npm i express cors
npm i -D typescript tsx tsc-alias tsconfig-paths @types/express @tsconfig/node24 @types/cors
```

# Step 2: Create config file and add the followings

```bash
npx tsc --init
```

add the json

```json
{
  "extends": "@tsconfig/node24/tsconfig.json",
  "compilerOptions": {
    "rootDir": "src",
    "outDir": "dist",
    "module": "nodenext",
    "target": "esnext",
    "types": [],
    "strict": true,

    "paths": {
      "@src/*": ["./src/*"]
    },

    "include": ["src/**/*.ts"],
    "exclude": ["node_modules"]
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
