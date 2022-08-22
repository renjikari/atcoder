package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var reader = NewReader()

func main() {
	n := reader.Int()
	s := strings.Split(reader.String(), "")

	thousands := []string{}
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			for k := 0; k < 10; k++ {
				thousands = append(thousands, strconv.Itoa(i)+strconv.Itoa(j)+strconv.Itoa(k))
			}
		}
	}

	one := false
	two := false
	ans := 0
	for t := 0; t < 1000; t++ {
		one = false
		two = false
		for i := 0; i < n; i++ {
			if s[i] == thousands[t][0:1] && !one {
				one = true
				continue
			}
			if one && s[i] == thousands[t][1:2] && !two {
				two = true
				continue
			}
			if two && s[i] == thousands[t][2:3] {
				//fmt.Printf("%#v\n", "3rd")
				//fmt.Printf("%#v\n", i)
				//fmt.Printf("%#v\n", s[i])
				//fmt.Printf("%#v\n", thousands[t])
				ans += 1
				break
			}
		}

	}
	fmt.Println(ans)
}

//階乗
func factorical(n int) int {
	ans := 1
	if n < 0 {
		fmt.Println("n is less than 0")
		os.Exit(1)
	}
	for i := 1; i <= n; i++ {
		ans = ans * i
	}
	return ans
}

//順列
func permutation(n, k int) int {
	if n < k {
		fmt.Println("n is less than k")
		os.Exit(1)
	}
	return factorical(n) / factorical(n-k)
}

//組み合わせ
func combination(n, k int) int {
	if n < k {
		fmt.Println("n is less than k")
		os.Exit(1)
	}
	return permutation(n, k) / factorical(k)
}

// Read
type Reader struct {
	r *bufio.Reader
}

func NewReader() Reader {
	return Reader{bufio.NewReader(os.Stdin)}
}

func (r Reader) String() string {
	line, _ := reader.r.ReadString('\n')
	return strings.TrimRight(line, "\r\n")
}

func (r Reader) Int() int {
	line := r.String()
	v, _ := strconv.Atoi(line)
	return v
}

func (r Reader) IntPair() (int, int) {
	v := strings.Split(r.String(), " ")
	v0, _ := strconv.Atoi(v[0])
	v1, _ := strconv.Atoi(v[1])
	return v0, v1
}

func (r Reader) IntTriple() (int, int, int) {
	v := strings.Split(r.String(), " ")
	v0, _ := strconv.Atoi(v[0])
	v1, _ := strconv.Atoi(v[1])
	v2, _ := strconv.Atoi(v[2])
	return v0, v1, v2
}

func (r Reader) IntQuad() (int, int, int, int) {
	v := strings.Split(r.String(), " ")
	v0, _ := strconv.Atoi(v[0])
	v1, _ := strconv.Atoi(v[1])
	v2, _ := strconv.Atoi(v[2])
	v3, _ := strconv.Atoi(v[3])
	return v0, v1, v2, v3
}

func (r Reader) IntFifth() (int, int, int, int, int) {
	v := strings.Split(r.String(), " ")
	v0, _ := strconv.Atoi(v[0])
	v1, _ := strconv.Atoi(v[1])
	v2, _ := strconv.Atoi(v[2])
	v3, _ := strconv.Atoi(v[3])
	v4, _ := strconv.Atoi(v[4])
	return v0, v1, v2, v3, v4
}

func (r Reader) Ints(n int) []int {
	ans := make([]int, 0, n)
	for _, v := range strings.Split(r.String(), " ") {
		if v == "" {
			continue
		}
		v, _ := strconv.Atoi(v)
		ans = append(ans, v)
	}
	return ans
}

func (r Reader) StringPair() (string, string) {
	v := strings.Split(r.String(), " ")
	return v[0], v[1]
}

func (r Reader) Strings(n int) []string {
	res := make([]string, 0, n)
	for _, v := range strings.Split(r.String(), " ") {
		res = append(res, v)
	}
	return res
}

//calc
func abs(a int) int {
	return int(math.Abs(float64(a)))
}

func pow(p, q int) int {
	return int(math.Pow(float64(p), float64(q)))
}

//min and max

func min(nums ...int) int {
	if len(nums) == 0 {
		panic("funciton min() requires at least one argument.")
	}
	res := nums[0]
	for i := 0; i < len(nums); i++ {
		res = int(math.Min(float64(res), float64(nums[i])))
	}
	return res
}

func max(nums ...int) int {
	if len(nums) == 0 {
		panic("funciton max() requires at least one argument.")
	}
	res := nums[0]
	for i := 0; i < len(nums); i++ {
		res = int(math.Max(float64(res), float64(nums[i])))
	}
	return res
}

// slice to uniq
func Uniq(slice []string) []string {
	m := make(map[string]bool)
	uniq := []string{}
	for _, ele := range slice {
		if !m[ele] {
			m[ele] = true
			uniq = append(uniq, ele)
		}
	}
	return uniq
}
