<font size=4 face='楷体'>

## Prisma 使用

### Prisma 连接 Mongo

#### 1. 安装 Prisma CLI 

首先，你需要安装 Prisma CLI。在项目根目录下运行以下命令：


```bash
npm install prisma --save-dev
npm install @prisma/client
```
 
- `prisma`：Prisma CLI 工具。
 
- `@prisma/client`：Prisma Client，供代码中调用数据库。

#### 2. 初始化 Prisma 

在项目根目录下初始化 Prisma：


```bash
npx prisma init
```
这将在项目中创建一个 `prisma` 文件夹，并生成一个 `schema.prisma` 文件。

#### 3. 配置 MongoDB 数据源 
打开 `prisma/schema.prisma` 文件，更新数据源配置以连接 MongoDB：

```prisma
// schema.prisma

datasource db {
  provider = "mongodb"
  url      = env("DATABASE_URL") // 使用环境变量指定 MongoDB 连接字符串
}
```
在 `.env` 文件中添加 MongoDB 的连接字符串：

```env
// .env
DATABASE_URL="mongodb+srv://your-mongo-db-connection-string"
```

确保你的 MongoDB 连接字符串格式正确，并且可以通过 Prisma 连接到数据库。

#### 4. 生成 Prisma Client 

生成 Prisma Client，这样你就可以在代码中使用 Prisma 来操作 MongoDB 数据库：


```bash
npx prisma generate
```
这会根据 `schema.prisma` 文件中的配置生成 Prisma Client。
#### 5. 使用 Prisma Client 进行数据库操作 

在 TypeScript 文件中导入并使用 Prisma Client：


```typescript
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  // 获取所有用户
  const users = await prisma.user.findMany();
  console.log(users);
}

main()
  .catch(e => {
    console.error(e);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

##### 数据操作示例 
 
- **插入数据** ：


```typescript
const newUser = await prisma.user.create({
  data: {
    name: 'Alice',
    email: 'alice@prisma.io',
  },
});
console.log(newUser);
```
 
- **查询数据** ：


```typescript
const user = await prisma.user.findUnique({
  where: { id: 1 },
});
console.log(user);
```
 
- **更新数据** ：


```typescript
const updatedUser = await prisma.user.update({
  where: { id: 1 },
  data: { name: 'Alice Updated' },
});
console.log(updatedUser);
```
 
- **删除数据** ：


```typescript
const deletedUser = await prisma.user.delete({
  where: { id: 1 },
});
console.log(deletedUser);
```

#### 总结 

通过以上步骤，你已经成功地将 Prisma 与 MongoDB 集成，并可以使用 Prisma Client 进行数据库操作。你可以在代码中通过 Prisma Client 执行数据库查询、插入、更新和删除等操作。

### Reference

[官方文档](https://www.prisma.io/docs/getting-started/setup-prisma/add-to-existing-project/mongodb/connect-your-database-typescript-mongodb)

**2024.12.19**
