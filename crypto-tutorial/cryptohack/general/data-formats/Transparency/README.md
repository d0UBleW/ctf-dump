Given: a public RSA key that is used in the x509 certificate for the https connection to a cryptohack subdomain

We could of course take the easy way, and use our knowledge that the key is used for a cryptohack subdomain, and just query https://crt.sh/?q=cryptohack.org or whatever other service (such as the google page referenced in other solutions) can provide us with an overview of subdomains with https that are visible to certificate transparency.

Where it gets more interesting however, is when we would choose to discard that knowledge, and try to find the corresponding domain name based only on the public key we've been given. crt.sh does offer search by certificate fingerprint too, but we've only been given the public key, and not the full certificate (which would also include the subdomain name anyway, so that would have been even more boring). Instead, we'll use https://censys.io/certificates, which does also index the sha256 fingerprint of the subject key info field in the x509 certificate; aka the public key.

The SHA256 fingerprint is simply the SHA256 hash of the DER representation of the public key, so a simple shell command through openssl will give us what we need.

openssl pkey -outform der -pubin -in transparency.pem | sha256sum

Taking the output and querying it on the censys site, we arrive at an overview of the certificate we're interested in, including it's CN field: the subdomain: https://censys.io/certificates?q=29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2

