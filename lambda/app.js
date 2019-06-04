exports.handler = (event, context, callback) => {
   var number1 = event.Number1;
   var number2 = event.Number2;
   var sum = number1 + number2;
   var product = number1 * number2;
   var difference = Math.abs(number1 - number2);
   var quotient = number1 / number2;
   callback(null, {
       "Number1": number1,
       "Number2": number2,
       "Sum": sum,
       "Product": product,
       "Difference": difference,
       "Quotient": quotient
   });
};
