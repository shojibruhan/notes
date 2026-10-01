1. install Prisma CLI globally using npm:

```bash
npm i -D prisma@7.10.0 @types/pg

npm i @prisma/client@7.10.0 @prisma/adapter-pg

```

2.

```bash
npx prisma init --datasource-provider postgresql
```

3. Add script to package.json: (Optional)

```json
"scripts": {
    "migrate:dev": "prisma migrate dev",
    "migrate:prod": "prisma migrate deploy"
}
```

```bash
npm run migrate:dev
```

4. generate Prisma client: (put it .gitignore)

```bash
npx prisma generate
```

5. create prisma client: from documentation

```typescript
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../generated/prisma/client";

const connectionString = `${process.env.DATABASE_URL}`;
const adapter = new PrismaPg({ connectionString });

const prisma = new PrismaClient({ adapter });

export default prisma;
```
