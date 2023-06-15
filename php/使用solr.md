<font size=4 face='楷体'>

## 原生 php 使用 solr

Solr 是一个独立的企业级搜索应用服务器，它对外提供类似于 Web-service 的 API 接口。用户可以通过 http 请求，向搜索引擎服务器提交一定格式的 XML 文件，生成索引；也可以通过 Http Get 操作提出查找请求，并得到 XML 格式的返回结果。

php 官方的 solr 扩展貌似只支持到了 php5.9：

```php
PHP Version: PHP version 5.99.99 or older
PHP Version: PHP 5.3 or newer
PEAR Package: PEAR 1.4.0 or newer
PHP Extension: libxml
```

不过好在公司的这个系统比较老，php 用的 5.4。如果使用的是框架比如 YII，有专门的 solr 包，composer 安装一下就好，使用的并不是这个扩展进行的查询，所以这个不需要担心。

php 安装 solr 扩展
下载扩展，下载地址为：http://pecl.php.net/package/solr

```bash
tar zxf solr-2.4.0.tgz
cd solr-2.4.0
[php安装路径]bin/phpize
./configure --with-php-config=[php安装路径]/bin/php-config
make && make install
```

安装完后会有类似这样的提示：

```bash
Installing shared extensions: /usr/local/lib/php/extensions/no-debug-non-zts-20090626/
```

修改 php 的 php.ini 文件：在文件末尾加上

```bash
extension_dir = "/usr/local/php/lib/php/extensions/no-debug-non-zts-20090626/"
extension=solr.so
```

如果 extension_dir 目录已经添加，则只添加 extension 即可

查询方法

