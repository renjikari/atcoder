package main

import (
        "fmt"
        )

func main() {
    var N,S,T int
    fmt.Scan(&N,&S,&T)

    var w,ans int
    for i:=0; i<N; i++{
       var s int
       fmt.Scan(&s)
       w += s
       if S<=w && w<=T{
           ans+=1
       }
    }
    fmt.Println(ans)
}
