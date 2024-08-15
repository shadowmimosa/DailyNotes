# 基本使用

## 快速开始

## 打开终端

### Windows 用户

> **⚠️注意**  
> Windows 用户请注意斜杠的区别，Windows 的路径分隔符是 `/` 而类 UNIX 系统则是 `\`，如果你指定了错误的符号，那么可能会出现找不到路径的问题导致程序执行失败。

Windows 用户在下载完成软件的压缩包之后，打开解压后的文件夹，按住 Shift + 右键呼出菜单，然后选择 PowerShell/命令提示符/Windows 终端，根据下述说明执行命令即可。

### macOS 用户

> **⚠️注意**  
> macOS 和 Linux 系统在文件解压完成之后，还需要确保其是否具备可执行权限。  
> 请使用 `sudo chmod +x ./ZonyLrcTools.Cli` 命令授予工具可执行权限。

按下 `Command+空格` 唤醒搜索框，在里面输入 `终端` 之后按回车会运行终端程序，它看起来像是这样。 ![image-20230813204445279](https://docs.myzony.com/Images/image-20230813204445279.png)

![image-20230813204520840](https://docs.myzony.com/Images/image-20230813204520840.png)

### Linux 用户

> **⚠️注意**  
> macOS 和 Linux 系统在文件解压完成之后，还需要确保其是否具备可执行权限。  
> 请使用 `sudo chmod +x ./ZonyLrcTools.Cli` 命令授予工具可执行权限。

既然你已经使用 Linux 系统了，那么你肯定知道如何打开 Terminal，这里不再详细赘述如何打开终端，仅提醒使用者注意程序是否拥有可执行权限。

## 下载歌词

这里假设你需要下载歌词的歌曲文件夹，其路径是 `C:\歌曲目录` 或 `/media/music`，直接执行以下指令即可进行下载操作。

**Windows**

```
.\ZonyLrcTools.Cli.exe download -d "C:\歌曲目录" -l -n 2
```

**macOS/Linux**

```
./ZonyLrcTools.Cli download -d "/media/music" -l -n 2
```

## 下载专辑封面

这里假设你需要下载歌词的歌曲文件夹，其路径是 `C:\歌曲目录` 或 `/media/music`，直接执行以下指令即可进行下载操作。

**Windows**

```
.\ZonyLrcTools.Cli.exe download -d "C:\歌曲目录" -a -n 2
```

**macOS/Linux**

```
./ZonyLrcTools.Cli download -d "/media/music" -a -n 2
```

## 格式转换

如果你拥有某些特定格式的歌曲，例如 `*.ncm` 需要转换为通用格式 `*.flac` / `*.mp3` ，可以直接使用以下命令进行转换。

这里以加密歌曲路径 `C:\加密歌曲` 或 `/media/ncm-music` 为例。 **Windows**

```
.\ZonyLrcTools.Cli.exe util -s C:\加密歌曲
```

**macOS/Linux**

```
.\ZonyLrcTools.Cli.exe util -s /media/ncm-music
```

## 歌词下载

歌词下载功能是本工具的核心功能，本节主要介绍了歌词下载子命令 `download` 的常见参数和使用方法。

## 命令结构

执行 `./ZonyLrcTools.Cli download -h` 指令可以得到具体的帮助信息，常规情况来说它会输出以下内容。

```
zony@Zonys-MBP TempFiles % ./ZonyLrcTools.Cli download -h
[21:18:12 INF] Starting...
下载歌词文件或专辑图像。

Usage: lyric-tool download [options]

Options:
  -h|--help          欢迎使用 ZonyLrcToolsX Command Line Interface，有任何问题请访问 https://soft.myzony.com 或添加 QQ 群 337656932 寻求帮助。
  -d|--dir           指定需要扫描的目录。
  -l|--lyric         指定程序需要下载歌词文件。
  -a|--album         指定程序需要下载专辑图像。
  -n|--number        指定下载时候的线程数量。(默认值 1)
                     Default value is: 1.
  -sc|--scanner      指定歌词文件扫描器，目前支持本地文件(local)，网易云音乐(netease)，csv 文件(csv)，默认值为 local。
                     Default value is: local.
  -o|--output        指定歌词文件的输出路径。
                     Default value is: DownloadedLrc.
  -p|--pattern       指定歌词文件的输出文件名模式。
                     Default value is: {Artist} - {Name}.lrc.
  -f|--file          指定 CSV 文件的路径。
  -s|--song-list-id  指定网易云音乐歌单的 ID，如果有多个歌单，请使用 ';' 分割 ID。
