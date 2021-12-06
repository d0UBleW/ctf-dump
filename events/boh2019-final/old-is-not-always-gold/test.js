// decrypt result from "echo supersecret | openssl des3 | xxd -p"

var forge = require('node-forge');

function decrypt(encryptedHex, password) {
    var input = forge.util.hexToBytes(encryptedHex);
    input = forge.util.createBuffer(input);

    // skip 'Salted__';
    input.getBytes('Salted__'.length);
    // read 8-byte salt
    var salt = input.getBytes(8);

    // 3DES key and IV sizes
    var keySize = 24;
    var ivSize = 8;

    var derivedBytes = forge.pbe.opensslDeriveBytes(
        password, salt, keySize + ivSize);
    var buffer = forge.util.createBuffer(derivedBytes);
    var key = buffer.getBytes(keySize);
    var iv = buffer.getBytes(ivSize);
    console.log(key);
    console.log("hi");
    console.log(iv);
    console.log("hi");

    var decipher = forge.cipher.createDecipher('3DES-ECB', key);
    decipher.start({iv: iv});
    decipher.update(input);
    var result = decipher.finish(); // check 'result' for true/false
    if(!result) {
        console.log('decryption failed');
        return;
    }

    // get result as hex
    var hex = decipher.output.toHex();
    console.log(hex);
    // OR get result as a binary-encoded string
    // var bytes = decipher.output.getBytes();
    return hex;
}

// decrypt('53616c7465645f5f09e6d3507565a380e3cd6ff5f0bab8adcb50ed251a8cab11', 'test');

decrypt('53616c7465645f5fd6c62248af830f1355a74f729bf15131aba66eb94947328c1c546a5650d1aff39423d918436ccd5f53f50279602249a1', 'friend');
