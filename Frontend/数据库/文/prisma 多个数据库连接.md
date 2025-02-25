# Prisma Issue #2443: "Multiple Connections / Databases / Datasources" 

## 问题概述 
在 [Prisma Issue #2443](https://github.com/prisma/prisma/issues/2443)  中，讨论了如何在 Prisma 中使用多个数据库连接（datasources），并且如何配置多个数据库源。
## 背景 

Prisma 允许用户在同一个项目中配置多个数据库连接。这对于需要连接到多个数据库的项目非常有用，尤其是在微服务架构或者需要同时支持多个数据库时。此功能在不同的数据源（例如 PostgreSQL 和 MySQL）之间切换变得更加灵活。

## 问题与挑战 
Prisma 的官方文档支持配置多个数据源（`datasources`），但是在实际使用中，用户会面临以下挑战： 
1. **如何在 schema 文件中正确配置多个数据源** 。
 
2. **如何在应用中正确使用多个数据库连接** 。
 
3. **如何使用 Prisma Client 在多个数据库之间切换** 。

## 解决方案 

### 1. 配置多个数据源 
Prisma schema 文件支持配置多个 `datasource`，例如可以同时配置 PostgreSQL 和 MySQL 数据源。每个数据源都有一个不同的连接字符串，并且可以为每个数据源指定不同的数据库。
#### 示例：配置多个数据源 


```prisma
// schema.prisma

// PostgreSQL 数据源
datasource db1 {
  provider = "postgresql"
  url      = env("DATABASE_URL1")
}

// MySQL 数据源
datasource db2 {
  provider = "mysql"
  url      = env("DATABASE_URL2")
}
```
在这个示例中，`db1` 连接到 PostgreSQL 数据库，`db2` 连接到 MySQL 数据库。每个数据源都有自己的连接字符串。
### 2. 使用多个 Prisma Client 实例 

当配置多个数据源时，可以为每个数据源生成不同的 Prisma Client 实例。在代码中，通过指定不同的 Prisma Client 实例来选择连接哪个数据库。

#### 示例：使用多个 Prisma Client 实例 


```javascript
import { PrismaClient as PrismaClient1 } from '@prisma/client/db1'; // PostgreSQL Client
import { PrismaClient as PrismaClient2 } from '@prisma/client/db2'; // MySQL Client

const prisma1 = new PrismaClient1();
const prisma2 = new PrismaClient2();

async function main() {
  const user = await prisma1.user.findUnique({ where: { id: 1 } });
  const post = await prisma2.post.findMany();
  console.log(user, post);
}

main()
  .catch(e => {
    throw e
  })
  .finally(async () => {
    await prisma1.$disconnect();
    await prisma2.$disconnect();
  });
```
在这个示例中，`prisma1` 使用 PostgreSQL 数据源，`prisma2` 使用 MySQL 数据源。通过这种方式，你可以同时操作多个数据库。
### 3. 数据源命名和连接字符串 
在 `schema.prisma` 文件中，你可以为每个数据源指定连接字符串，通常通过环境变量来传递连接信息。
#### 环境变量示例 


```bash
DATABASE_URL1=postgresql://user:password@localhost:5432/mydb
DATABASE_URL2=mysql://user:password@localhost:3306/mydb
```
确保你为每个数据源提供了正确的连接信息，并在 `prisma generate` 之前设置了这些环境变量。
### 4. 在应用中切换数据源 

Prisma 的设计目的是通过不同的 Prisma Client 实例在多个数据库之间进行切换。你可以根据需要在代码中选择性地连接不同的数据库，而无需每次都修改数据库配置。

## 注意事项 

- Prisma 在多个数据库连接的情况下，并不会自动合并数据源之间的操作，操作会局限于每个 Prisma Client 所连接的数据库。

- 在使用多个数据源时，需要仔细管理和切换连接，以避免数据混乱或错误。

- 在 Prisma 中支持多个数据库连接，但是要注意性能优化，避免在多个数据库之间频繁切换，影响性能。

## 结论 
通过配置多个 `datasource` 并为每个数据源生成不同的 Prisma Client 实例，开发者可以轻松地在 Prisma 中使用多个数据库。确保正确管理连接和操作，可以提高数据库的灵活性和可扩展性。

