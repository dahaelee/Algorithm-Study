// 13ȸ 10�� �ؼ� �ҽ��ڵ�

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 16 // �ִ� ���ڿ� ����
#define MAXL 1001 // �ִ� ���ڿ� ����
#define INF 999999999 // INFINITY �� � ���� ���ص� ���� ū ��

int cnt[MAXN][26]; // ���ڿ��� a~z 26 ���� ���ĺ� ����
int dp[1 << MAXN]; // �ִ� ���ڿ� ���� ����� �� 2^16 ��ŭ �ʿ�

//���ڿ� ���� x ���� �ߺ� ���ĺ� ���� ����մϴ�
int calc_pref(int n, int x) {
	int len = 0; // �ߺ� ���ĺ� ����
	int temp[26]; // ���ĺ����� �ּҷ� �����ϴ� ���� ����

	// temp �迭�� �ִ����� �ʱ�ȭ�մϴ�
	for (int i = 0; i < 26; i++) {
		temp[i] = INF;
	}

	for (int i = 0; i < n; i++) {
		if (x & (1 << i)) // i��° ���ڿ� ���� Ȯ�� �մϴ�
			for (int j = 0; j < 26; j++)
				// temp[j]�� cnt i ][�� ���� �� �����մϴ�
				temp[j] = (temp[j] > cnt[i][j]) ? cnt[i][j] : temp[j];
	}

	// temp ���� ���մϴ�
	for (int i = 0; i < 26; i++)
		len += temp[i];

	return len;
}

//���ڿ� 2 ���� �������� �����ϴ�
int solve(int n, int x) {
	//�� �� ����� dp �� �ٽ� ������� �ʰ� ���� ��� ��� Ȱ��
	if (dp[x] != -1) return dp[x];

	//���ڿ� ���� x ���� ��� �ߺ��Ǵ� ���ĺ� ������ ����մϴ�
	int pref = calc_pref(n, x);

	// x�� 2 �� ���������� Ȯ��
	// =>���ڿ� 1 ���� ������ ������ ���
	//�ش� ���ڿ��� ���ĺ� ���� ����
	if ((x & -x) == x) return dp[x] = pref;

	// ��� ���ڿ� ���� ��� ��ȸ
	dp[x] = INF;
	for (int i = (x - 1) & x; i > 0; i = (i - 1) & x) {
		int curr = solve(n, i) + solve(n, x ^ i) - pref;
		dp[x] = (dp[x] > curr) ? curr : dp[x];
	}

	return dp[x];
}

int solution(int n, char str[][MAXL]) // n�� ���ڿ� ����
{
	// ���� dp �迭 ����ϱ� ���̹Ƿ� dp �迭 -1 �� �ʱ�ȭ�մϴ�
	memset(dp, -1, sizeof(dp));

	// i��° ���ڿ��� ���ĺ� ������ �ε����� ���߾� ��� �����մϴ�
	for (int i = 0; i < n; i++) {
		for (int j = 0; str[i][j]; j++) {
			cnt[i][str[i][j] - 'a']++;
		}
	}
	return solve(n, (1 << n) - 1) + 1; // solve(2^n 1) ���� �� +1
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
