package main

import (
        "fmt"
        "os"
        )

func main() {
    var N,a,b,K int
    fmt.Scan(&N,&a,&b,&K)

    var num int

    P:= make([]int, K)
    for i:=0; i<K; i++{
        fmt.Scan(&num)
        P[i] = num
    }
    all:=P

    if arrayContains(P, a){
        fmt.Println("NO")
        os.Exit(0)
    }

    if arrayContains(P, b){
        fmt.Println("NO")
        os.Exit(0)
    }

    for _, i:=range P{
        // iがallにあるか
        if arrayContains(all, i){
            // iをallから削除
            all = remove(all, i)
        }else{
            fmt.Println("NO")
            os.Exit(0)
        }
    }
    fmt.Println("YES")

}

func arrayContains(arr []int, i int) bool{
  for _, v := range arr{
    //fmt.Println(v)
    if v == i{
        return true
    }
  }
  return false
}


func remove(arr []int, search int) []int {
    result := []int{}
    for _, v := range arr {
        if v != search {
            result = append(result, v)
        }
    }
    return result
}

func getIntSlice(n int) []int{
	b := make([]int, n)
	for i:=0;i<n ;i++  {
		//b[i] = nint()
	}
	return b
}
