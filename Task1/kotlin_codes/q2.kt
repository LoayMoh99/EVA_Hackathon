// Loay Mohamed
// Challeng 2:

fun main(args: Array<String>) {
    
    print("Input string to be evaluated:")
    val exp = readLine() ?: ""
    //exp = "(1+2)+(2+7)"
    var stack = mutableListOf<String>();
    var char :String = ""
    for (i in 0 until exp.length ){
        char = exp[i].toString();
        if (char == "(" || char == "+" || char == "-"){
            stack.add(char)
        }
        else if (char == ")"){
            // get the index of "("
            var index = stack.size-1
            while (stack[index] != "(" ){
                index--
            }

            var enter = false
            while (stack[stack.size-1] != "(" )
            {
                //case (-num)
                if (stack[index] == "(" && stack[index+1] == "-" ){
                    val num = stack[index+2].toInt()
                    stack.removeAt(index+2)
                    stack.removeLast() // pop "-"
                    stack.removeLast() // pop "("
                    stack.add((-1*num).toString())
                    break;
                }
                if(!enter){
                    index++
                    enter = true
                }
                val x = stack[index].toInt()
                stack.removeAt(index)
                if(stack[stack.size-1] == "("){
                    stack.removeLast()
                    stack.add(x.toString())
                    break;
                }
                else {
                    val oper = stack[index]
                    stack.removeAt(index)
                    val y = stack[index].toInt()

                    if(oper == "+"){ // oper is plus
                        stack[index] = (x+y).toString()
                    }
                    else { // oper is minus
                        stack[index] = (x-y).toString()
                    }
                }
            }
        }
        else if (char == " "){
            continue;
        }
        else{
            stack.add(char)
        }
    }

    if(stack.size > 1){
        var index =0
        while(stack.size > 1){
            val x = stack[index].toInt()
            stack.removeAt(index)

            if (stack.size == 1 && stack[stack.size-1]=="("){
                stack.removeLast()
                stack.add(x.toString())
                break;
            }
            else{
                val oper = stack[index]
                stack.removeAt(index)
                val y = stack[index].toInt()

                if(oper == "+"){ // oper is plus
                    stack[index] = (x+y).toString()
                }
                else { // oper is minus
                    stack[index] = (x-y).toString()
                }
            }
        }
    }

    println(stack[0])
    stack.removeAt(0)
}