```

其中几个参数是必填的，从 [快速开始](https://docs.myzony.com/#/quickstart) 说明我们可以看到，下载歌词时必须传递 `-d` 和 `-l`/`-a` 参数。其中 `-l` 说明我们要下载歌词，而 `-a` 则表明我们需要下载专辑图像。两个参数二选一提供即可，如果同时提供则不会有任何效果。

## 参数详解

### 线程数量

`-n` 选项用于指定下载歌词时的线程数量，理论上来说线程数量越多，同时下载的歌词文件就越多，整体的下载速度越快。  
但是由于歌词源服务器的检测和限制，如果同一个 IP 地址同时在短时间内发起大量下载请求，会导致服务器对这个 IP 进行临时封禁，程序就会提示大量的下载错误信息。  
因此，这个线程数量一般建议设置为 `1` 或者 `2`，这样可以保证程序在下载歌词的时候不会被服务器进行限制。

### 文件扫描器

`-sc` 选项用于指定歌曲信息的来源，默认情况下会使用 `local` 扫描器以歌曲的元信息(标签)，或者是文件名来作为歌词搜索的依据。对应的歌词文件也会在歌曲所在目录生成，不需要用户执行多余的操作。  
**支持的扫描器**  
| 参数值 | 说明 | | --- | --- | | local | 从指定目录的歌曲文件中获取歌曲信息。 | | netease | 从网易云歌单获取歌曲信息。 | | csv | 从 CSV 文件获取歌曲信息。 |

#### 网易云歌曲扫描器

使用网易云歌曲扫描器(`netease`)的完整命令如下:

```
.\ZonyLrcTools.Cli.exe download -sc netease -o "D:\TempFiles" -s "7224428149" -l
```

其中 `-sc` 参数用于指定歌词信息的来源是网易云歌单; `-o` 参数指定的是歌词文件的输出目录，请尽量使用绝对路径; `-s` 参数指定的的是歌单的 ID，该 ID 可以从网页版的网易云音乐获得。  
例如获取地址 [https://music.163.com/#/playlist?id=158010361](https://music.163.com/#/playlist?id=158010361) 的歌单信息，那么歌单 ID 就应该传递 158010361。  
如果你需要获取多个歌单的歌曲数据，请在传递歌单 ID 时使用分号 `;` 指定多个 ID，例如下面的命令就是下载两个歌单的歌曲数据。

```
.\ZonyLrcTools.Cli.exe download -sc netease -o "D:\TempFiles" -s "7224428149;158010361" -l
```

由于网易云音乐的限制，要想获取完整的歌单信息，必须扫码登录程序，还是以最上面的为例，我需要下载歌单内的歌词数据，就必须扫码之后程序才会执行。  
![QR_CODE](https://docs.myzony.com/Images/image-20230328223155280.png)

### CSV 歌曲扫描器

应 [Issue 126](https://github.com/real-zony/ZonyLrcToolsX/issues/126) 的请求，增加了从 CSV 获取歌曲信息的方式。这样可以在没有原始歌曲的情况下载歌词数据。  
示例命令:

```
.\ZonyLrcTools.Cli.exe download -sc csv -o "D:\TempFiles" -f "D:\TempFiles\demo.csv" -l
```

其中 `-f` 参数用于指定 csv 文件的路径，csv 文件的格式应该如下所示，保证第一行是列信息，一共要包含两列。

```
Song,Artist
刀马旦,李玟
发如雪,周杰伦
说书人,寅子
爱的供养,张国荣
七里香,周杰伦
```

### 歌词输出路径

`-o` 选项可以指定歌词文件最终输出的路径，如果你的扫描器指定的是`local` 以外的扫描器的话，这个参数是必填项。  
这是因为默认的 `local` 扫描器会直接将歌词文件输出到歌曲所在目录，而其他的扫描器，例如网易云歌单扫描器，因为没有原始歌曲文件的路径，所以只能由用户自己指定一个目录用于存储歌词文件。

## 加密格式转换

子命令为 `util`，可用于转换部分加密歌曲，**仅供个人研究学习使用，思路与源码都来自于网络**。  
具体支持的格式请参考项目 [MusicDecrypto](https://github.com/davidxuang/MusicDecrypto/blob/master/MusicDecrypto.Library/DecryptoFactory.cs#L23)，本工具仅做一个集成，替换掉原本自己的一些实现。现在不需要指定对应的类型参数，程序会自动根据文件后缀选择适合的解密算法。

命令只需要一个参数 `-s`，指定需要转换的文件夹或者是文件路径。

```
.\ZonyLrcTools.Cli.exe util -s D:\CloudMusic
```

或者你可以直接使用 [MusicDecrypto](https://github.com/davidxuang/MusicDecrypto) 来转换那些加密的格式。

# 高级配置

## 歌词编码

目前程序支持修改 `config.yaml` 文件里面的配置，来改变输出歌词文件的编码格式。  
完整支持的编码列表请参考: [MSDN Encoding 列表](https://learn.microsoft.com/en-us/dotnet/api/System.Text.Encoding.GetEncodings?view=net-6.0#examples)，使用 `identifier and name` 作为参数值填入 `config.yaml` 文件当中的 `fileEncoding`。

具体的位置请参考下面的定位:

```
globalOption:
  provider:
    lyric:
      config:
        fileEncoding: 'utf-8'           # 歌词文件的编码格式。
