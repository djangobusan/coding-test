// https://school.programmers.co.kr/learn/courses/30/lessons/43164

package com.sangkon.programmers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class TravelRoute {

	private HashMap<String, ArrayList<String>> arrivalsByDeparture = new HashMap<>();
	private HashMap<String, Integer> counts = new HashMap<>();
	private Stack<String> answer = new Stack<>();
	private int n;

	boolean DFS(String now) {
		if (answer.size() == n + 1) {
			return true;
		} else {
			for (String next : arrivalsByDeparture.getOrDefault(now, new ArrayList<>())) {
				int count = counts.get(now + next);
				if (count > 0) {
					counts.put(now + next, count - 1);
					answer.push(next);
					if (DFS(next))
						return true;
					answer.pop();
					counts.put(now + next, count);
				}
			}
		}

		return false;
	}

	public String[] solution(String[][] tickets) {
		n = tickets.length;

		for (String[] ticket : tickets) {
			String departure = ticket[0];
			String arrival = ticket[1];

			ArrayList<String> arrivals = arrivalsByDeparture.getOrDefault(departure, new ArrayList<>());
			arrivals.add(arrival);
			arrivalsByDeparture.put(departure, arrivals);

			int count = counts.getOrDefault(departure + arrival, 0);
			counts.put(departure + arrival, count + 1);
		}

		for (Map.Entry<String, ArrayList<String>> entry : arrivalsByDeparture.entrySet()) {
			ArrayList<String> arrivals = entry.getValue();
			arrivals.sort((a, b) -> a.compareTo(b));
		}

		answer.add("ICN");
		DFS("ICN");

		return answer.toArray(new String[0]);
	}

}
