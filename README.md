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

### Java

You don't have to do this. But you *can*.

```Java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class hello {
    
    public static void main (String[] args) throws Exception {
        URL url = new URL("https://hello.sar.ai");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String text = in.readLine();
        in.close();
        System.out.print(text);
    }
}
```
