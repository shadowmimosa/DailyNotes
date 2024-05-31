<font size=4 face='楷体'>

## Python difflib 包的 Golang 实现

- [go-difflib](https://github.com/pmezard/go-difflib)
  Partial port of Python difflib package to Go
- [go-diff](https://github.com/sergi/go-diff)
  Diff, match and patch text in Go
- [diff](https://github.com/nao1215/diff)
  diff is a partial port of Python difflib module

### 使用参考

可以参考 [mongo-go-driver](https://github.com/mongodb/mongo-go-driver/blob/bb699bdb84dc1e61ebb0944a5877c50989ddd0af/internal/assert/difflib.go) 直接 copy 到项目中

```go
// Copied from https://github.com/pmezard/go-difflib/blob/5d4384ee4fb2527b0a1256a821ebfc92f91efefc/difflib/difflib.go

// Copyright 2013 Patrick Mezard. All rights reserved. Use of this source code is
// governed by a license that can be found in the THIRD-PARTY-NOTICES file.

package assert

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
...
```

### Reference

**2024.05.24**
