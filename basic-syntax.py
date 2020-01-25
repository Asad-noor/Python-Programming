print("Hello, World!")

#Data structrues - assume the gap as run command
var1 = "sam"
var1

var1 = 'cool'
var1

#so variables are just temporary storage basis

#every variable is associated with a data-type
var1 = 12
type(var1)

var1 = True //not true or TRUE
type(var1)

var1 = 4 + 8j
type(var1) //prints complex

#String manipulation
var1 = "Hello, World!"
var1[0] //prints 'H'
var1[-1] //prints '!'
var1[-13] //prints 'H'

len(var1) //prints 13

var1[1:12] //prints 'ello, World' substring

var1.upper() //prints 'HELLO, WORLD!'

var1 + " gg" //string concat prints 'Hello, World! gg'

var1 * 2 //string multiply prints 'Hello, World!Hello, World!'

'example '.strip() //works as trim prints 'example'

'This string has five words'.split() //spilt blank prints ['This', 'string', 'has', 'five', 'words']

'one,two,three,four,five'.split(',') //comma separated to list conversion prints ['one', 'two', 'three', 'four', 'five']

' '.join(['This', 'string', 'has', 'five', 'words']) //join space -> 'This string has five words'

','.join(['one', 'two', 'three', 'four', 'five']) //join comma -> 'one,two,three,four,five'
