// 13회 10번 해설 소스코드

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 16 // 최대 문자열 개수
#define MAXL 1001 // 최대 문자열 길이
#define INF 999999999 // INFINITY 로 어떤 수와 비교해도 가장 큰 수

int cnt[MAXN][26]; // 문자열의 a~z 26 개의 알파벳 개수
int dp[1 << MAXN]; // 최대 문자열 조합 경우의 수 2^16 만큼 필요

//문자열 조합 x 에서 중복 알파벳 개수 계산합니다
int calc_pref(int n, int x) {
	int len = 0; // 중복 알파벳 개수
	int temp[26]; // 알파벳별로 최소로 존재하는 개수 저장

	// temp 배열을 최댓값으로 초기화합니다
	for (int i = 0; i < 26; i++) {
		temp[i] = INF;
	}

	for (int i = 0; i < n; i++) {
		if (x & (1 << i)) // i번째 문자열 포함 확인 합니다
			for (int j = 0; j < 26; j++)
				// temp[j]와 cnt i ][중 작은 값 선택합니다
				temp[j] = (temp[j] > cnt[i][j]) ? cnt[i][j] : temp[j];
	}

	// temp 전부 더합니다
	for (int i = 0; i < 26; i++)
		len += temp[i];

	return len;
}

//문자열 2 가지 조합으로 나눕니다
int solve(int n, int x) {
	//한 번 계산한 dp 는 다시 계산하지 않고 이전 계산 결과 활용
	if (dp[x] != -1) return dp[x];

	//문자열 조합 x 에서 모두 중복되는 알파벳 개수를 계산합니다
	int pref = calc_pref(n, x);

	// x가 2 의 제곱수인지 확인
	// =>문자열 1 개만 포함한 조합인 경우
	//해당 문자열의 알파벳 개수 리턴
	if ((x & -x) == x) return dp[x] = pref;

	// 모든 문자열 조합 모두 순회
	dp[x] = INF;
	for (int i = (x - 1) & x; i > 0; i = (i - 1) & x) {
		int curr = solve(n, i) + solve(n, x ^ i) - pref;
		dp[x] = (dp[x] > curr) ? curr : dp[x];
	}

	return dp[x];
}

int solution(int n, char str[][MAXL]) // n은 문자열 개수
{
	// 아직 dp 배열 계산하기 전이므로 dp 배열 -1 로 초기화합니다
	memset(dp, -1, sizeof(dp));

	// i번째 문자열의 알파벳 개수를 인덱스에 맞추어 모두 저장합니다
	for (int i = 0; i < n; i++) {
		for (int j = 0; str[i][j]; j++) {
			cnt[i][str[i][j] - 'a']++;
		}
	}
	return solve(n, (1 << n) - 1) + 1; // solve(2^n 1) 실행 후 +1
}

int main(void) {
	int n;
	char str[MAXN][MAXL];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%s", str[i]);
	}

	printf("%d", solution(n, str));
}
