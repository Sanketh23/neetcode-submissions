class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_students = [0] * max_index

        for seat in seats:
            count_seats[seat] += 1
        for student in students:
            count_students[student] += 1
        
        one, two = 0, 0
        res = 0
        remain = len(students)
        while remain:
            if count_seats[one] == 0:
                one += 1
            if count_students[two] == 0:
                two += 1
            if count_seats[one] and count_students[two]:
                res += abs(one - two)
                count_seats[one] -= 1
                count_students[two] -= 1
                remain -= 1
        
        return res
