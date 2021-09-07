// Loay Mohamed
// Challeng 1:

fun main(args: Array<String>) {
    print("Input string s:")
    val s = readLine()
    print("Input string p:")
    val p = readLine()
    
    
    var res: Boolean
    var index_s: Int = 0
    var index_p: Int = 0

    while(index_p < p!!.length && index_s< s!!.length){
        if (s[index_s] == p[index_p] || p[index_p] == '?'){
            index_s += 1
            index_p += 1
        }
        else if (p[index_p] == '*'){
            index_p += 1

            if (index_p == 1)  // at the beginning
                index_s = index_p
            if (index_p == p.length)  // at the end
                index_s = s.length
        }
        else if (s[index_s] != p[index_p])
            break
        else
            index_s += 1
    }

    res = (index_p == p.length) && (index_s == s!!.length)
    // case if * is at the end and crossponds to epmty set
    if (index_s == s!!.length && index_p == p.length-1){
        if (p[index_p] == '*')
            res = true
    }
    // case if empty s and p is only *
    if (s.length == 0 && p.length > 0){
        for (char in p){
            if (char != '*'){
                res = false
                break
            }
            res = true
        }
    }

    println(res)
}