var wordlist = [ "getElementById", "value", "substring", "picoCTF{", "not_this", "37115}", "_again_3", "this", "Password Verified", "Incorrect password" ];

(function(_0x4bd822, _0x2bd6f7) {
	var _0xb4bdb3 = function(_0x1d68f6) {
		while (--_0x1d68f6) {
			_0x4bd822['push'](_0x4bd822['shift']());
		}
	};
	_0xb4bdb3(++_0x2bd6f7);
}(wordlist, 0x1b3));

var select = function(param1, param2) {
	param1 = param1 - 0x0;
	var word = wordlist[param1];
	return word;
};

// picoCTF{not_this_again_337115}

function verify() {
	checkpass = document.getElementById('pass').value;
	split = 0x4;
	if (checkpass.substring(0x0, split * 0x2) == "picoCTF{") {
		if (checkpass.substring(0x7, 0x9) == '{n') {
			if (checkpass.substring(split * 0x2, split * 0x2 * 0x2) == "not_this") {
				if (checkpass.substring(0x3, 0x6) == 'oct') {
					if (checkpass.substring(split * 0x3 * 0x2, split * 0x4 * 0x2) == "37115}") {
						if (checkpass.substring(0x6, 0xb) == 'f{not') {
							if (checkpass.substring(split * 0x2 * 0x2, split * 0x3 * 0x2) == "_again_3") {
								if (checkpass.substring(0xc, 0x10) == "this") {
									alert("Password Verified");
								}
							}
						}
					}
				}
			}
		}
	} else {
		alert("Incorrect password");
	}
}
