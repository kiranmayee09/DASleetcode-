class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n = students.size();

        queue<int> studentQueue;
        stack<int> sandwichesStack;

        // Put students into queue
        for (int i = 0; i < n; i++) {
            studentQueue.push(students[i]);
        }

        // Put sandwiches into stack
        for (int i = n - 1; i >= 0; i--) {
            sandwichesStack.push(sandwiches[i]);
        }

        int sandwichMissed = 0;

        while (!studentQueue.empty()) {
            if (sandwichesStack.top() == studentQueue.front()) {
                sandwichesStack.pop();
                studentQueue.pop();
                sandwichMissed = 0;
            } else {
                studentQueue.push(studentQueue.front());
                studentQueue.pop();
                sandwichMissed++;

                if (sandwichMissed == studentQueue.size())
                    break;
            }
        }

        return studentQueue.size();
    }
};