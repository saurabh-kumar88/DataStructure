function mergeSort(arr){

  if (arr.length > 1) {
    var mid = Math.floor( arr.length/2 )
    var L = arr.slice(0,mid)
    var R = arr.slice(mid, arr.length)

    mergeSort(L)
    mergeSort(R)

    // sorting
    var i, j, k = 0
    while (i < L.length) {
      if (L[i] < R[j]) {
        arr[k] = L[i]
        i++
      }
      else{
         arr[k] = R[j]
         j++ 
      }
      k++
    }
    // check for left elements
    while(i < L.length){
      arr[k] = L[i]
      i++
      k++
    }
    while(j < R.length ){
      arr[k] = R[j]
      j++
      k++
    }


  }

};


// driver code
var Arr = [45,13,29,87,44,39]
console.log("Orignal array : " + Arr)
var res = mergeSort(Arr)
console.log("After sorting : " + res )






