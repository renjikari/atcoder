package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin) // 標準入力を受け付けるスキャナ
	sc.Scan()                        // １行分の入力を取得する
	inputs := strings.Split(sc.Text(), " ")
	inputs_int := []int{}
	for _, v := range inputs {
		i, _ := strconv.Atoi(v)
		inputs_int = append(inputs_int, i)
	}

	if float64(inputs_int[1])/float64(inputs_int[0]) > float64(inputs_int[3])/float64(inputs_int[2]) {
		fmt.Println("TAKAHASHI")
	} else if float64(inputs_int[1])/float64(inputs_int[0]) < float64(inputs_int[3])/float64(inputs_int[2]) {
		fmt.Println("AOKI")
	} else {
		fmt.Println("DRAW")
	}
}
