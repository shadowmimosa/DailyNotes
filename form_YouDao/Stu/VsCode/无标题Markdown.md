变量参考
Visual Studio Code支持调试和任务配置文件中的变量替换。使用$ {variableName}语法在launch.json和tasks.json文件中的键和值字符串内支持变量替换。

预定义的变量
支持以下预定义变量：

$ {workspaceFolder} - 在VS Code中打开的文件夹的路径
$ {workspaceFolderBasename} - VS代码中打开的文件夹的名称，没有任何斜杠（/）
$ {file} - 当前打开的文件
$ {relativeFile} - 当前打开的文件相对于workspaceFolder
$ {fileBasename} - 当前打开文件的基本名称
$ {fileBasenameNoExtension} - 当前打开文件的基本名称，没有文件扩展名
$ {fileDirname} - 当前打开文件的目录名
$ {fileExtname} - 当前打开文件的扩展名
$ {cwd} - 任务运行器在启动时的当前工作目录
$ {lineNumber} - 活动文件中当前选定的行号
$ {selectedText} - 活动文件中当前选定的文本
预定义变量示例
假设您有以下要求：

位于/home/your-username/your-project/folder/file.ext编辑器中打开的文件;
该目录/home/your-username/your-project作为根工作空间打开。
因此，每个变量都有以下值：

$ {workspaceFolder} -/home/your-username/your-project
$ {workspaceFolderBasename} -your-project
$ {file} -/home/your-username/your-project/folder/file.ext
$ {relativeFile} -folder/file.ext
$ {fileBasename} -file.ext
$ {fileBasenameNoExtension} -file
$ {fileDirname} -/home/your-username/your-project/folder
$ {fileExtname} -.ext
$ {lineNumber} -5
$ {selectedText} -Text selected in your code editor
提示：在字符串值内使用IntelliSense tasks.json，launch.json以获取预定义变量的完整列表。

环境变量
您还可以通过$ {env：Name}语法引用环境变量（例如，${env:PATH}）。

{
    "type": "node",
    "request": "launch",
    "name": "Launch Program",
    "program": "${workspaceFolder}/app.js",
    "cwd": "${workspaceFolder}",
    "args": [ "${env:USERNAME}" ]
}
注意：确保匹配环境变量名称的大小写，例如${env:Path}在Windows上。

设置和命令变量
您可以使用以下语法引用VS Code设置和命令：

$ {config：Name} - 示例：${config:editor.fontSize}
$ {command：CommandID} - 示例：${command:explorer.newFolder}
每个工作区文件夹的变量范围
通过将根文件夹的名称附加到变量（用冒号分隔），可以访问工作区的兄弟根文件夹。如果没有根文件夹名称，则该变量的范围限定为使用它的同一文件夹。

例如，在多根工作空间的文件夹Server和Client，一个${workspaceFolder:Client}指的路径Client根。

常见问题
用户和工作区设置是否支持变量替换？
不，settings.json文件中的字符串不支持预定义变量。一些设置一样window.title有自己的变量：

  "window.title": "${dirty}${activeEditorShort}${separator}${rootName}${separator}${appName}"
请参阅设置编辑器中的注释（Ctrl +，）以了解有关设置特定变量的信息。

为什么不记录$ {workspaceRoot}？
${workspaceRoot}不推荐使用该变量，${workspaceFolder}以便更好地与多根工作区支持保持一致。

[Link](https://code.visualstudio.com/docs/editor/variables-reference)