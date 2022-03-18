const dick = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "a": 26,
    "b": 27,
    "c": 28,
    "d": 29,
    "e": 30,
    "f": 31,
    "g": 32,
    "h": 33,
    "i": 34,
    "j": 35,
    "k": 36,
    "l": 37,
    "m": 38,
    "n": 39,
    "o": 40,
    "p": 41,
    "q": 42,
    "r": 43,
    "s": 44,
    "t": 45,
    "u": 46,
    "v": 47,
    "w": 48,
    "x": 49,
    "y": 50,
    "z": 51,
    "0": 52,
    "1": 53,
    "2": 54,
    "3": 55,
    "4": 56,
    "5": 57,
    "6": 58,
    "7": 59,
    "8": 60,
    "9": 61,
    " ": 62,
    ",": 63
};


function random(k) {
    k = Math.floor(k / 4);
    const hexString = Array(k)
        .fill()
        .map(() => Math.round(Math.random() * 0xF).toString(16))
        .join('');
    return BigInt(`0x${hexString}`);
}

function gcd(a, b) {
    if (!b) return a
    return gcd(b, a % b)
}


function getRandomBigInt(lower, upper) {
    let maxInt = BigInt(Number.MAX_SAFE_INTEGER);
    if (upper <= maxInt) {
        x = BigInt((Math.floor(Math.random() * Number(upper))));
        while (x < lower || x > upper) {
            x = BigInt((Math.floor(Math.random() * Number(upper))));
        }
        return x
    } else {
        x = BigInt((Math.floor(Math.random() * Number(upper))));
        while (x < lower || x > upper) {
            x = BigInt((Math.floor(Math.random() * Number(upper))));
        }
        return BigInt((Math.floor(Math.random() * Number.MAX_SAFE_INTEGER)));
    }

}

function powerMod(base, exponent, modulus) {
    base = BigInt(base)
    exponent = BigInt(exponent)
    modulus = BigInt(modulus)
    if (modulus === 1) return 0;
    result = 1n;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2n === 1n)  //odd number
            result = (result * base) % modulus;
        exponent = exponent >> 1n; //divide by 2
        base = (base * base) % modulus;
    }
    return result;
}


function modExp(x, e, n) {
    x = BigInt(x)
    e = BigInt(e)
    n = BigInt(n)
    let result = 1n
    while (true) {
        if (e & 0b1n) {
            result = (result * x) % n
        }
        if (e === 1n) {
            return result
        }
        x = (x * x) % n
        e >>= 1n
    }
}

function sqrt(value) {
    if (value < 0n) {
        throw 'square root of negative numbers is not supported'
    }

    if (value < 2n) {
        return value;
    }

    function newtonIteration(n, x0) {
        const x1 = ((n / x0) + x0) >> 1n;
        if (x0 === x1 || x0 === (x1 - 1n)) {
            return x0;
        }
        return newtonIteration(n, x1);
    }

    return newtonIteration(value, 1n);
}

function is_prime(n) {
    for (let i = 2n; i < sqrt(n) + 1n; ++i) {
        if (n % i === 0n) return false
    }
    return true
}


function miller_rabin(n, k = 40) {
    if (n === 2) return true;

    if (n % 2n === 0n) return false;

    s = BigInt(0);
    t = n - 1n;

    while (t % 2n === 0) {
        s += 1n;
        t = t / 2n;
    }

    for (let i = 0; i < k; ++i) {
        a = getRandomBigInt(2, n - 3n);
        x = modExp(a, t, n);
        if (x === 1n || x === (n - 1n)) continue;
        boule = true;
        for (let j = 0; j < s - 1n; ++j) {
            x = modExp(x, 2n, n);
            if (x === n - 1n) boule = false;
        }
        if (boule) return false
    }

    return true;
}

function euclide(a, b, u0 = 1n, v0 = 0n, u1 = 0n, v1 = 1n) {
    a = BigInt(a)
    b = BigInt(b)
    if (b === 1n) return [u1, v1]
    return euclide(b, a % b, u1, v1, u0 - u1 * (a / b), v0 - v1 * a / b)
}

function inverse(x, n) {
    let inv = euclide(x, n)[0]
    if (inv < 0) return inv + n
    return (inv % n)
}


function key_gen(k) {
    let p = BigInt(10);
    let q = BigInt(10);
    while (!miller_rabin(p)) {
        p = random(Math.floor(k / 2));
    }
    while (!miller_rabin(q)) {
        q = random(Math.floor(k / 2));
    }
    if (p === q) return;
    let N = p * q
    let phiN = (p - 1n) * (q - 1n)
    let e = 65537n
    while (gcd(e, phiN) !== 1n) e = getRandomBigInt(3, phi - 1)
    let d = inverse(e, phiN)
    // console.log("les clés sont prêtes ZEBI")
    return [e, d, N, p, q, phiN]
}

function E(M, e, N) {
    return powerMod(M, e, N)
}

function D(C, d, N) {
    return powerMod(C, d, N)
}

function getKeyByValue(value) {
    return Object.keys(dick).find(key => dick[key] === value);
}

function dec2bin(dec) {
    return (dec >> 0n).toString(2);
}


function int_str(s) {
    let b = dec2bin(n)// Ceci est un string in memory of Ben
    while (b.length % 6 !== 0) b = "0" + b
    let char = []
    for (let i = 0; i < Math.floor(b.length / 6); ++i) {
        let slice = parseInt(b.slice(i * 6, i * 6 + 6), 2)
        char.push(slice)
    }
    char = char.reverse()
    let string = ""
    for (c in char) {
        let kar = getKeyByValue(char[c])
        let string = string + kar
    }
    return string
}

function str_int(s) {
    let n = 0n
    let indice = 0
    for (let i = 0n; i < s.length; ++i) {
        let kar = s[i]
        let exp = 6n * i
        n += BigInt(dick[kar]) * (2n ** exp)
    }
    return n
}

function encrypt(m, e, N) {
    let texteint = str_int(m)
    return E(texteint, e, N);
}

function decrypt(c, d, N) {
    let texte = D(c, d, N)
    return int_str(texte)
}


// x = key_gen(1024)
// e = x[0]
// d = x[1]
// N = x[2]
// texte = encrypt("je mappelle Son jai 56 ans et je recherche un emploi", e, N)
// d = decrypt(texte, d, N)



























