# Hello, Gorgeous
Twitter API to replace "Hello, world" with words of affirmation.

Live: https://hello.sar.ai/hello

## Using hello_gorgeous

### From the command line
```Shell
curl https://hello.sar.ai
```

### Python
```Python
import requests

requests.get('https://hello.sar.ai').text
```

### JavaScript

#### jQuery

```JavaScript
$.get("https://hello.sar.ai", callback);
```

#### ES6

```JavaScript
fetch("https://hello.sar.ai")
  .then(function(response) {
  return response.text().then(function(text) {
    callback(text);
  });
});
```
