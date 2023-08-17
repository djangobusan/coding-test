package com.sangkon.programmers;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class FindPrimeTest {

	@Test
	void testFindPrime() {
		FindPrime findPrime = new FindPrime();
		assertEquals(findPrime.solution("17"), 3);
		assertEquals(findPrime.solution("011"), 2);
	}

}
