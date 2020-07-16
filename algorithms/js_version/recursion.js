/** reverse the string using recursion */
function reverse_String(string, i){
  
  if (i > string.length) {
    return
    
  } else {
    console.log(string[string.length - i] )
    i++
    reverse_String(string, i)
    
  }
}


// reverse_String("foo bar", 1)

/** Mobile keypad possible word combinations */


 
function keypad_wordFormation(arr){

  const mobile_keypad = { 
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PRQS",
    8 : "TUV",
    9 : "WXYZ",
  }
  str1 = mobile_keypad[ arr[0] ]
  str2 = mobile_keypad[ arr[1] ]
  str3 = mobile_keypad[ arr[2] ]

  k = 0
  while ( k <  str3.length ) {
    for (let j = 0; j < str2.length; j++) {
      for (let i = 0; i < str1.length; i++) {
        console.log( str1[i] + str2[j] + str3[k] )
        
      }
      console.log(" ")
    }
    
  k++
  }

 };

 keypad_wordFormation( [2,3,4] )



