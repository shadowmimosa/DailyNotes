## 为什么使用双 Token 机制？——JWT 与 OAuth2 的安全性探讨

在实际开发中，很多人对使用双 Token（`access_token`和`refresh_token`）机制有疑问，认为单 Token 是否也能实现相同功能。为了更好地理解这个问题，我们需要区分 JWT 和 OAuth2 这两个概念，并探讨双 Token 机制的必要性。

### JWT 与 OAuth2 的区别

**JWT（JSON Web Token）** 只是定义了一个 Token 的编码、加密和解密方式，并不限制如何使用这个 Token。**OAuth2** 则是一种认证规范，其中包含`access_token`和`refresh_token`。虽然很多实践中这两个 Token 使用 JWT 构建，但 OAuth2 只要求这两个 Token 是能够识别用户登录状态的字符串。

### 为什么 OAuth2 需要双 Token？

OAuth2 定义了资源服务器和授权服务器的分离。初次认证时，授权服务器会颁发`access_token`和`refresh_token`两个 Token：

- **Access Token**：用于访问资源服务器上的资源，传输频率高，通常有效期较短。
- **Refresh Token**：用于在`access_token`失效后获取新的`access_token`，传输频率低，有效期较长。

这种设计的原因在于安全性考虑。资源服务器通常不完全可信，不能暴露`refresh_token`，否则可能会被用来提权。因此，`access_token`仅用于访问资源，而`refresh_token`则由授权服务器来管理，用于更新`access_token`。

### 双 Token 机制的实际应用与优势

在典型的系统流程中，用户登录后会获得`access_token`和`refresh_token`。在后续请求中，仅需携带`access_token`。当`access_token`即将失效时，可以通过`refresh_token`获取新的`access_token`，从而避免频繁要求用户重新登录。

双 Token 设计的核心优势在于安全性：

1. **降低风险**：`access_token`使用频繁且有效期短，即使被窃取，损失也较小。而`refresh_token`使用频率低，有效期长，藏得更“深”，安全性更高。
2. **灵活控制**：服务端可以根据操作的安全等级，设置不同的 Token 过期时间，灵活控制安全策略。
3. **提升用户体验**：只要用户在`refresh_token`失效前操作，理论上可以避免频繁输入密码验证身份，提供更好的用户体验。

### 刷新令牌的作用

假设用户登录后，黑客截获了`access_token`和`refresh_token`，那么：

- 黑客只能在`access_token`过期前进行攻击。
- 当黑客尝试使用`refresh_token`获取新的`access_token`时，服务端可以通过 IP 变化等信息识别异常，要求用户重新验证身份。

使用单 Token 的设计虽然可以通过缩短 Token 的有效期来提高安全性，但这会导致用户频繁输入密码，不仅影响体验，还可能增加密码泄露的风险。因此，双 Token 机制在安全性和用户体验之间取得了平衡。

### 总结

双 Token 机制不仅解决了 Token 失效后的续签问题，还通过减少高频使用 Token 的有效期降低了被窃取的风险，同时让低频使用的`refresh_token`承担了安全控制的重任。这种设计已被广泛采纳，成为保障系统安全的重要策略。

### Reference

[jwt 续签为什么要使用双 token,是否单个 token 也可以吗?](https://zhuanlan.zhihu.com/p/683939210)
[JWT, 为什么需要刷新令牌?](https://www.jianshu.com/p/693aa7b1394e)

**2024.09.04**
