# Certificate



[https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/](https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/)



Convert DER to PEM

```bash
$ openssl x509 -inform der -in cert.der -out cert.pem
```



Read DER

```bash
$ openssl x509 -inform der -text -noout -in cert.der
```



Read PEM

```bash
$ openssl x509 -text -noout -in cert.pem
```
