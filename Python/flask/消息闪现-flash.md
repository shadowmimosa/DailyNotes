<font size=4 face='楷体'>

## 消息提示 - flash()

flask 提供了一个 flash() 函数, 它可以用来"闪现"需要提示给用户的消息
通过 flash()函数发送的消息会存储在 session 对象中，所以我们需要为程序设置秘钥
可以通过 app.secret_key 属性或配置变量 SECRET_KEY 设置

视图中, 通过 flash() 函数发送一条消息, 然后重定向到 index 视图

```python
@app.route('/flash')
def just_flash():
    flash('I am flash, who is looking for me?')
    return redirect(url_for('watchlist'))
```

在 base.html 模板中加入处理闪现消息的函数

```html
<main>
  {% for message in get_flashed_messages() %}
  <div class="alert">{{ message }}</div>
  {% endfor %} {% block content %}{% endblock %}
</main>
```

### Reference

[flask 模板应用-消息闪现（flash()）](https://www.cnblogs.com/xiaxiaoxu/p/10468103.html)

**2020.09.07**
