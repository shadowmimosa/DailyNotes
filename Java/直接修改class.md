<font size=4 face='楷体'>

## 直接修改 class 值

一些古老的程序要修改的话, 其中引用了一些 jar 包导致无法直接编译，只能直接修改 `.class` 文件

- [修改.class 文件变量](https://segmentfault.com/a/1190000023909465)
  该方法使用 idea 安装 jclasslib-bytecode-viewer 插件
  没有 idea, 遂未尝试

### 反编译修改 class 文件变量

- 下载 [JClassLib_windows](<(https://github.com/ingokegel/jclasslib)>)
- 下载[jd-gui](https://github.com/java-decompiler/jd-gui) 或 [jadx](https://github.com/skylot/jadx)
  用来反编译 class 文件的(IDEA 也可以反编译 class 文件)
- 用 JClassLib 打开需要修改的 class 文件
  找到需要修改的函数方法位置
  点菜单的 code
  查看右侧的 Bytecode
  找到需要修改的变量
  点击, 会跳到变量区

- 替换变量
  写一个 Java 程序, 替换指定变量的值
  filePath 变量存在需要替换的 class 文件路径
  174 是需要替换的位置, Admin123 是希望替换的变量, 如果替换成中文需要注意目标编码 (不然会用 JVM 默认编码)

- 特别需要注意的是
  程序依赖 JClasslib 包下的 jclasslib-library.jar 包, 所以可以进到 JClasslib 安装路径下拷贝一个 jclasslib-library.jar 包文件放到 build path 内

- 完整代码

```java
// 需要替换三处，文件路径、变量位置、修改后目标变量

import java.io.DataInput;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.gjt.jclasslib.io.ClassFileWriter;
import org.gjt.jclasslib.structures.CPInfo;
import org.gjt.jclasslib.structures.ClassFile;
import org.gjt.jclasslib.structures.InvalidByteCodeException;
import org.gjt.jclasslib.structures.constants.ConstantUtf8Info;

public class Client
{
     @SuppressWarnings("deprecation")
    public static void main(String[] args){
         String filePath = "C:\\Users\\zw\\Desktop\\Client.class";
            FileInputStream fis = null;
            try {
                fis = new FileInputStream(filePath);
            } catch (FileNotFoundException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

            DataInput di = new DataInputStream(fis);
            ClassFile cf = new ClassFile();
            try {
                cf.read(di);
            } catch (InvalidByteCodeException e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            } catch (IOException e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            }
            CPInfo[] infos = cf.getConstantPool();

            int count = infos.length;
            for (int i = 0; i < count; i++) {
                if (infos[i] != null) {
                    System.out.print(i);
                    System.out.print(" = ");
                    try {
                        System.out.print(infos[i].getVerbose());
                    } catch (InvalidByteCodeException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                    System.out.print(" = ");
                    System.out.println(infos[i].getTagVerbose());
                    if(i == 174){
                        ConstantUtf8Info uInfo = (ConstantUtf8Info)infos[i];
                        uInfo.setBytes("Admin123".getBytes());
                        infos[i]=uInfo;
                    }
                }
            }
            cf.setConstantPool(infos);
            try {
                fis.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            File f = new File(filePath);
            try {
                ClassFileWriter.writeToFile(f, cf);
            } catch (InvalidByteCodeException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
}
```

## Reference
[class文件直接修改_反编译修改class文件变量](https://www.cnblogs.com/zhengwang/p/class.html)

**2022.07.27**
