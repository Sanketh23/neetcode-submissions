class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count_seats = Counter(seats)
        count_students = Counter(students)
        i, j = 0, 0
        res = 0
        length = len(seats)
        while length:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                res += abs(i-j)
                count_seats[i] -= 1
                count_students[j] -= 1
                length -= 1
        
        return res