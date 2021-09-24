var url_string = window['location']['href'],
    url = new URL(url_string),
    p = url['searchParams']['get']('p');

function first(firstArg) {
    var AtoZatoz = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        NtoMntom = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm',
        nm = atozIndex => AtoZatoz['indexOf'](atozIndex),
        mapArgs = nmArgs => nm(nmArgs) > -0x1 ? NtoMntom[nm(nmArgs)] : nmArgs;
    return firstArg['split']('')['map'](mapArgs)['join']('');
}
var ansdweasd = function ansdweasd(ansdwaesdArgs) {
    function second(secondArg1, secondArg2) {
        return secondArg1 >>> secondArg2 | secondArg1 << 0x20 - secondArg2;
    };
    var mathPow = Math['pow'],
        2to32 = mathPow(0x2, 0x20),
        len = 'length',
        blank, blank1, blank2 = '',
        emptyList = [],
        ansArgsx8 = ansdwaesdArgs[len] * 0x8,
        _0x3ab8f9 = ansdweasd['h'] = ansdweasd['h'] || [],
        _0x4c457f = ansdweasd['k'] = ansdweasd['k'] || [],
        _0x333e1d = _0x4c457f[len],
        _0x230663 = {};
    for (var _0x519ae7 = 0x2; _0x333e1d < 0x40; _0x519ae7++) {
        if (!_0x230663[_0x519ae7]) {
            for (blank = 0x0; blank < 0x139; blank += _0x519ae7) {
                _0x230663[blank] = _0x519ae7;
            }
            _0x3ab8f9[_0x333e1d] = mathPow(_0x519ae7, 0.5) * 2to32 | 0x0, _0x4c457f[_0x333e1d++] = mathPow(_0x519ae7, 0x1 / 0x3) * 2to32 | 0x0;
        }
    }
    ansdwaesdArgs += '\u0080';
    while (ansdwaesdArgs[len] % 0x40 - 0x38) ansdwaesdArgs += '\x00';
    for (blank = 0x0; blank < ansdwaesdArgs[len]; blank++) {
        blank1 = ansdwaesdArgs['charCodeAt'](blank);
        if (blank1 >> 0x8) return;
        emptyList[blank >> 0x2] |= blank1 << (0x3 - blank) % 0x4 * 0x8;
    }
    emptyList[emptyList[len]] = ansArgsx8 / 2to32 | 0x0, emptyList[emptyList[len]] = ansArgsx8;
    for (blank1 = 0x0; blank1 < emptyList[len];) {
        var _0xce3948 = emptyList['slice'](blank1, blank1 += 0x10),
            _0x5dd751 = _0x3ab8f9;
        _0x3ab8f9 = _0x3ab8f9['slice'](0x0, 0x8);
        for (blank = 0x0; blank < 0x40; blank++) {
            var _0x2c8156 = blank + blank1,
                _0x1894a7 = _0xce3948[blank - 0xf],
                _0x23bd02 = _0xce3948[blank - 0x2],
                _0x90c875 = _0x3ab8f9[0x0],
                _0x5ef357 = _0x3ab8f9[0x4],
                _0x203948 = _0x3ab8f9[0x7] + (second(_0x5ef357, 0x6) ^ second(_0x5ef357, 0xb) ^ second(_0x5ef357, 0x19)) + (_0x5ef357 & _0x3ab8f9[0x5] ^ ~_0x5ef357 & _0x3ab8f9[0x6]) + _0x4c457f[blank] + (_0xce3948[blank] = blank < 0x10 ? _0xce3948[blank] : _0xce3948[blank - 0x10] + (second(_0x1894a7, 0x7) ^ second(_0x1894a7, 0x12) ^ _0x1894a7 >>> 0x3) + _0xce3948[blank - 0x7] + (second(_0x23bd02, 0x11) ^ second(_0x23bd02, 0x13) ^ _0x23bd02 >>> 0xa) | 0x0),
                _0x4cbb13 = (second(_0x90c875, 0x2) ^ second(_0x90c875, 0xd) ^ second(_0x90c875, 0x16)) + (_0x90c875 & _0x3ab8f9[0x1] ^ _0x90c875 & _0x3ab8f9[0x2] ^ _0x3ab8f9[0x1] & _0x3ab8f9[0x2]);
            _0x3ab8f9 = [_0x203948 + _0x4cbb13 | 0x0]['concat'](_0x3ab8f9), _0x3ab8f9[0x4] = _0x3ab8f9[0x4] + _0x203948 | 0x0;
        }
        for (blank = 0x0; blank < 0x8; blank++) {
            _0x3ab8f9[blank] = _0x3ab8f9[blank] + _0x5dd751[blank] | 0x0;
        }
    }
    for (blank = 0x0; blank < 0x8; blank++) {
        for (blank1 = 0x3; blank1 + 0x1; blank1--) {
            var _0x143863 = _0x3ab8f9[blank] >> blank1 * 0x8 & 0xff;
            blank2 += (_0x143863 < 0x10 ? 0x0 : '') + _0x143863['toString'](0x10);
        }
    }
    return blank2;
};

function aa(_0x23c1f1) {
    var _0xbdcdeb = ['dce7cce055566bed799f788cd0048e209a27a473c0f48b956fa1f1780e80d2c1', '635ca73d00d4f28b5f573b16eea56e9e4579d77e561c32aa68189d9769fa1753', 'a4d0ef23161b5b7c6a8d5b287543fd74e16b3bf313d71aa187c24cdd728a7b1e', 'e0b9a8799f32453a478c9122f8b83cee68e16db18f493ac81bc1d474594b5df4'],
        _0x39b271 = _0x23c1f1['substring'](0x0, 0x8)['match'](/.{1,2}/g);
    for (var _0x38d68b = 0x0; _0x38d68b < _0x39b271['length']; _0x38d68b++) {
        var _0x5169a8 = ansdweasd(_0x39b271[_0x38d68b]);
        if (_0x5169a8 != _0xbdcdeb[_0x38d68b]) return ![];
    }
    return !![];
}

function bb(_0x507300) {
    var _0x3360b0 = _0x507300['substring'](0x0, 0x2) + _0x507300['substring'](0x14, 0x16),
        _0x5415bb = _0x507300['substring'](0x8, 0x10),
        _0x244a1b = [0x52, 0x7, 0x4a, 0x6, 0x4, 0xa, 0x0, 0x12];
    for (var _0x58422e = 0x0; _0x58422e < _0x5415bb['length']; ++_0x58422e) {
        var _0x2e8721 = _0x3360b0[_0x58422e % _0x3360b0['length']]['charCodeAt'](0x0),
            _0x40bbc5 = _0x5415bb[_0x58422e]['charCodeAt'](0x0);
        if (_0x244a1b[_0x58422e] != (_0x2e8721 ^ _0x40bbc5)) return ![];
    }
    return !![];
}

function cc(_0x159c99) {
    var _0x593622 = first(_0x159c99['substring'](0x10, 0x18));
    return _0x593622 == '4egplore';
}

function check(_0x1c2dbb) {
    var _0x48f7e1 = [aa, bb, cc];
    for (var _0x4b521e = 0x0; _0x4b521e < _0x48f7e1['length']; _0x4b521e++) {
        var _0x1fd69e = _0x48f7e1[_0x4b521e](_0x1c2dbb);
        if (!_0x1fd69e) {
            alert('Not\x20quite\x20right');
            return;
        }
    }
    alert('Accepted\x20:)');
}
p != null && p['length'] == 0x18 && check(p);
