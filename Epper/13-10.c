// EPPER 13회 10번 해설

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 16		 // 접두어 개수의 최대값
#define MAXL 1<<20	// str배열의 최대 길이. str 배열을 전역변수로 선언하기 위함.
#define inf 1 << 30	// 코드 내에서 infinite 값, 가장 큰 값을 표현.

int n; // 입력받는 접두어의 개수
char str[MAXN][MAXL];	// 접두어를 입력받아 저장할 배열
int cnt[MAXN][26];	// 입력받은 접두어마다 알파벳이 몇개씩 있는지 카운트.
int dp[1 << MAXN];	// << : 첫번째 피연산자를 왼쪽으로 두번째 피연산자만큼 쉬프트. 

int calc_pref(int mask) {
	int len = 0;
	int tmp[26];
	// tmp배열의 값으로 모두 inf값으로 초기화.
	for (int i = 0; i < 26; i++) {
		tmp[i] = inf;
	}

	// mask를 이진수로 나타내었을 때 i번째 자리수가 1인 i에서 단어 배열에서 i번째 단어의 빈도수 들 중 가장 작은 값을 선택하는 반복문.
	for (int i = 0; i < n; i++) {
		if (mask&(1 << i))
			for (int j = 0; j < 26; j++)
				tmp[j] = (tmp[j] > cnt[i][j]) ? cnt[i][j] : tmp[j]; //tmp[j]와 cnt[i][j]중 작은 값을 선택
	}

	// 최종적으로 정해진 tmp의 값을 모두 더한 값을 len에 저장하여 return.
	for (int i = 0; i < 26; i++)
		len += tmp[i];

	return len;
}

// solve의 return 값은 mask가 2의 제곱수일 때는 pref값을 반환하고 아닐때는 그 수를 만드는 두 개의 2의 제곱수번째의 pref중 큰 값을 가진다.
int solve(int mask) {
	// ret는 dp[mask]를 가리키고 ret의 값이 바뀔 때 dp[mask]의 값도 같이 바뀐다.
	int *ret = &dp[mask];
	// ret의 값이 -1이 아니라면 ret의 값을 반환한다. solve(mask)가 이미 실행되었다면 ret의 값이 -1이 아니게된다.
	if (*ret != -1) return *ret;
	// pref의 값은 mask를 이진수로 나타내었을때 1인 위치를 인덱스로 가지는 단어들 중 가장 작은 빈도수의 합을 값으로 가진다.
	int pref = calc_pref(mask);
	// mask&(-mask) 는 mask의 lowest set bit을 찾아낸다. mask가 2의 제곱수일 때 pref의 값을 ret에 저장하고 그 값을 return 한다.
	if ((mask&-mask) == mask) return *ret = pref;
	// 가장 작은 curr 값을 저장하기 위해 ret를 inf 값으로 바꾼다.
	*ret = inf;
	for (int i = (mask - 1) & mask; i > 0; i = (i - 1)&mask) {
		int curr = solve(i) + solve(mask^i) - pref;
		*ret = (*ret > curr) ? curr : *ret;
	}
	return *ret;
}


int main(void) {
	memset(dp, -1, sizeof(dp));	// dp 배열의 값을 모두 1로 초기화.
	scanf("%d", &n); // 접두어의 개수를 입력받음
					 //접두어를 입력받음
	for (int i = 0; i < n; ++i)
		scanf("%s", str[i]);

	for (int i = 0; i < n; i++) {
		// str[i][j]가 null이 아닐때까지, 즉 str[i]의 마지막 글자까지 반복문 실행
		for (int j = 0; str[i][j]; j++) {
			cnt[i][str[i][j] - 'a']++;	// str[i] 단어의 j번째 알파벳이 몇번 나왔는지 카운트
		}
	}

	printf("%d\n", solve((1 << n) - 1) + 1);

	return 0;
}
