package com.sangkon.programmers;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class TestProgrammers {

	@Test
	void testFindPrime() {
		FindPrime findPrime = new FindPrime();
		assertEquals(findPrime.solution("17"), 3);
		assertEquals(findPrime.solution("011"), 2);
	}

	@Test
	void testTravelRoute() {
		TravelRoute travelRoute1 = new TravelRoute();
		String[][] input1 = new String[][] { { "ICN", "JFK" }, { "HND", "IAD" }, { "JFK", "HND" } };
		String[] output1 = new String[] { "ICN", "JFK", "HND", "IAD" };

		TravelRoute travelRoute2 = new TravelRoute();
		String[][] input2 = new String[][] { { "ICN", "SFO" }, { "ICN", "ATL" }, { "SFO", "ATL" }, { "ATL", "ICN" },
				{ "ATL", "SFO" } };
		String[] output2 = new String[] { "ICN", "ATL", "ICN", "SFO", "ATL", "SFO" };

		assertArrayEquals(travelRoute1.solution(input1), output1);
		assertArrayEquals(travelRoute2.solution(input2), output2);
	}

}