```

> ⚠️**注意** 针对 UTF-8 BOM 格式，程序进行了特殊处理，请在 `fileEncoding` 里面填写 "utf-8-bom" 以支持。

例:

```
globalOption:
  provider:
    lyric:
      config:
        fileEncoding: 'utf-8-bom'           # 歌词文件的编码格式。
```

## 歌词源

目前支持的歌词源有以下几种，其默认的优先级如下: | 歌词源 | 默认优先级 | | ---------- | ---------- | | 网易云音乐 | 1 | | QQ 音乐 | 2 | | 酷狗音乐 | 3 | | 酷我音乐 | 4 |

## 优先级

从上面的表格可以知道歌词源的默认优先级，当然你也可以更改这个优先级，比如你觉得 QQ 音乐的歌词更加准确，那么你可以让工具优先从 QQ 音乐下载歌词。  
修改优先级的方法在 CLI 当中就是修改 `config.yaml` 文件，在文件内找到这一部分代码。

```
globalOption:
  provider:
    lyric:
      plugin:
        - name: NetEase   # 基于网易云音乐的歌词下载器。
          priority: 1     # 优先级，升序排列，改为 -1 时禁用。
          depth: 10       # 搜索深度，值越大搜索结果越多，但搜索时间越长。
        - name: QQ        # 基于 QQ 音乐的歌词下载器。
          priority: 2
          # depth: 10     # 暂时不支持。
        - name: KuGou     # 基于酷狗音乐的歌词下载器。
          priority: 3
          depth: 10
        - name: KuWo      # 基于酷我音乐的歌词下载器。
          priority: 4
          depth: 10
```

根据上面的描述，我们可以修改 `priority` 的值，以便调整歌词源的优先级，或者是直接禁用掉某个歌词源，让工具仅从你指定的歌词源下载歌词。

## 搜索深度

所谓的搜索深度，本质上是工具在搜索歌词的时候的搜索次数。假如某首歌曲的正确歌词在搜索结果的第10条，但是搜索深度是 5，那么工具就不会匹配到正确的歌词。在这种情况下，工具只会取一个默认值，也就是搜索结果的第 1 条结果作为最终的歌词文件。  
搜索深度的值一般来说不需要变更，这个参数跟线程数量一样，如果调整值过大则会影响下载效率。

## 网络代理

如果你的网络受到限制无法直接访问歌词源服务器，那么你可以考虑启用网络代理。  
目前工具仅支持 HTTP 代理，这部分的配置在 `config.yaml` 当中，下面的代码是一个示例。

```
globalOption:
  # 网络代理服务设置，仅支持 HTTP 代理。
  networkOptions:
    isEnable: false # 是否启用代理。
    ip: 127.0.0.1   # 代理服务 IP 地址。
    port: 4780      # 代理服务端口号。
    updateUrl: https://api.myzony.com/lrc-tools/update # 更新检查地址。
