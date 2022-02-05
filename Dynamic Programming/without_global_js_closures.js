 
function f() {
	let cache = {};
	return function f(n) {
		if(n in cache){
			return cache[n];
		}
		else {
			if (n<2) {
				return cache[n]
			}
			else{
				cache[n] = f(n-1) + f(n-2);
				return cache[n]
			}
		}
	}
}

const fib = f();
output = fib(5);
console.log(output); 
output = fib(7);
console.log(output); 
output = fib(9);
console.log(output); 


