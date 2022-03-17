
function random(k){
k = Math.floor(k/4);
const hexString = Array(k)
  .fill()
  .map(() => Math.round(Math.random() * 0xF).toString(16))
  .join('');
return randomBigInt = BigInt(`0x${hexString}`);
}

function gcd(a, b) {
  if (!b) return a
  return gcd(b, a % b)
}


function getRandomBigInt(lower,upper) {
  let maxInt = BigInt(Number.MAX_SAFE_INTEGER);
  if (upper <= maxInt) {
      x= BigInt((Math.floor(Math.random()*Number(upper))));
      while(x<lower|| x > upper){x=BigInt((Math.floor(Math.random()*Number(upper))));}
      return x
  } else {
      x= BigInt((Math.floor(Math.random()*Number(upper))));
      while(x<lower||x > upper){x=BigInt((Math.floor(Math.random()*Number(upper))));}
      return BigInt((Math.floor(Math.random()*Number.MAX_SAFE_INTEGER)));
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

function is_prime(n){
  for (let i= 2n; i< sqrt(n)+1n;++i)
        {if (n % i == 0n)return false}
    return true
}



function miller_rabin(n,k=40){
if(n==2) return true;

if(n%2n==0) return false;

s=BigInt(0);
t=n-1n;

while (t%2n==0){
  s+=1n;
  t=t/2n;
}

for(let i=0; i<k;++i) {
    a= getRandomBigInt(2,n-3n); 
    x= modExp(a,t,n);
    if( x== 1n || x== (n-1n)) continue;
    boule = true;
    for(let j=0; j< s-1n ; ++j){
    x=modExp(x,2n,n);
    if(x== n-1n) boule=false;}
    if (boule) return false
}

return true;
}

function euclide(a, b, u0 = 1n, v0 = 0n, u1 = 0n, v1 = 1n) {
  a=BigInt(a)
  b=BigInt(b)
  if (b === 1n) return [u1, v1]
  return euclide(b, a % b, u1, v1, u0 - u1 * (a / b), v0 - v1 * a / b)
}

function inverse(x, n) {
 inv= euclide(x, n)[0]
 if (inv < 0) return inv+n
 return (inv%n)
}




function key_gen(k){
p= BigInt(10);
q=BigInt(10);
while(!miller_rabin(p)) {p = random(Math.floor(k/2));}
while(!miller_rabin(q)) {q = random(Math.floor(k/2));}
if(p==q) return;
N=p*q
phiN = (p-1n)*(q-1n)
e = 65537n
while (gcd(e,phiN) != 1n) e = getRandomBigInt(3,phi-1)
d=inverse(e,phiN)
console.log("les clés sont prêtes ZEBI")
return new Array(e,d,N,p,q,phiN)
}

function E(M,e,N){return powerMod(M,e,N)}

function D(C,d,N){return powerMod(C,d,N)}

x=key_gen(512)
console.log("pk",x[0])
console.log("sk",x[1])
console.log("N",x[2])

c = E(10000000000000000000000,x[0],x[2])
console.log("c",c)
d = D(c,x[1],x[2])
console.log("d",d)