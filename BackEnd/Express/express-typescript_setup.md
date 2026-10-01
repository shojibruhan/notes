# Step: 1 Initial setup

```js
npm i express cors
npm i -D typescript tsx tsc-alias tsconfig-paths @types/node @types/express @tsconfig/node24 @types/cors
```

# Step 2: Create config file and add the followings

```bash
npx tsc --init
```

add the json

```json
{
  "compileOnSave": false,
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["ES6"],
    "allowJs": true,
    "module": "nodenext",
    "rootDir": ".",
    "outDir": "./dist",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "nodenext",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "typeRoots": ["./src/types", "./node_modules/@types"],
    "sourceMap": true,
    "types": ["node"],
    "noImplicitAny": false,

    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["src/**/*", "prisma.config.ts"],
  "exclude": ["node_modules"]
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
