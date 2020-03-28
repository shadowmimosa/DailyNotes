<font size=4 face='楷体'>

## pdf 转图片

- 安装 poppler

  - Linux
    ```shell
    yum install poppler poppler-cpp-devel poppler-utils
    ```
  - Windows
    [这里](http://blog.alivate.com.au/poppler-windows/)下载，第三方打包的应用，或者[这里](https://github.com/tsdgeos/poppler_mirror/tree/master)自行打包

- 安装 pdf2image

  ```shell
  pip install pdf2image
  ```

- 脚本示例

  ```python
  from pdf2image import convert_from_path
  import tempfile

  def main(filename, outputDir):
      print('filename=', filename)
      print('outputDir=', outputDir)
      with tempfile.TemporaryDirectory() as path:
          images = convert_from_path(filename)
          for index, img in enumerate(images):
              img.save('%s/page_%s.png' % (outputDir, index))

  if __name__ == "__main__":
      main('source.pdf', 'pdfimage/')
  ```

  关键方法

  ```python
    convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm')
    convert_from_bytes(pdf_file, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm')
  ```

  参数说明

  ```
    thread_count ：允许设置用于转换的线程数；
    first_page ：允许设置由pdftoppm处理的第一个页面；
    last_page：允许设置最后一页由pdftoppm处理；
    fmt：允许指定输出格式。目前支持的格式是jpg、png和ppm；
  ```


### Reference

[使用 Python 将 PDF 转换成图片](https://blog.51cto.com/11142243/2299706)
[利用 Python 将 pdf 转为图片](https://www.jianshu.com/p/dd225ba31be4)

**2020.03.28**
