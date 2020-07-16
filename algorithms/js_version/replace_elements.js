/** Replace each element of array by product of rest of elements in O(n) time */

/** Using recursive function */
function replace_elements(A, i){
  var left_sub = null
  var left_sub = null

  n = A.length

    // base case
    if (i > n-1) {
      return A
    }

    if (i==0) {
      left_sub = 1
      right_sub = A.slice(i+1, n)
    }else if(i==1){
      left_sub = A[0]
      right_sub = A.slice(i+1, n)
    }
    else if(i==n){
      right_sub = 1
      left_sub = A.slice(0, i-1)    
    }else{
      left_sub = A.slice( 0, i-1 )
      right_sub = A.slice( i+1, n )
    }

    console.log(i + " " + left_sub)
    // console.log(`index:  ${i} value : ${A[i]}`)
    // console.log(right_sub)
    // replace current element 
    // A[i] = left_sub.reduce(product_of_elements) * right_sub.reduce(product_of_elements) 

    i++

    replace_elements(A, i)

};

function product_of_elements(num, product){
  return product * num;

};


arr = [45, 18, 28, 4]

replace_elements(arr, 0)

// test code

// console.log(arr)

var temp = arr.slice(0,2)
// console.log(temp)