```

其中 `updateUrl` 一般不需要做变更，保持原样即可。  
网络代理的其他参数如上所示，你只需要填写你的 HTTP 代理服务器的 IP 和端口即可。

## 屏蔽字典

屏蔽字典适用于网易云音乐歌词下载，针对某些单词，网易云音乐使用了 \* 号进行屏蔽，这个时候可以使用屏蔽字典，设置歌曲名的关键词替换。例如有一首歌曲叫做 _Fucking ABC_ ，这个时候网易云实际的名字是 _Fu\*\*\*\*ing_ ，用户只需要在屏蔽字典加入替换逻辑即可，例如:

```
{
    "Fuckking": "Fu****ing"
}
```

屏蔽字典默认路径为程序所在目录的 _BlockWords.json_ 文件，用户可以在 _appsettings.json_ 文件中配置其他路径。

# 配置规范(Spec)

程序的所有的配置信息，都在 `config.yaml` 进行更改，下面标注了各个配置的说明。  
其中是否开启的可选项为 `true` 或者 `false`，等同于中文的 **是** 和 **否**。

## 默认配置文件内容

```
globalOption:
  # 允许扫描的歌曲文件后缀名。
  supportFileExtensions:
    - '*.mp3'
    - '*.flac'
    - '*.wav'
  # 网络代理服务设置，仅支持 HTTP 代理。
  networkOptions:
    isEnable: false # 是否启用代理。
    ip: 127.0.0.1   # 代理服务 IP 地址。
    port: 4780      # 代理服务端口号。
    updateUrl: https://api.myzony.com/lrc-tools/update # 更新检查地址。
  
  # 下载器的相关参数配置。
  provider:
    # 标签扫描器的相关参数配置。
    tag:
      # 支持的标签扫描器。
      plugin:
        - name: Taglib    # 基于 Taglib 库的标签扫描器。
          priority: 1     # 优先级，升序排列。
        - name: FileName  # 基于文件名的标签扫描器。
          priority: 2
          # 基于文件名扫描器的扩展参数。
          extensions:
            # 正则表达式，用于匹配文件名中的作者信息和歌曲信息，可根据
            # 自己的需求进行调整。
            regularExpressions: "(?'artist'.+)\\s-\\s(?'name'.+)"
      # 歌曲标签屏蔽字典替换功能。
      blockWord:
        isEnable: false             # 是否启用屏蔽字典。
        filePath: 'BlockWords.json' # 屏蔽字典的路径。
    # 歌词下载器的相关参数配置。
    lyric:
      # 支持的歌词下载器。
      plugin:
        - name: NetEase   # 基于网易云音乐的歌词下载器。
          priority: 1     # 优先级，升序排列，改为 -1 时禁用。
          depth: 10       # 搜索深度，值越大搜索结果越多，但搜索时间越长。
        - name: QQ        # 基于 QQ 音乐的歌词下载器。
          priority: 2
          # depth: 10     # 暂时不支持。
        - name: KuGou     # 基于酷狗音乐的歌词下载器。
          priority: 3
          depth: 10
        - name: KuWo      # 基于酷我音乐的歌词下载器。
          priority: 4
          depth: 10
      # 歌词下载的一些共有配置参数。
      config:
        isOneLine: true                 # 双语歌词是否合并为一行展示。
        lineBreak: "\n"                 # 换行符的类型，记得使用双引号指定。
        isEnableTranslation: true       # 是否启用翻译歌词。
        isOnlyOutputTranslation: false  # 是否只输出翻译歌词。
        isSkipExistLyricFiles: false    # 如果歌词文件已经存在，是否跳过这些文件。
        fileEncoding: 'utf-8'           # 歌词文件的编码格式。
```

[ZonyLrcToolsX](https://docs.myzony.com/#/)
