// https://school.programmers.co.kr/learn/courses/30/lessons/42839

package com.sangkon.programmers;

import java.util.HashSet;
import java.util.Set;

public class FindPrime {

	private boolean isPrime(int n) {
		if (n <= 1)
			return false;
		for (int i = 2; i * i <= n; i++) {
			if (n % i == 0)
				return false;
		}
		return true;
	}

	private void getPrimes(int acc, int[] numbers, boolean[] isUsed, Set<Integer> primes) {
		if (isPrime(acc))
			primes.add(acc);

		for (int i = 0; i < numbers.length; i++) {
			if (isUsed[i])
				continue;

			int nextAcc = acc * 10 + numbers[i];

			isUsed[i] = true;
			getPrimes(nextAcc, numbers, isUsed, primes);
			isUsed[i] = false;
		}
	}

	public int solution(String numbers) {
		Set<Integer> primes = new HashSet<>();
		int[] permutation = numbers.chars().map(c -> c - '0').toArray();
		getPrimes(0, permutation, new boolean[permutation.length], primes);
		return primes.size();
	}
}
