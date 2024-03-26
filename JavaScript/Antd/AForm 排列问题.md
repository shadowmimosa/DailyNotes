<font size=4 face='楷体'>

## Form 组件排列问题

当 Form 组件在宽度小于 550px 时， layout="horizontal" 失效
可以用 Token 配置响应式范围 [example](https://codesandbox.io/p/sandbox/biao-dan-bu-ju-antd-5-6-1-forked-3hd6lp?file=%2Fdemo.tsx%3A1%2C1-51%2C1)
```js
// demo.tsx

import React, { useState } from "react";
import "./index.css";
import { Button, Form, Input, ConfigProvider } from "antd";

type LayoutType = Parameters<typeof Form>[0]["layout"];

const App: React.FC = () => {
  const [form] = Form.useForm();
  const [formLayout, setFormLayout] = useState<LayoutType>("horizontal");

  const onFormLayoutChange = ({ layout }: { layout: LayoutType }) => {
    setFormLayout(layout);
  };

  const formItemLayout = { labelCol: { span: 4 }, wrapperCol: { span: 20 } };

  const buttonItemLayout = { wrapperCol: { span: 20, offset: 4 } };

  return (
    <ConfigProvider
      theme={{
        components: {
          Form: {
            screenXSMax: 0
          }
        }
      }}
    >
      <Form
        {...formItemLayout}
        layout="horizontal"
        form={form}
        initialValues={{ layout: formLayout }}
        onValuesChange={onFormLayoutChange}
      >
        <Form.Item label="Field A">
          <Input placeholder="input placeholder" />
        </Form.Item>
        <Form.Item label="Field B">
          <Input placeholder="input placeholder" />
        </Form.Item>
        <Form.Item {...buttonItemLayout}>
          <Button type="primary">Submit</Button>
        </Form.Item>
      </Form>
    </ConfigProvider>
  );
};

export default App;
```

### Reference

- [Form组件在宽度小于550px时， layout="horizontal"失效](https://github.com/ant-design/ant-design/issues/42957)

**2023.12.06**
