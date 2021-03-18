// EPPER 13ȸ 10�� �ؼ�

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 16		 // ���ξ� ������ �ִ밪
#define MAXL 1<<20	// str�迭�� �ִ� ����. str �迭�� ���������� �����ϱ� ����.
#define inf 1 << 30	// �ڵ� ������ infinite ��, ���� ū ���� ǥ��.

int n; // �Է¹޴� ���ξ��� ����
char str[MAXN][MAXL];	// ���ξ �Է¹޾� ������ �迭
int cnt[MAXN][26];	// �Է¹��� ���ξ�� ���ĺ��� ��� �ִ��� ī��Ʈ.
int dp[1 << MAXN];	// << : ù��° �ǿ����ڸ� �������� �ι�° �ǿ����ڸ�ŭ ����Ʈ. 

int calc_pref(int mask) {
	int len = 0;
	int tmp[26];
	// tmp�迭�� ������ ��� inf������ �ʱ�ȭ.
	for (int i = 0; i < 26; i++) {
		tmp[i] = inf;
	}

	// mask�� �������� ��Ÿ������ �� i��° �ڸ����� 1�� i���� �ܾ� �迭���� i��° �ܾ��� �󵵼� �� �� ���� ���� ���� �����ϴ� �ݺ���.
	for (int i = 0; i < n; i++) {
		if (mask&(1 << i))
			for (int j = 0; j < 26; j++)
				tmp[j] = (tmp[j] > cnt[i][j]) ? cnt[i][j] : tmp[j]; //tmp[j]�� cnt[i][j]�� ���� ���� ����
	}

	// ���������� ������ tmp�� ���� ��� ���� ���� len�� �����Ͽ� return.
	for (int i = 0; i < 26; i++)
		len += tmp[i];

	return len;
}

// solve�� return ���� mask�� 2�� �������� ���� pref���� ��ȯ�ϰ� �ƴҶ��� �� ���� ����� �� ���� 2�� ��������°�� pref�� ū ���� ������.
int solve(int mask) {
	// ret�� dp[mask]�� ����Ű�� ret�� ���� �ٲ� �� dp[mask]�� ���� ���� �ٲ��.
	int *ret = &dp[mask];
	// ret�� ���� -1�� �ƴ϶�� ret�� ���� ��ȯ�Ѵ�. solve(mask)�� �̹� ����Ǿ��ٸ� ret�� ���� -1�� �ƴϰԵȴ�.
	if (*ret != -1) return *ret;
	// pref�� ���� mask�� �������� ��Ÿ�������� 1�� ��ġ�� �ε����� ������ �ܾ�� �� ���� ���� �󵵼��� ���� ������ ������.
	int pref = calc_pref(mask);
	// mask&(-mask) �� mask�� lowest set bit�� ã�Ƴ���. mask�� 2�� �������� �� pref�� ���� ret�� �����ϰ� �� ���� return �Ѵ�.
	if ((mask&-mask) == mask) return *ret = pref;
	// ���� ���� curr ���� �����ϱ� ���� ret�� inf ������ �ٲ۴�.
	*ret = inf;
	for (int i = (mask - 1) & mask; i > 0; i = (i - 1)&mask) {
		int curr = solve(i) + solve(mask^i) - pref;
		*ret = (*ret > curr) ? curr : *ret;
	}
	return *ret;
}


int main(void) {
	memset(dp, -1, sizeof(dp));	// dp �迭�� ���� ��� 1�� �ʱ�ȭ.
	scanf("%d", &n); // ���ξ��� ������ �Է¹���
					 //���ξ �Է¹���
	for (int i = 0; i < n; ++i)
		scanf("%s", str[i]);

	for (int i = 0; i < n; i++) {
		// str[i][j]�� null�� �ƴҶ�����, �� str[i]�� ������ ���ڱ��� �ݺ��� ����
		for (int j = 0; str[i][j]; j++) {
			cnt[i][str[i][j] - 'a']++;	// str[i] �ܾ��� j��° ���ĺ��� ��� ���Դ��� ī��Ʈ
		}
	}

	printf("%d\n", solve((1 << n) - 1) + 1);

	return 0;
}