```php
<?php
class SolrList
{

    private $options = ['hostname' => 'X.X.X.X', 'port' => '8983', 'login' => '', 'password' => '']; //solr配置
    private $coreList = ['item', 'news']; //允许的solr库
    private $queryObj;  //solr查询对象


    /**
     * @description: 初始化solr对象
     * @author: injurys
     * @param string $core solr库名
     */
    public function __construct($core='')
    {
        if(empty($core) || !in_array($core, $this->coreList)){
            var_dump('solr库选择异常：库名不能为空或者库不存在！');exit();
        }
        $this->options['path'] = 'solr/'.$core;
        $this->queryObj = new SolrQuery();
    }


    /**
     * @description: 拼接转化where
     * @author: injurys
     * @param array $where 查询条件
     *        转化前：
     *              [
     *                  ['=', 'field', 'value'],
     *                  ['<>', 'field', 'value'],
     *                  ['between', 'field', ['value1', 'value2']],
     *                  ['in', 'field', ['value1', 'value2']],
     *                  ['not in', 'field', ['value1', 'value2']]
     *              ]
     *        转化后：
     *              [
     *                  ['+field:value'] field=value
     *                  ['-field:value'] field<>value
     *                  ['+field:[value1 TO value2]'] field > value and field < value2
     *                  ['+field:value1+field:value2'] field in (value1,value2)
     *                  ['-field:value1+-field:value2'] field not in (value1,value2)
     *              ]
     * @return $this
     */
    public function where($where=[]){
        if(!empty($where) && count($where)>=1){
            $condition = [];
            if(is_array($where[0])){
                foreach ($where as $val){
                    if(count($val) == 3){
                        $condition[] = $this->getWhere(trim($val[0]), trim($val[1]), $val[2]);
                    }
                }
            }elseif(count($where) == 3){
                $condition[] = $this->getWhere(trim($where[0]), trim($where[1]), $where[2]);
            }
            if(!empty($condition)){
                $this->queryObj->setQuery(implode(' AND ', $condition));
            }
        }
        return $this;
    }



    /**
     * @description: 设置页码
     * @author: injurys
     * @param int $pageNumber 页码
     * @param int $pageSize   每页条数
     * @return $this
     */
    public function page($pageNumber=1, $pageSize=20)
    {
        $pageNumber = max(intval($pageNumber), 1);
        $pageSize = max(intval($pageSize), 1);
        $start = ($pageNumber <= 1) ? 0 : ($pageNumber - 1) * $pageSize;
        $this->queryObj->setStart($start);
        $this->queryObj->setRows($pageSize);
        return $this;
    }

    /**
     * @description: 排序
     * @author: injurys
     * @param array $sort 排序
     *        ['field'=>"desc", 'field'=>'asc']
     * @return $this
     */
    public function order($sort=[])
    {
        if($sort){
            foreach($sort as $k => $v){
                $rule = strtolower($v);
                if($rule == 'asc'){
                    $this->queryObj->addSortField($k, SolrQuery::ORDER_ASC);
                }elseif($rule == 'desc'){
                    $this->queryObj->addSortField($k, SolrQuery::ORDER_DESC);
                }
            }
        }
        return $this;
    }

    /**
     * @description: 设置查询字段
     * @author: injurys
     * @param array $field 查询字段
     *        ['field1','field2']
     * @return $this
     */
    public function field($field=[])
    {
        if($field && is_array($field)){
            foreach($field as $key => $val){
                $this->queryObj->addField($val);
            }
        }
        return $this;
    }

    /**
     * @description: 执行查询
     * @author: injurys
     * @return array
     */
    public function all()
    {
        $client = new SolrClient($this->options);
        $result = $client->query($this->queryObj);
        $result = $result->getResponse();
        $num = $result->response->numFound;
        $list = [];
        if($num && $result->response->docs){
            $listData = [];
            foreach ($result->response->docs as $v){
                $listData[] = get_object_vars($v);
            }
            $list = ['count'=>$num, 'list'=>$listData];
        }
        return $list;
    }

/**
     * @description: 解析where转化为solr查询使用的条件
     * @author: injurys
     * @param string $operator
     * @param string $field
     * @param string $value
     * @return string
     */
    private function getWhere($operator='', $field='', $value='')
    {
        $condition = '';
        $value = is_array($value) ? $value : trim($value);
        switch ($operator){
            case "=":
            case "<>":
                $symbol = $operator == '=' ? '' : '-';
                $condition .= $symbol.$field.':'.$value.'';
            break;
            case "in":
            case "not in":
                $value = is_array($value) ? $value : explode(',', $value);
                $symbol = $operator == 'in' ? '' : '-';
                $valIn = [];
                foreach ($value as $v){
                    $valIn[] = $symbol.$field.':'.$v;
                }
                $condition .= '('.implode(' OR ',$valIn).')';
            break;
            case "between":
                if(is_array($value) && count($value) == 2){
                    $condition .= $field.':['.$value[0].' TO '.$value[1].']';
                }
            break;
            case "like":
                $condition .= $field.':*'.$value.'*';
            break;
            case ">=":  //大于等于
            case "<=":  //小于等于
                $info = $operator == '<=' ? '[* TO '.$value.']' : '['.$value.' TO *]';
                $condition .= $field.':'.$info.'';
            break;
        }
        return $condition;
    }
}
```

查询使用方法

```php
$solrList = new SolrList('item');
$where = [
    ['in', 'type', '1,2,3'],
    ['not in', 'type', [1,2,3]],
    ['=', 'type', 1],
    ['like', 'name', '小明'],
    ['between', 'ymd', [20190301, 20190310]],
    ['>=', 'type', 10],
    ['<=', 'type', 10]
];
$order = ['id'=>'desc','type'=>'asc'];
$page = 1;
$pageSize = 10;
$field = ['id', 'name', 'type'];
$list = $SolrList
    ->where($where)
    ->order($order)
    ->page($page, $pageSize)
    ->field($field)
    ->all();
```

### Reference

[原生 php 使用 solr 全文搜索引擎（扩展安装）](http://blog.hug-code.cn/article/1045.shtml)
