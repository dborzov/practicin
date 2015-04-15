package lcs

func LongestCommonSubstring(P, Q string) (lcs string) {
	N := len(P)
	M := len(Q)
	if N == 0 || M == 0 {
		return ""
	}

	A := make([][]binds, N)
	for i := 0; i < N; i++ {
		A[i] = make([]binds, M)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if P[i] != Q[j] {
				// when not matched,
				// we take the longest subseq from A[i-1,j] and A[i,j-1]
				if i != 0 {
					if A[i-1][j].Len() > A[i][j].Len() {
						A[i][j] = A[i-1][j]
					}
				}
				if j != 0 {
					if A[i][j-1].Len() > A[i][j].Len() {
						A[i][j] = A[i][j-1]
					}
				}
				continue
			}
			// the pointer symbols match
			left := 0
			parent := make(binds, 0)

			if i != 0 {
				left = A[i-1][j].Len()
				parent = A[i-1][j][:]
			}
			upper := 0
			if j != 0 {
				upper = A[i][j-1].Len()
				parent = A[i][j-1][:]
			}
			if upper == left {
				A[i][j] = append(parent, i, j)
				continue // does nothing, for readability
			}

			if upper > left {
				A[i][j] = A[i][j-1]
			} else {
				A[i][j] = A[i-1][j]
			}

		}
	}

	return A[N-1][M-1].ForString(P)
}

// binds stores pairs of symbol indices within strings
// that make up common substring
type binds []int

func (b binds) Len() int {
	return len(b) / 2
}

func (b binds) ForString(P string) string {
	var out []byte
	for i := 0; i < len(b); i += 2 {
		out = append(out, P[b[i]])
	}
	return string(out)
}
