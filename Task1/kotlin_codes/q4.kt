// Loay Mohamed
// Challeng 4:

class Q4{
    val matrix = arrayOf(arrayOf(-3, 3, -2),arrayOf(-1, 5, -1),arrayOf(3, 5, -2))
    //val matrix = arrayOf(arrayOf(-2, -3, 3),arrayOf(-5, -10, 1),arrayOf(10, 30, -5))
    val n = matrix.size 
    val m = matrix[0].size
    
    fun dungeon(currHealth:Int , i:Int , j:Int) :Boolean {
        var currhealth = currHealth
        print(currhealth)
        print(" ")
        print(i)
        print(" ")
        println(j)
        if(currhealth+matrix[0][0] > 0){
            currhealth =currhealth+ matrix[i][j]
            if (i == n-1 && j == m-1){
                return true
            }

            if (i >= n-1 && j < m-1){
                return dungeon(currhealth, i, j+1)
            }
            if (i < n-1 && j >= m-1){
                return dungeon(currhealth, i+1, j)
            }

            return dungeon(currhealth, i, j+1) || dungeon(currhealth, i+1, j)
        }
        else {
            return false
        }
    }


}
fun main(args: Array<String>) {

    var q4 = Q4()

    if (q4.n == 0 || q4.m == 0){
        println("Invalid Matrix dimensions ")
    }
    for (i in 0 until q4.n) {
        if(q4.matrix[i].size != q4.m){
            println("Invalid Matrix dimensions ")
        }
    }

    var health:Int = 1
    if(q4.matrix[0][0]<0){
        health = -1*q4.matrix[0][0]+1
    }
    println(health)

    while(true){
        if (q4.dungeon(health,0,0)){
            break
        }
        else{
            health++
        }
    }

    println(health)
}
