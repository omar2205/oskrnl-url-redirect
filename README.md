# oskrnl-url-redirect

Redirect URLs using Vercel and Redis

### **API**

|  Route   | Description                                      |
| :------: | ------------------------------------------------ |
| /go/:uid | redirect to URL associated with the uid          |
| /create  | Create URL <br>**Headers**: 'Content-Type: application/json'<br>**body**: {"url":"http://example.com"} |
