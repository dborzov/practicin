package main  

import ("strconv"
		"fmt"
)

type TTT [3][3]rune


func (t TTT) IsWon() bool {
	endgames := make(map[string]int)
	positions := map[string][]string{
		// corners
		"0,0": []string{"w","n","\\"},
		"0,2": []string{"w","s","/"},
		"2,0": []string{"n","e","/"},
		"2,2": []string{"s","e","\\"},
		// edges
		"1,0": []string{"!","n"},
		"0,1": []string{"-","w"},
		"2,1": []string{"e","-"},
		"1,2": []string{"!","s"},
		//center
		"1,1": []string{"/","\\","!","-"},
	}

	var cur []string
	for i:=0; i<3; i++ {
		for j:=0; j<3; j++ {
			cur = positions[strconv.Itoa(i) + "," + strconv.Itoa(j)]
			if t[i][j] != ' ' {
				for k:=0; k< len(cur); k++ {
					if v, ok := endgames[string(t[i][j]) + cur[k]]; ok {
						endgames[string(t[i][j]) + cur[k]] = v + 1
					}  else {
						endgames[string(t[i][j]) + cur[k]] = 1
					}
				}
			}
		}
	}

	fmt.Printf("Here is the winning counter: %v \n", endgames)

	for l, v:=range endgames {
		if v==3 {
			fmt.Printf("%v for the WIN!!!\n", l)
			return true
		}
	}
	return false
}

func main() {
	m := TTT([3][3]rune{
		    [3]rune{'x','o','x'},
		    [3]rune{'o','x','o'},
		    [3]rune{' ',' ',' '},
		})

	m.IsWon()
}